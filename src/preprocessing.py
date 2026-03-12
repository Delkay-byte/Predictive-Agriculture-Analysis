import pandas as pd
import numpy as np

def clean_data(df):
    """
    Handles deduplication and Winsorization (The 99% Rule).
    """
    # Remove duplicates to get to our 25,932 unique records (before expansion)
    df = df.drop_duplicates()

    # Winsorization: Cap yield at the 99th percentile
    q = df['hg/ha_yield'].quantile(0.99)
    df['hg/ha_yield'] = np.where(df['hg/ha_yield'] > q, q, df['hg/ha_yield'])

    return df

def feature_engineering(df):
    """
    Keyword-based column selection to prevent KeyErrors.
    """
    rain_col = [c for c in df.columns if 'rain' in c.lower()][0]
    pest_col = [c for c in df.columns if 'pesticide' in c.lower()][0]
    temp_col = [c for c in df.columns if 'temp' in c.lower()][0]
    return df[[rain_col, pest_col, temp_col]]
