# main.py
if __name__ == '__main__':
    from ui import prompt_items, step_through_dp, navigate_steps
    from knapsack import cari_item_yang_dipilih as traceSolution, hitung_profit_maksimal as fillDP, tampilkan_hasil

    # Ambil input melalui CLI
    weights, profits, capacity = prompt_items()

    # Pilih mode DP: step or final
    mode = input("Pilih mode: (1) Step-through, (2) Final saja: ")
    
    if mode.strip() == '1':
        snapshots = step_through_dp(weights, profits, capacity)
        navigate_steps(snapshots, weights, profits, capacity)
    else:
        # Final mode: langsung hitung dan tampilkan
        DP = fillDP(weights, profits, capacity)
        tampilkan_hasil(
            traceSolution(DP, weights, profits, capacity),
            weights, profits
        )