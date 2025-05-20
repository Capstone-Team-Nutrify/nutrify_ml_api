from ..model.model_nutrify import ml_model
from ..data.mongo_config import save_predict_log

def handle_prediction(input_makanan):
    prediction = ml_model(input_makanan)
    save_predict_log(input_makanan, prediction)
    
    return {
        "nama makanan": input_makanan,
        "prediction": prediction,
        "message": "Prediction successful and logged"
    }
