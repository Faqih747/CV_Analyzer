from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

def summarize_cv(cv_text):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {"role": "system", "content": "Ringkas CV berikut ini dalam bahasa Indonesia, fokus pada pengalaman, keahlian, dan pencapaian utama."},
            {"role": "user", "content": cv_text}
        ]
    )
    return response.choices[0].message.content

def recommend_cv(cv_text):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {"role": "system", "content": "Kamu adalah HR profesional. Berikan rekomendasi dalam bahasa Indonesia terhadap CV ini."},
            {"role": "user", "content": cv_text}
        ]
    )
    return response.choices[0].message.content

def compare_cvs(cv_list, role):
    prompt = (
        f"Berikut ini adalah beberapa CV. Bandingkan dan tentukan CV mana yang paling cocok untuk role '{role}'. "
        "Jelaskan alasanmu dalam bahasa Indonesia:\n\n"
    )
    for i, cv in enumerate(cv_list):
        prompt += f"CV {i+1}:\n{cv['text']}\n\n"

    response = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {"role": "system", "content": "Kamu adalah HR profesional."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def score_cv_prompt(cv_text, weights):
    prompt = f"""
    Anda adalah HR profesional yang menilai CV berdasarkan kriteria berikut dengan bobot:
    Technical Skills: {weights['Technical Skills']}
    Education: {weights['Education']}
    Work Experience: {weights['Work Experience']}
    Leadership: {weights['Leadership']}
    Communication: {weights['Communication']}

    Berikan penilaian dalam format JSON seperti ini:
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
    {cv_text}
    """

    response = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {"role": "system", "content": "Kamu adalah HR profesional."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
