import sys
from typing import List

def prompt_items() -> (List[int], List[int], int):
    """
    Baca input n, daftar berat, daftar profit, dan kapasitas Knapsack dari CLI dengan validasi.
    """
    try:
        n = int(input("Masukkan jumlah barang (n, minimal 8): "))
        if n < 8:
            raise ValueError
    except ValueError:
        print("Error: n harus integer >= 8.")
        sys.exit(1)

    print("Masukkan berat tiap barang, dipisah spasi:")
    weights = list(map(int, input().split()))
    print("Masukkan profit tiap barang, dipisah spasi:")
    profits = list(map(int, input().split()))

    if len(weights) != n or len(profits) != n:
        print(f"Error: Jumlah berat ({len(weights)}) dan profit ({len(profits)}) harus sama dengan n ({n}).")
        sys.exit(1)
    if any(x <= 0 for x in weights + profits):
        print("Error: Semua berat dan profit harus bilangan positif.")
        sys.exit(1)

    try:
        capacity = int(input("Masukkan kapasitas knapsack (W): "))
        if capacity <= 0:
            raise ValueError
    except ValueError:
        print("Error: Kapasitas harus integer > 0.")
        sys.exit(1)

    return weights, profits, capacity


def display_dp_table(DP: List[List[int]]) -> None:
    """
    Cetak tabel DP dengan header kolom kapasitas dan baris item.
    """
    n = len(DP) - 1
    W = len(DP[0]) - 1
    header = ['k\\w'] + [str(w) for w in range(W+1)]
    print(' | '.join(f"{h:>4}" for h in header))
    print('-' * (6*(W+2)))
    for i in range(n+1):
        row = [str(i)] + [str(DP[i][w]) for w in range(W+1)]
        print(' | '.join(f"{c:>4}" for c in row))


def step_through_dp(weights: List[int], profits: List[int], capacity: int) -> List[List[List[int]]]:
    """
    Bangun tabel DP baris per baris, simpan snapshot setiap tahap.
    """
    from knapsack import hitung_profit_maksimal as fillDP

    n = len(weights)
    DP = [[0] * (capacity+1) for _ in range(n+1)]
    snapshots = []

    for i in range(1, n+1):
        for w in range(capacity+1):
            no_take = DP[i-1][w]
            take = (DP[i-1][w-weights[i-1]] + profits[i-1]) if weights[i-1] <= w else 0
            DP[i][w] = max(no_take, take)
        snapshots.append([row[:] for row in DP])
        print(f"--- Setelah item ke-{i} ---")
        display_dp_table(DP)
        input("Tekan Enter untuk lanjut ke tahap berikutnya...")

    return snapshots


def navigate_steps(snapshots: List[List[List[int]]], weights: List[int], profits: List[int], capacity: int) -> None:
    """
    Navigasi snapshot DP dengan perintah user hingga keluar.
    """
    from knapsack import cari_item_yang_dipilih as traceSolution, tampilkan_hasil

    idx = len(snapshots) - 1
    total = len(snapshots)
    
    while True:
        print(f"\nTahap saat ini: {idx+1}/{total}")
        display_dp_table(snapshots[idx])
        cmd = input("(n)ext, (p)rev, nomor tahap, atau (q)uit: ")
        if cmd.lower() == 'q':
            break
        elif cmd.lower() == 'n' and idx < total-1:
            idx += 1
        elif cmd.lower() == 'p' and idx > 0:
            idx -= 1
        elif cmd.isdigit() and 1 <= int(cmd) <= total:
            idx = int(cmd)-1
        else:
            print("Perintah tidak dikenali.")

    # Setelah navigasi, tampilkan solusi berdasarkan DP terakhir
    final_DP = snapshots[-1]
    picked = traceSolution(final_DP, weights, profits, capacity)
    tampilkan_hasil(picked, weights, profits)


