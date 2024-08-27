import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def predict(model, features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return prediction[0]
