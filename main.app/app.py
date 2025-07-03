import os
import joblib
import streamlit as st
import pdfplumber
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)


def extract_features(cv_text):
    return {
        "text": cv_text,
        "educational_institution_name": "",
        "skills": "",
        "experiencere_requirement": ""
    }

st.set_page_config(page_title="CV Analyzer AI", layout="wide")
st.title("📄 CV Analyzer AI")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📤 Upload CV", "🔍 Ringkasan", "🤖 Rekomendasi",
    "⚖️ Perbandingan", "📊 Skoring CV", "🧠 Skoring ML (Model Lokal)"
])

# Tab 1
with tab1:
    st.header("Upload Beberapa CV (PDF) 📂")
    uploaded_files = st.file_uploader("Upload beberapa file PDF di sini", type=["pdf"], accept_multiple_files=True)
    if uploaded_files:
        st.session_state["cv_texts"] = []
        for file in uploaded_files:
            with pdfplumber.open(file) as pdf:
                text = "".join([page.extract_text() or "" for page in pdf.pages])
                features = extract_features(text)
                st.session_state["cv_texts"].append({"filename": file.name, **features})
        st.success(f"✅ {len(uploaded_files)} CV berhasil diproses!")

# Tab 2
with tab2:
    st.header("Ringkasan CV 📝")
    if "cv_texts" in st.session_state:
        for cv in st.session_state["cv_texts"]:
            with st.expander(f"{cv['filename']}"):
                with st.spinner("Meringkas..."):
                    response = client.chat.completions.create(
                        model="meta-llama/llama-4-maverick-17b-128e-instruct",
                        messages=[
                            {"role": "system", "content": "Ringkas CV berikut ini dalam bahasa Indonesia, fokus pada pengalaman, keahlian, dan pencapaian utama."},
                            {"role": "user", "content": cv["text"]}
                        ]
                    )
                    st.write(response.choices[0].message.content)
    else:
        st.warning("⬅️ Silakan upload CV terlebih dahulu.")

# Tab 3
with tab3:
    st.header("Rekomendasi AI 🤖")
    if "cv_texts" in st.session_state:
        for cv in st.session_state["cv_texts"]:
            if st.button(f"Dapatkan Rekomendasi untuk {cv['filename']}"):
                with st.spinner("AI sedang menganalisis..."):
                    response = client.chat.completions.create(
                        model="meta-llama/llama-4-maverick-17b-128e-instruct",
                        messages=[
                            {"role": "system", "content": "Kamu adalah HR profesional. Berikan rekomendasi dalam bahasa Indonesia terhadap CV ini."},
                            {"role": "user", "content": cv["text"]}
                        ]
                    )
                    st.success("✅ Rekomendasi:")
                    st.write(response.choices[0].message.content)
    else:
        st.warning("⬅️ Silakan upload CV terlebih dahulu.")

# Tab 4
with tab4:
    st.header("Perbandingan CV berdasarkan Role ⚖️")
    if "cv_texts" in st.session_state:
        role = st.text_input("Masukkan posisi atau role pekerjaan (misal: Data Analyst)")
        if st.button("Bandingkan CV"):
            with st.spinner("AI sedang membandingkan..."):
                cv_list_text = "\n\n".join([f"CV {i+1} ({cv['filename']}):\n{cv['text']}" for i, cv in enumerate(st.session_state["cv_texts"])])
                prompt = (
                    f"Berikut ini adalah beberapa CV. Bandingkan dan tentukan CV mana yang paling cocok untuk role '{role}'. "
                    "Jelaskan alasanmu dalam bahasa Indonesia:\n\n" + cv_list_text
                )
                response = client.chat.completions.create(
                    model="meta-llama/llama-4-maverick-17b-128e-instruct",
                    messages=[
                        {"role": "system", "content": "Kamu adalah HR profesional yang diminta membandingkan beberapa CV."},
                        {"role": "user", "content": prompt}
                    ]
                )
                st.success("✅ Hasil Perbandingan:")
                st.write(response.choices[0].message.content)
    else:
        st.warning("⬅️ Silakan upload CV terlebih dahulu.")

