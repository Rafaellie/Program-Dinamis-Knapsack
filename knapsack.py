# Solusi Knapsack 0/1 dengan Dynamic Programming + Backtracking

from typing import List, Tuple

def hitung_profit_maksimal(daftar_berat: List[int], daftar_profit: List[int], kapasitas_maksimal: int) -> List[List[int]]:
    """
    Fungsi ini menghitung keuntungan maksimal yang bisa didapat
    dengan memilih item-item dengan berat dan profit tertentu,
    agar total berat tidak melebihi kapasitas_maksimal.

    Kita akan membangun tabel 'memo' (seperti catatan)
    berukuran (jumlah_item + 1) x (kapasitas_maksimal + 1).
    memo[i][w] akan menyimpan keuntungan maksimal
    saat mempertimbangkan item dari 0 sampai i-1
    dengan batasan kapasitas w.
    """
    jumlah_item = len(daftar_berat)

    # Buat tabel 'memo' dengan nilai awal 0
    memo = []  # Buat list kosong untuk menampung baris-baris tabel

    jumlah_baris = jumlah_item + 1
    jumlah_kolom = kapasitas_maksimal + 1

    for i in range(jumlah_baris):
        # Untuk setiap baris
        baris_baru = [] # Buat list kosong untuk menampung sel-sel dalam baris ini
        for w in range(jumlah_kolom):
            # Untuk setiap kolom dalam baris ini
            baris_baru.append(0) # Tambahkan nilai 0 ke sel
        memo.append(baris_baru) # Tambahkan baris yang sudah diisi ke tabel memo

    # Isi tabel 'memo' baris demi baris, kolom demi kolom
    for i in range(1, jumlah_item + 1):
        # Untuk setiap item (mulai dari item pertama)
        berat_item_saat_ini = daftar_berat[i - 1]
        profit_item_saat_ini = daftar_profit[i - 1]

        for w in range(0, kapasitas_maksimal + 1):
            # Untuk setiap kemungkinan kapasitas (dari 0 sampai kapasitas_maksimal)

            # Pilihan 1: TIDAK mengambil item saat ini
            # Keuntungan sama dengan keuntungan tanpa mempertimbangkan item ini
            keuntungan_tidak_ambil = memo[i - 1][w]

            # Pilihan 2: Mengambil item saat ini
            # Ini hanya bisa dilakukan jika kapasitas yang tersisa cukup (w >= berat_item_saat_ini)
            keuntungan_ambil = 0  # Awalnya diasumsikan tidak bisa diambil
            if berat_item_saat_ini <= w:
                # Jika kapasitas cukup, keuntungan adalah:
                # keuntungan dari kapasitas yang tersisa setelah mengambil item
                # ditambah profit dari item saat ini
                kapasitas_tersisa = w - berat_item_saat_ini
                keuntungan_ambil = memo[i - 1][kapasitas_tersisa] + profit_item_saat_ini

            # Simpan keuntungan maksimal dari kedua pilihan di tabel memo
            memo[i][w] = max(keuntungan_tidak_ambil, keuntungan_ambil)

    # Tabel memo sudah terisi, keuntungan maksimal ada di memo[jumlah_item][kapasitas_maksimal]
    return memo

def cari_item_yang_dipilih(memo: List[List[int]], daftar_berat: List[int], daftar_profit: List[int], kapasitas_maksimal: int) -> List[int]:
    """
    Fungsi ini melihat kembali tabel 'memo' untuk mengetahui
    item mana saja yang dipilih untuk mendapatkan keuntungan maksimal.
    """
    jumlah_item = len(daftar_berat)
    kapasitas_saat_ini = kapasitas_maksimal
    item_yang_dipilih = []  # Daftar untuk menyimpan indeks item yang dipilih

    # Mulai dari sel paling kanan bawah tabel memo
    # dan bergerak mundur
    for i in range(jumlah_item, 0, -1):
        # Untuk setiap item (dari yang terakhir ke yang pertama)

        # Bandingkan keuntungan di memo[i][kapasitas_saat_ini]
        # dengan keuntungan di memo[i-1][kapasitas_saat_ini]
        if memo[i][kapasitas_saat_ini] != memo[i - 1][kapasitas_saat_ini]:
            # Jika nilainya berbeda, itu artinya item ke i-1 (indeks asli)
            # HARUS diambil untuk mencapai keuntungan di memo[i][kapasitas_saat_ini]

            # Tambahkan indeks item ini ke daftar
            item_yang_dipilih.append(i - 1)

            # Kurangi kapasitas_saat_ini dengan berat item yang baru saja diambil
            berat_item_yang_diambil = daftar_berat[i - 1]
            kapasitas_saat_ini -= berat_item_yang_diambil

    # Balik daftar item_yang_dipilih agar urut dari indeks terkecil
    item_yang_dipilih.reverse()
    return item_yang_dipilih

