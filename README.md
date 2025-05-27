# Knapsack 0/1 DP Explorer

Aplikasi eksplorasi Dynamic Programming untuk masalah Knapsack 0/1, menyediakan:

* **CLI** (via `main.py`) dan **Streamlit Web UI** (`app.py`)
* Visualisasi tabel DP akhir dan langkah demi langkah
* Ekstraksi solusi optimal (barang terpilih, total berat & profit)

---

## Struktur Project

```
program dinamis knapsack/
├── README.md               # Dokumentasi project
├── requirements.txt        # Daftar dependencies Python
├── knapsack.py             # Core DP & Backtracking
├── ui.py                   # CLI interface (optional)
├── main.py                 # Entry point CLI mode
├── app.py        # Streamlit Web UI
├── tests/                  # Unit tests
│   ├── test_dp.py
│   ├── test_ui.py
└── └── test_streamlit.py
```

## Instalasi

1. **Clone repository**

   ```bash
   git clone https://github.com/Rafaellie/Program-Dinamis-Knapsack.git
   cd Program-Dinamis-Knapsack
   ```
2. **Buat virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan

### Mode CLI

```bash
python main.py
```

Ikuti prompt untuk input jumlah barang, daftar berat & profit, dan kapasitas knapsack.

### Mode Streamlit

```bash
streamlit run app.py
```

Akses antarmuka web di `http://localhost:8501`.

* **Mode Final**: Tabel DP akhir & solusi optimal.
* **Step-by-Step**: Slider untuk memilih tahap dan melihat snapshot DP.

## Testing

```bash
pytest
```

## Demo

* **UI.md**: Petunjuk detail CLI & Streamlit.
* Demo singkat (<2 menit) menampilkan alur penginputan, visualisasi, dan solusi.

---
