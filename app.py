# streamlit_app.py
import streamlit as st
from typing import List
from knapsack import (
    hitung_profit_maksimal as fillDP,
    cari_item_yang_dipilih as traceSolution
)

# Konfigurasi halaman
st.set_page_config(
    page_title="Knapsack 0/1 DP Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Knapsack 0/1 Dynamic Programming Explorer")

# Sidebar: Input Parameter
st.sidebar.header("Input Parameter")

n = st.sidebar.number_input(
    "Jumlah barang (n, minimal 8)", min_value=8, value=8, step=1
)
weights_input = st.sidebar.text_input(
    "Berat barang (pisah spasi)", "2 3 4 5 9 7 1 6"
)
profits_input = st.sidebar.text_input(
    "Profit barang (pisah spasi)", "3 4 8 8 10 6 1 7"
)
capacity = st.sidebar.number_input(
    "Kapasitas knapsack (W)", min_value=1, value=15, step=1
)
step_mode = st.sidebar.checkbox("Step-by-Step Mode", value=False)

# Parsing dan validasi input
try:
    weights: List[int] = list(map(int, weights_input.split()))
    profits: List[int] = list(map(int, profits_input.split()))
    if len(weights) != n or len(profits) != n or any(x <= 0 for x in weights+profits):
        raise ValueError
except Exception:
    st.error("Masukkan berat dan profit sesuai format, jumlah = n, nilai > 0.")
    st.stop()

# Hitung tabel DP
memo = fillDP(weights, profits, capacity)

if not step_mode:
    st.subheader("Tabel DP (Final)")
    st.caption("Baris = item ke-k (0…n), Kolom = kapasitas (0…W)")
    st.dataframe(memo)

    st.subheader("Solusi Optimal")
    picked = traceSolution(memo, weights, profits, capacity)
    cols = st.columns(3)
    cols[0].markdown("**Idx**")
    cols[1].markdown("**Berat**")
    cols[2].markdown("**Profit**")
    total_w = total_p = 0
    for i in picked:
        cols[0].write(i)
        cols[1].write(weights[i])
        cols[2].write(profits[i])
        total_w += weights[i]
        total_p += profits[i]
    st.write(f"**Total Berat:** {total_w}  \n**Total Profit:** {total_p}")
else:
    st.subheader("Visualisasi Step-by-Step DP")
    st.caption("Geser slider untuk memilih tahap (item ke-k)")

    # Buat snapshot setiap tahap
    snapshots = []
    n_items = len(weights)
    DP_temp = [[0] * (capacity+1) for _ in range(n_items+1)]
    for i in range(1, n_items+1):
        for w in range(capacity+1):
            no_take = DP_temp[i-1][w]
            take = (DP_temp[i-1][w-weights[i-1]] + profits[i-1]) \
                if weights[i-1] <= w else 0
            DP_temp[i][w] = max(no_take, take)
        snapshots.append([row[:] for row in DP_temp])

    stage = st.slider(
        "Pilih Tahap (1…n)", 1, n_items, 1
    )
    st.write(f"Tabel DP setelah item ke-{stage}")
    st.dataframe(snapshots[stage-1])

    if st.button("Tampilkan Solusi Optimal dari Tahap Akhir"):
        picked = traceSolution(snapshots[-1], weights, profits, capacity)
        st.write("**Barang Terpilih:**", picked)
        total_w = sum(weights[i] for i in picked)
        total_p = sum(profits[i] for i in picked)
        st.write("**Total Berat:**", total_w)
        st.write("**Total Profit:**", total_p)
