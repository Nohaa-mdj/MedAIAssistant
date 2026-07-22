import streamlit as st

from src.predict import predict_disease, symptom_columns


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

for symptom in symptom_columns:
    patient_data[symptom] = st.checkbox(
        symptom.replace("_", " ").title()
    )

# Prediction button
if st.button("Predict"):

    selected_symptoms = [
        symptom
        for symptom, selected in patient_data.items()
        if selected
    ]

    prediction, results = predict_disease(selected_symptoms)

    st.success(f"Predicted condition: {prediction}")

    st.subheader("Top 3 predictions")

    for disease, probability in results:
        st.write(f"**{disease}** — {probability:.1%}")