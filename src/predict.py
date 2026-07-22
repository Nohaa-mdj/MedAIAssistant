import joblib
import pandas as pd
from pathlib import Path


# Chemin racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "medai_model.pkl"
DATA_PATH = BASE_DIR / "data" / "Training.csv"


# Charger le modèle entraîné
model = joblib.load(MODEL_PATH)

# Charger les noms des symptômes
data = pd.read_csv(DATA_PATH)

# Supprimer la colonne vide si elle existe
if "Unnamed: 133" in data.columns:
    data = data.drop(columns=["Unnamed: 133"])

# Liste des symptômes
symptom_columns = data.drop("prognosis", axis=1).columns


def predict_disease(selected_symptoms):
    """
    Predict the most likely disease from a list of selected symptoms.
    """

    # Créer un patient vide
    patient = pd.DataFrame(
        [[0] * len(symptom_columns)],
        columns=symptom_columns
    )

    # Cocher les symptômes sélectionnés
    for symptom in selected_symptoms:
        if symptom in patient.columns:
            patient.loc[0, symptom] = 1

    # Prédiction
    prediction = model.predict(patient)[0]

    # Probabilités
    probabilities = model.predict_proba(patient)[0]

    # Les 3 maladies les plus probables
    classes = model.classes_

    results = sorted(
        zip(classes, probabilities),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    return prediction, results