import joblib
import os

def load_models(model_paths):
    models = {}
    for path in model_paths:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model {path} tidak ditemukan.")
        models[path.split('.')[0].split('_')[-1]] = joblib.load(path)
    return models

def score_local_models(cv, models):
    score_edu = models['education'].predict([cv.get("educational_institution_name", "")])[0] * 100
    score_exp = models['experience'].predict([cv.get("experiencere_requirement", "")])[0] * 100
    score_skill = models['skill'].predict([cv.get("skills", "")])[0] * 100
    score_main = models['main'].predict([cv.get("text", "")])[0] * 100

    return {
        "Candidate": cv.get("filename", "Unknown"),
        "Education": score_edu,
        "Experience": score_exp,
        "Skill": score_skill,
        "Total": score_main
    }