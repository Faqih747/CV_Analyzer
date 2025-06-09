from utils.pdf_utils import extract_text_from_pdf

def extract_single_cv(uploaded_file):
    if uploaded_file:
        return extract_text_from_pdf(uploaded_file)
    return ""
