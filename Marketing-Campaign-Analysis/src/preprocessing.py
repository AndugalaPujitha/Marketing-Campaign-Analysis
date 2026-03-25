# src/preprocessing.py

import pandas as pd


def load_data(path):
    df = pd.read_csv(path, sep=";")
    return df


def clean_data(df):
    # Ensure target column exists
    if 'y' not in df.columns:
        raise ValueError("Target column 'y' not found")

    # Handle target safely (only if it's object type)
    if df['y'].dtype == 'object':
        df['y'] = df['y'].map({'yes': 1, 'no': 0})

    # Drop missing values
    df = df.dropna()

    return df


def feature_engineering(df):
    # Age groups (only if not already created)
    if 'age_group' not in df.columns:
        df['age_group'] = pd.cut(
            df['age'],
            bins=[18, 25, 35, 50, 65, 100],
            labels=['18-25', '26-35', '36-50', '51-65', '65+']
        )

    # Contact efficiency (avoid division issues)
    if 'contact_efficiency' not in df.columns:
        df['contact_efficiency'] = df['pdays'] / (df['campaign'] + 1)

    return df


def preprocess_pipeline(path):
    df = load_data(path)
    df = clean_data(df)
    df = feature_engineering(df)

    return df