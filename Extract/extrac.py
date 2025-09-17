import pandas as pd
import os

def extract_data():
    file_path = os.path.join(os.path.dirname(__file__), "archive", "F1Drivers_Dataset.csv")
    df = pd.read_csv(file_path)
    return df
