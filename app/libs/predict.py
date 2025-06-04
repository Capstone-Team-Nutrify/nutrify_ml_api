from ..model.model_nutrify import load_model_and_data, prediksi_kombinasi_makanan
from ..data.mongo_config import save_predict_log

def translate_keys_to_indonesian(data):
    """
    Mengubah key 'food' menjadi 'makanan', dan 'ingredient' menjadi 'bahan'
    agar cocok dengan format yang dikenali model.
    """
    if "food" in data:
        makanan_baru = []
        for item in data["food"]:
            bahan = item.get("ingredient")
            takaran = item.get("dose")
            if bahan is not None and takaran is not None:
                makanan_baru.append({
                    "bahan": bahan,
                    "dose": takaran
                })
        return {
            "makanan": makanan_baru
        }
    return data

def translate_nutrition_keys_to_english(nutrition_data):
    """
    Translate nutrition keys from Indonesian to English.

    Parameters:
    nutrition_data (dict): Dictionary with Indonesian nutrition names.

    Returns:
    dict: Dictionary with English nutrition names.
    """
    translation_map = {
        "gula": "sugar",
        "serat": "fiber",
        "protein": "protein",
        "lemak": "fat",
        "karbohidrat": "carbohydrate",
        "vitamin_A": "vitamin_A",
        "vitamin_C": "vitamin_C",
        "zat_besi": "iron",
        "kalsium": "calcium",
        "natrium": "sodium",
        "magnesium": "magnesium",
        "kolesterol": "cholesterol",
        "kalori": "calories",
        "fosfor": "phosphorus",
        "kalium": "potassium",
        "zinc": "zinc",
        "air": "water",
        "vitamin_B1": "vitamin_B1",
        "vitamin_B11": "vitamin_B11",
        "vitamin_B12": "vitamin_B12",
        "vitamin_B2": "vitamin_B2",
        "vitamin_B3": "vitamin_B3",
        "vitamin_B5": "vitamin_B5",
        "vitamin_B6": "vitamin_B6",
        "vitamin_D": "vitamin_D",
        "vitamin_E": "vitamin_E",
        "vitamin_K": "vitamin_K"
    }

    translated = {}

    for key, value in nutrition_data.items():
        english_key = translation_map.get(key, key)  # default: use original if not found
        translated[english_key] = value

    return translated



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
    # save_predict_log(prediction)
    
    return prediction
