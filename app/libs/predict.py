from ..model.model_nutrify import load_model_and_data, prediksi_kombinasi_makanan
from ..data.mongo_config import save_predict_log

def parse_makanan_json(data):
    """
    Mengubah input JSON menjadi list of tuple (nama_makanan, berat)
    """
    makanan_input = data.get("makanan", [])
    makanan_list = []
    for item in makanan_input:
        try:
            nama = item.get("bahan")
            berat = float(item.get("dose"))
            if nama and berat > 0:
                makanan_list.append((nama, berat))
        except (ValueError, TypeError):
            continue
    return makanan_list


def handle_prediction(input_makanan):
    # Load model and required data
    model, makanan_df, kolom_nutrisi, penyakit_cols = load_model_and_data()
    
    # Mengubah json ke tupple/list
    makanan_list = parse_makanan_json(input_makanan)
    
    # Get prediction for the input food
    prediction = prediksi_kombinasi_makanan(makanan_list, makanan_df, kolom_nutrisi, model, penyakit_cols)
    
    # Save prediction log
    # save_predict_log(input_makanan, prediction)
    
    return prediction
