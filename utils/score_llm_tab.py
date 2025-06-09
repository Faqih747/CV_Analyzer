import json
from utils.openai_utils import score_cv_prompt

def score_cv_llm(cv_text, weights):
    if not cv_text.strip():
        return "CV kosong atau tidak valid."
    
    result_str = score_cv_prompt(cv_text, weights)
    try:
        return json.loads(result_str)
    except json.JSONDecodeError:
        return {"error": "Gagal mengurai hasil dari LLM."}
