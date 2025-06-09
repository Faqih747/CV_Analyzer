from utils.feature_extraction import extract_features
from utils.model_utils import score_local_models

def score_cv_local(cv_text, models, filename="Unknown"):
    features = extract_features(cv_text)
    features["filename"] = filename
    return score_local_models(features, models)