# Tab 5
def score_single_cv(cv, weights):
    prompt = f"""
    Anda adalah HR profesional yang menilai CV berdasarkan kriteria berikut dengan bobot:
    Technical Skills: {weights['Technical Skills']}
    Education: {weights['Education']}
    Work Experience: {weights['Work Experience']}
    Leadership: {weights['Leadership']}
    Communication: {weights['Communication']}

    Berikan penilaian dalam format JSON:
    {{
      "Candidate": "<nama kandidat>",
      "Technical Skills": 4,
      "Education": 3,
      "Work Experience": 2,
      "Leadership": 3,
      "Communication": 3,
      "total_weighted_score": 48,
      "max_possible_score": 100,
      "percentage_score": 48.0,
      "notes": "Tuliskan catatan singkat tentang kandidat."
    }}

    Gunakan angka bulat dan desimal biasa tanpa rumus matematika dalam JSON.

    CV:
    {cv['text']}
    """
    response = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {"role": "system", "content": "Kamu adalah HR profesional."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )
    import json
    result = json.loads(response.choices[0].message.content)
    result["Candidate"] = cv.get("filename", "Unknown")
    return result

with tab5:
    st.header("🏆 Candidate Ranking")
    if "cv_texts" in st.session_state:
        col1, col2, col3 = st.columns(3)
        with col1:
            tech = st.slider("Technical Skills", 1, 10, 8)
            exp = st.slider("Work Experience", 1, 10, 9)
        with col2:
            edu = st.slider("Education", 1, 10, 4)
            lead = st.slider("Leadership", 1, 10, 7)
        with col3:
            comm = st.slider("Communication", 1, 10, 4)

        weights = {
            "Technical Skills": tech,
            "Education": edu,
            "Work Experience": exp,
            "Leadership": lead,
            "Communication": comm
        }

        if st.button("💯 Hitung & Rank Kandidat"):
            with st.spinner("Mengevaluasi..."):
                results = []
                for cv in st.session_state["cv_texts"]:
                    try:
                        results.append(score_single_cv(cv, weights))
                    except Exception as e:
                        st.error(f"Gagal memproses {cv['filename']}: {e}")
                if results:
                    df = pd.DataFrame(results)
                    df = df.sort_values("percentage_score", ascending=False).reset_index(drop=True)
                    df["Rank"] = df.index + 1
                    df["Total Score"] = df["total_weighted_score"].astype(str) + "/" + df["max_possible_score"].astype(str)
                    df["Percentage"] = df["percentage_score"].astype(str) + "%"
                    st.dataframe(df, use_container_width=True)
                    csv = df.to_csv(index=False).encode("utf-8")
                    st.download_button("📥 Download Ranking (CSV)", data=csv, file_name="ranking.csv", mime="text/csv")
    else:
        st.warning("⬅️ Silakan upload CV terlebih dahulu.")

# Tab 6
with tab6:
    st.header("🧠 Skoring CV dengan Model ML Lokal")
    model_dir = "models"
    required_files = ["model_education.pkl", "model_experience.pkl", "model_skill.pkl", "model_main.pkl"]
    missing = [f for f in required_files if not os.path.exists(os.path.join(model_dir, f))]
    if missing:
        st.error("❌ Model belum lengkap. Harap letakkan model di folder 'models/'.")
    elif "cv_texts" in st.session_state:
        model_edu = joblib.load(os.path.join(model_dir, "model_education.pkl"))
        model_exp = joblib.load(os.path.join(model_dir, "model_experience.pkl"))
        model_skill = joblib.load(os.path.join(model_dir, "model_skill.pkl"))
        model_main = joblib.load(os.path.join(model_dir, "model_main.pkl"))

        scores = []
        for cv in st.session_state["cv_texts"]:
            try:
                edu_score = model_edu.predict([cv.get("educational_institution_name", "")])[0] * 100
                exp_score = model_exp.predict([cv.get("experiencere_requirement", "")])[0] * 100
                skill_score = model_skill.predict([cv.get("skills", "")])[0] * 100
                main_score = model_main.predict([cv.get("text", "")])[0] * 100

                scores.append({
                    "Candidate": cv.get("filename", "Unknown"),
                    "Education": edu_score,
                    "Experience": exp_score,
                    "Skill": skill_score,
                    "Total": main_score
                })
            except Exception as e:
                st.error(f"Gagal prediksi untuk {cv.get('filename', 'Unknown')}: {e}")
        df = pd.DataFrame(scores).sort_values("Total", ascending=False).reset_index(drop=True)
        df.index += 1
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("⬅ Silakan upload CV terlebih dahulu.")
