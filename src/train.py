import joblib
from sklearn.ensemble import RandomForestRegressor

def train_and_save(X, y, model_path='models/random_forest_model.pkl'):
    """
    Trains the Champion Model with a fixed Random State for consistency.
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X, y)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
    return model
