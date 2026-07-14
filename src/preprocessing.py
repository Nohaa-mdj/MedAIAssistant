import pandas as pd

# Load dataset
data = pd.read_csv("data/Training.csv")

# Remove empty column
data = data.drop(columns=["Unnamed: 133"])

# Display first rows
print(data.head())

# Display dataset information
print(data.info())