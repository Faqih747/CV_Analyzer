from utils.openai_utils import recommend_cv

def generate_recommendation(cv_text):
    if cv_text.strip():
        return recommend_cv(cv_text)
    return "CV kosong atau tidak valid."
