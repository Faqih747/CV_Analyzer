from utils.openai_utils import summarize_cv

def generate_summary(cv_text):
    if cv_text.strip():
        return summarize_cv(cv_text)
    return "CV kosong atau tidak valid."