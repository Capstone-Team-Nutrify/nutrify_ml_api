import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # lokasi file ini
MODEL_PATH = os.path.join(BASE_DIR, "./nutrify_multi_rf.joblib")

model = joblib.load(MODEL_PATH)


def ml_model(input_makanan):
    arr = np.array(input_makanan).reshape(1, -1)
    return model.predict(arr).tolist()