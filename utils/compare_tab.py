from utils.openai_utils import compare_cvs

def compare_uploaded_cvs(cv_texts, role):
    if len(cv_texts) < 2:
        return "Unggah minimal dua CV untuk dibandingkan."
    return compare_cvs(cv_texts, role)
