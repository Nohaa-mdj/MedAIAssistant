import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def load_data(file_path):
    """
    Load the dataset from a CSV file.
    """
    data = pd.read_csv(file_path)

    # Remove empty column if present
    if "Unnamed: 133" in data.columns:
        data = data.drop(columns=["Unnamed: 133"])

    return data


def prepare_data(data):
    """
    Separate features (X) and target (y).
    """
    X = data.drop("prognosis", axis=1)
    y = data["prognosis"]
    return X, y


def train_model(X_train, y_train):
    """
    Train a Random Forest classifier.
    """
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model accuracy.
    """
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("=" * 40)
    print("MEDAI MODEL REPORT")
    print("=" * 40)
    print(f"Model Accuracy : {accuracy:.2%}")
    print("=" * 40)

    return accuracy


def save_model(model):
    """
    Save the trained model.
    """
    os.makedirs("models", exist_ok=True)

    joblib.dump(model, "models/medai_model.pkl")

    print("✅ Model saved in models/medai_model.pkl")


def main():

    print("Loading dataset...")

    data = load_data("data/Training.csv")

    X, y = prepare_data(data)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("Training Random Forest model...")

    model = train_model(X_train, y_train)

    evaluate_model(model, X_test, y_test)

    save_model(model)


if __name__ == "__main__":
    main()