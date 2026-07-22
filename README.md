# 🩺 MedAI Assist

> An explainable machine learning prototype for healthcare decision support

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Machine Learning](https://img.shields.io/badge/AI-Machine%20Learning-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Summary

MedAI Assist is an explainable AI prototype for clinical decision support.

The project demonstrates how machine learning can assist healthcare professionals by analyzing symptom patterns and predicting possible medical conditions.

The goal is not to replace medical expertise, but to explore how AI systems can support decision-making through data-driven recommendations.

---

# 🌍 Background

Healthcare professionals process a large amount of information when evaluating patients.

AI-assisted tools could help organize medical data and highlight possible conditions, especially in situations where rapid analysis is required.

Common challenges include:

- information overload
- limited time for decision-making
- complex symptom combinations
- unequal access to medical expertise

MedAI Assist explores how machine learning can contribute to healthcare applications while considering important ethical aspects such as transparency, fairness and human supervision.

This project was developed as part of the **Building AI course by Reaktor and the University of Helsinki**.

---

# 🚀 How is it used?

Users select symptoms through an interactive Streamlit interface.

The system then:

1. Converts symptoms into numerical features
2. Processes the input data
3. Applies a trained machine learning model
4. Predicts a possible condition

Example:

Selected symptoms:

- Fever
- Cough
- Chest pain
- Shortness of breath

Prediction example:

| Condition                   | Confidence |
| --------------------------- | ---------- |
| Pneumonia                   | 87%        |
| Influenza                   | 8%         |
| Other respiratory condition | 5%         |

> This output is an AI prediction and not a medical diagnosis.

---

# 🤖 AI Methods

## Machine Learning

The current prototype uses:

- Random Forest Classifier
- Scikit-Learn

The model was trained on a labeled symptom dataset to identify patterns between symptoms and possible conditions.

## Explainability

Explainability is an important goal of this project.

Future improvements could include:

- SHAP explanations
- feature importance visualization
- model confidence analysis

These techniques would help users better understand how predictions are generated.

---

# 📊 Dataset

The prototype uses a medical symptom dataset containing:

- symptom features
- disease labels
- training and testing samples

The dataset does not contain personal patient information.

Future versions could explore validated medical datasets such as:

- MIMIC-IV
- UCI Machine Learning Repository
- public healthcare datasets

---

# 👥 Target Users

Potential users:

- Healthcare professionals
- Medical students
- Researchers

Possible future environments:

- hospitals
- clinics
- educational platforms

---

# ⚠ Limitations & Ethics

MedAI Assist is a research and educational prototype.

It is **not designed to diagnose patients or replace healthcare professionals**.

Current limitations include:

- dataset quality and bias
- limited clinical context
- incomplete patient information
- lack of real-world validation

Important considerations:

- patient privacy
- transparency
- fairness
- human decision-making

---

# 🔮 Future Improvements

Possible future developments:

- SHAP-based explanations
- Natural Language Processing for symptom extraction
- Medical image analysis
- Multilingual support
- Integration with healthcare systems
- Large Language Models for medical assistance

---

# 🏗 Architecture

```

User

↓

Streamlit Interface

↓

Data Processing

↓

Machine Learning Model

↓

Prediction Output

↓

Future Explainability Layer

```

---

# 🛠 Technologies

| Component            | Technology       |
| -------------------- | ---------------- |
| Programming Language | Python           |
| Machine Learning     | Scikit-Learn     |
| Interface            | Streamlit        |
| Data Processing      | Pandas           |
| Model Serialization  | Joblib           |
| Data Analysis        | Jupyter Notebook |

---

# 🤝 Acknowledgments

This project was created as part of the **Building AI course by Reaktor and the University of Helsinki**.

Resources and inspiration:

- Scikit-Learn
- Kaggle datasets
- UCI Machine Learning Repository
- World Health Organization resources

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/Nohaa-mdj/MedAIAssistant.git

cd MedAIAssistant

pip install -r requirements.txt

python3 -m streamlit run app/streamlit_app.py
```

---

# 📄 License

MIT License

```

```
