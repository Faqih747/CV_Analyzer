# 📄 CV Analyzer AI

Aplikasi **CV Analyzer AI** berbasis Streamlit yang memungkinkan pengguna mengunggah dan menganalisis banyak CV dalam bentuk PDF, memberikan ringkasan, rekomendasi, perbandingan, dan skoring menggunakan LLM (Groq/OpenAI) maupun model machine learning lokal (`.pkl`).

---

## 🚀 Fitur Utama

- 📤 **Upload CV**: Unggah banyak file PDF sekaligus  
- 🔍 **Ringkasan CV**: Gunakan LLM untuk merangkum isi CV  
- 🤖 **Rekomendasi AI**: LLM memberi saran peningkatan CV  
- ⚖️ **Perbandingan CV**: Bandingkan banyak CV berdasarkan role  
- 📊 **Skoring LLM**: Penilaian CV berdasarkan kriteria HR  
- 🧠 **Skoring ML Lokal**: Penilaian CV via model lokal `.pkl`

---

## 🗂️ Struktur Proyek

```
CV_Analyzer/
├── app.py
├── requirements.txt
├── README.md
├── .env                      # API Key untuk Groq/OpenAI
├── models/                   # Model ML lokal (jika ada)
│   ├── model_education.pkl
│   ├── model_experience.pkl
│   ├── model_skill.pkl
│   └── model_main.pkl
├── utils/                    # Modularisasi logika per tab
│   ├── extract_tab.py        # Tab Upload CV
│   ├── summarize_tab.py      # Tab Ringkasan CV
│   ├── recommend_tab.py      # Tab Rekomendasi AI
│   ├── compare_tab.py        # Tab Perbandingan CV
│   ├── score_llm_tab.py      # Tab Skoring LLM
│   ├── score_local_tab.py    # Tab Skoring ML Lokal
│   ├── pdf_utils.py          # Fungsi bantu ekstraksi PDF
│   └── model_utils.py        # Load dan prediksi model ML
```

---

## ⚙️ Cara Menjalankan

1. **Clone repositori**
   ```bash
   git clone https://github.com/Faqih747/CV_Analyzer.git
   cd CV_Analyzer
   ```

2. **Install dependensi**
   ```bash
   pip install -r requirements.txt
   ```

3. **Buat file `.env`**
   ```env
   GROQ_API_KEY=sk-...
   ```

4. **Jalankan aplikasi**
   ```bash
   streamlit run app.py
   ```

---

## 🧩 Modul Per Tab

| File `utils/`           | Fungsi                                                                 |
|------------------------|------------------------------------------------------------------------|
| `extract_tab.py`       | Mengunggah dan membaca isi PDF                                          |
| `summarize_tab.py`     | Merangkum CV menggunakan LLM                                            |
| `recommend_tab.py`     | Memberikan saran per CV                                                 |
| `compare_tab.py`       | Membandingkan banyak CV terhadap role tertentu                         |
| `score_llm_tab.py`     | Memberi skor CV berdasarkan bobot kriteria HR (LLM via JSON)           |
| `score_local_tab.py`   | Memberi skor CV menggunakan model Machine Learning lokal (`.pkl`)      |
| `pdf_utils.py`         | Fungsi ekstraksi teks dari PDF                                         |
| `model_utils.py`       | Load model `.pkl` dan lakukan prediksi                                 |

---

## 📦 requirements.txt

```txt
streamlit
openai
pdfplumber
pandas
joblib
python-dotenv
matplotlib
scikit-learn
```

---

## 🛡️ Keamanan

- Simpan API Key di `.env`, **jangan commit `.env` ke publik**
- Jangan upload model `.pkl` ke GitHub publik tanpa izin