def ambil_input_pengguna() -> Tuple[List[int], List[int], int]:
    """
    Fungsi ini membaca informasi tentang item dan kapasitas
    dari pengguna melalui input.
    Juga melakukan pengecekan sederhana agar inputnya masuk akal.
    """
    try:
        jumlah_barang = int(input("Masukkan jumlah barang (minimal 8): "))
        if jumlah_barang < 8:
             raise ValueError("Jumlah barang harus minimal 8.")

        print("Masukkan berat tiap barang, pisahkan dengan spasi:")
        input_berat = input().split()
        list_berat = list(map(int, input_berat))

        print("Masukkan profit tiap barang, pisahkan dengan spasi:")
        input_profit = input().split()
        list_profit = list(map(int, input_profit))

        if len(list_berat) != jumlah_barang or len(list_profit) != jumlah_barang:
            raise ValueError(f"Jumlah berat dan profit harus sama dengan jumlah barang ({jumlah_barang}).")

        # Cek apakah ada berat atau profit yang nol atau negatif
        if any(x <= 0 for x in list_berat + list_profit):
             raise ValueError("Semua berat dan profit harus bilangan positif (lebih dari 0).")

        kapasitas_maksimal = int(input("Masukkan kapasitas knapsack (W): "))
        if kapasitas_maksimal <= 0:
             raise ValueError("Kapasitas knapsack harus lebih dari 0.")

    except ValueError as e:
        # Tangkap error jika input tidak sesuai
        raise ValueError("Input Error: " + str(e))
    except Exception as e:
        # Tangkap error lain yang mungkin terjadi
        raise ValueError("Terjadi kesalahan saat membaca input: " + str(e))


    return list_berat, list_profit, kapasitas_maksimal

def tampilkan_hasil(item_yang_dipilih: List[int], daftar_berat: List[int], daftar_profit: List[int]):
    """
    Fungsi ini menampilkan daftar item yang dipilih,
    berat masing-masing, profit masing-masing,
    serta total berat dan total profit.
    """
    print("\n=== Hasil Knapsack ===")
    print(f"{'Indeks':>6} | {'Berat':>5} | {'Profit':>6}")
    print("-" * 22)

    total_berat_terpilih = 0
    total_profit_terpilih = 0

    for indeks_item in item_yang_dipilih:
        berat_item = daftar_berat[indeks_item]
        profit_item = daftar_profit[indeks_item]
        print(f"{indeks_item:>6} | {berat_item:>5} | {profit_item:>6}")
        total_berat_terpilih += berat_item
        total_profit_terpilih += profit_item

    print("-" * 22)
    print(f"{'Total':>6} | {total_berat_terpilih:>5} | {total_profit_terpilih:>6}")

def main():
    """
    Fungsi utama untuk menjalankan seluruh proses.
    """
    try:
        # 1. Ambil input dari pengguna
        list_berat, list_profit, kapasitas_maksimal = ambil_input_pengguna()

        # 2. Hitung keuntungan maksimal dengan tabel DP
        tabel_memo_dp = hitung_profit_maksimal(list_berat, list_profit, kapasitas_maksimal)

        # 3. Cari item mana saja yang dipilih dari tabel DP
        item_terpilih = cari_item_yang_dipilih(tabel_memo_dp, list_berat, list_profit, kapasitas_maksimal)

        # 4. Tampilkan hasilnya
        tampilkan_hasil(item_terpilih, list_berat, list_profit)

    except ValueError as e:
        # Jika ada error saat input atau validasi
        print("TERJADI KESALAHAN:", e)
    except Exception as e:
         # Jika ada error lain saat menjalankan program
         print("TERJADI KESALAHAN UMUM:", e)


if __name__ == "__main__":
    main()
