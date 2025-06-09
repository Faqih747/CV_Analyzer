from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('resume_data.csv')

if 'matched_score' in df.columns:
    df.dropna(subset=['matched_score'], inplace=True)

    df.fillna('', inplace=True)

    y = df['matched_score']

    X_edu = df['educational_institution_name']
    pipeline_edu = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=500)),
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    pipeline_edu.fit(X_edu, y)
    joblib.dump(pipeline_edu, 'model_education.pkl')

    X_exp = df['experiencere_requirement']
    pipeline_exp = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=500)),
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    pipeline_exp.fit(X_exp, y)
    joblib.dump(pipeline_exp, 'model_experience.pkl')

    X_skill = df['skills']
    pipeline_skill = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=500)),
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    pipeline_skill.fit(X_skill, y)
    joblib.dump(pipeline_skill, 'model_skill.pkl')

    df['Resume'] = df['career_objective'] + ' ' + df['skills'] + ' ' + df['responsibilities']
    X_resume = df['Resume']
    pipeline_main = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=1000)),
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    pipeline_main.fit(X_resume, y)
    joblib.dump(pipeline_main, 'model_main.pkl')

else:
    print("Kolom 'matched_score' tidak ditemukan dalam dataset. Periksa nama kolom dan file CSV.")
