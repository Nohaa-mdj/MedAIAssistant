import streamlit as st
import joblib
import pandas as pd


# Load trained model
model = joblib.load("models/medai_model.pkl")


# Load symptoms names
data = pd.read_csv("data/Training.csv")

if "Unnamed: 133" in data.columns:
    data = data.drop(columns=["Unnamed: 133"])

symptoms = data.drop("prognosis", axis=1).columns


# Page configuration
st.set_page_config(
    page_title="MedAI Assist",
    page_icon="🩺"
)


st.title("🩺 MedAI Assist")

st.write(
    "AI clinical decision support prototype. "
    "This tool does not replace medical professionals."
)


st.header("Select symptoms")


# Create symptom checkboxes
patient_data = {}

for symptom in symptoms:
    patient_data[symptom] = st.checkbox(symptom)


# Prediction button
if st.button("Predict"):

    # Convert symptoms to numbers
    input_data = pd.DataFrame(
        [patient_data]
    )

    # Convert True/False to 1/0
    input_data = input_data.astype(int)


    prediction = model.predict(input_data)


    st.success(
        f"Predicted condition: {prediction[0]}"
    )