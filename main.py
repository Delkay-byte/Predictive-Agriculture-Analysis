import pandas as pd
import joblib
import os
import sys
import numpy as np
from src.preprocessing import clean_data
from src.train import train_and_save
from src.eda import plot_importance
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def run_pipeline(data_path):
    print("🚀 Starting The Outliers: Crop Yield Prediction Pipeline...")

    # PATH CHECK
    if not os.path.exists(data_path):
        print(f"❌ ERROR: Data file not found at {data_path}")
        return

    # LOAD DATA
    df = pd.read_csv(data_path)
    print(f"📦 Data loaded: {df.shape}")

    # PREPROCESSING (The 99% Rule)
    df_clean = clean_data(df)
    print("🧹 Data cleaned and outliers handled (99th percentile cap).")

    # FEATURE SPLITTING
    X = df_clean.drop('hg/ha_yield', axis=1)
    y = df_clean['hg/ha_yield']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # ENCODING
    cat_cols = [c for c in X.columns if c.lower() in ['area', 'item']]
    num_cols = [c for c in X.columns if any(word in c.lower() for word in ['rain', 'pesticide', 'temp'])]

    ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    X_train_cat = ohe.fit_transform(X_train[cat_cols])
    X_train_final = np.hstack([X_train_cat, X_train[num_cols].values])

    # EXTERNAL MODEL CHECK & TRAINING
    model_path = 'Models/random_forest_model.pkl'
    if os.path.exists(model_path):
        print("✅ Champion Model detected in /models. Skipping training...")
        model = joblib.load(model_path)
    else:
        print("🧠 Champion Model not found. Training a new Random Forest...")
        if not os.path.exists('Models'): os.makedirs('Models')
        model = train_and_save(X_train_final, y_train, model_path=model_path)
        # Also save the preprocessor (OHE) for future use
        joblib.dump(ohe, 'Models/preprocessor.pkl')
        print("💾 Preprocessor saved to Models/preprocessor.pkl")

    # GENERATE IMPORTANCE DATA & VISUALIZE
    ohe_cat_names = ohe.get_feature_names_out(cat_cols)
    all_feature_names = list(ohe_cat_names) + num_cols

    importance_df = pd.DataFrame({
        'Feature': all_feature_names,
        'Importance': model.feature_importances_
    }).sort_values(by='Importance', ascending=False)

    if not os.path.exists('Reports'): os.makedirs('Reports')
    plot_importance(importance_df, save_path='Reports/final_importance_plot.png')
    print("📊 Importance chart saved to reports/final_importance_plot.png")

    print("\n✅ Pipeline Complete! Your model is ready for the Outliers project.")

if __name__ == "__main__":
    # Pointing to your actual master file as requested
    run_pipeline('Data/master_clean_yield_data.csv')
