# 📄 CV Analyzer AI

Aplikasi **CV Analyzer AI** berbasis Streamlit yang memungkinkan pengguna mengunggah dan menganalisis banyak CV dalam bentuk PDF, memberikan ringkasan, rekomendasi, perbandingan, dan skoring menggunakan LLM (Groq/OpenAI) maupun model machine learning lokal (`.pkl`).

---

## 🚀 Fitur Utama

- 📤 **Upload CV**: Unggah banyak file PDF sekaligus  
- 🔍 **Ringkasan CV**: Gunakan LLM untuk merangkum isi CV  
- 🤖 **Rekomendasi AI**: LLM memberi saran peningkatan CV  
- ⚖️ **Perbandingan CV**: Bandingkan banyak CV berdasarkan role  
- 📊 **Skoring LLM**: Penilaian CV berdasarkan kriteria HR  
- 🧠 **Skoring ML Lokal**: Penilaian CV via model `.pkl`  
- 🧪 **Training Model Lokal**: Melatih model sendiri dengan `resume_data.csv`

---

## 🗂️ Struktur Proyek

```
CV_Analyzer/
├── .env
├── requirements.txt
├── main.app/
│   └── app.py
├── data/
│   ├── CV Arbia.pdf
│   └── CV Raya.pdf
├── models/
│   ├── model_education.pkl
│   ├── model_experience.pkl
│   ├── model_main.pkl
│   └── model_skill.pkl
├── training/
│   ├── resume_data.csv
│   └── train.py
├── utils/
│   ├── compare_tab.py        # Tab Perbandingan CV
│   ├── extract_tab.py        # Tab Upload CV
│   ├── feature_extraction.py # Ekstraksi fitur untuk model ML
│   ├── model_utils.py        # Load dan prediksi model lokal
│   ├── openai_utils.py       # Koneksi ke LLM via Groq/OpenAI
│   ├── pdf_utils.py          # Ekstraksi teks PDF
│   ├── recommend_tab.py      # Tab Rekomendasi AI
│   ├── score_llm_tab.py      # Tab Skoring LLM
│   ├── score_local_tab.py    # Tab Skoring ML Lokal
│   └── summarize_tab.py      # Tab Ringkasan CV
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
   streamlit run main.app/app.py
   ```

---

## 🧠 Training Model Lokal

Jika ingin melatih model dari awal:

```bash
python training/train.py
```

Data pelatihan disimpan di `training/resume_data.csv` dan model hasil training akan disimpan di folder `models/`.

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

## 📸 Cara Penggunaan

1. Masukkan beberapa File CV dengan format PDF
   ![image](https://github.com/user-attachments/assets/96b5cf69-42ac-4317-abc7-5ba8921c2ee1)
2. Pada Tab Ringkasan, pengguna dapat melihat ringkasan CV dari file yang di upload
   ![image](https://github.com/user-attachments/assets/207c8218-7208-4fa3-8f68-d337a03363cb)
3. Pada Tab Rekomendasi, pengguna dapat melihat rekomendasi perbaikan dari file yang di upload
   ![image](https://github.com/user-attachments/assets/77437659-67fc-45ac-9fb3-54d42a836819)
4. Pada Tab Perbandingan, pengguna dapat membandingkan CV berdasarkan posisi yang diinginkan pengguna
   ![image](https://github.com/user-attachments/assets/91cfbfa0-2fe3-423a-bd9c-773914a32782)
5. Pada Tab Skoring CV, pengguna dapat menentukan faktor mana yang paling dicari sehingga dapat terpilih kandidat yang diinginkan dan diurutkan berdasarkan skor 
   ![image](https://github.com/user-attachments/assets/38fce940-def9-4248-baa4-2ac1c54713cf)
   ![image](https://github.com/user-attachments/assets/3272a60c-35a6-442e-9449-97c63f21b06e)
6. Pada Tab Skoring ML (Model Lokal), pengguna dapat melihat skoring berdasarkan database yang telah dilatih dan hasilnya konsisten
   ![image](https://github.com/user-attachments/assets/c57b42b5-1c30-47ba-9ca5-43fe843255e0)

---

## 📍 Lisensi

© 2025 CV Analyzer

Dikembangkan oleh Abdullah Faqih bersama Tim AI Enginer PT Global Data Inspirasi

Hubungi Tim kami:

Linkedin : [https://www.linkedin.com/in/abdullah-faqih-8127b5245/]




