from ..model.model_nutrify import load_model_and_data, prediksi_status_makanan
from ..data.mongo_config import save_predict_log

def handle_prediction(input_makanan):
    # Load model and required data
    model, makanan_df, kolom_nutrisi, penyakit_cols = load_model_and_data()
    
    # Get prediction for the input food
    prediction = prediksi_status_makanan(input_makanan, makanan_df, kolom_nutrisi, model, penyakit_cols)
    
    # Save prediction log
    save_predict_log(input_makanan, prediction)
    
    return {
        "nama_makanan": input_makanan,
        "prediction": prediction,
        "message": "Prediction successful and logged"
    }
