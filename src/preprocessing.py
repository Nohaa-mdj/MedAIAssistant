import pandas as pd

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """
    Remove unnecessary columns.
    """
    if "Unnamed: 133" in data.columns:
        data = data.drop(columns=["Unnamed: 133"])
    return data

def dataset_report(data):
    """
    Display basic information about the dataset.
    """
    print("=" * 40)
    print("MEDAI DATASET REPORT")
    print("=" * 40)
    print(f"Number of patients : {len(data)}")
    print(f"Number of columns  : {len(data.columns)}")
    print(f"Missing values     : {data.isnull().sum().sum()}")
    print("=" * 40)

def main():
    data = load_data("data/Training.csv")
    data = clean_data(data)
    dataset_report(data)

if __name__ == "__main__":
    main()