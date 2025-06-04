import pandas as pd
import numpy as np
import tensorflow as tf
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # lokasi file ini
MODEL_PATH = os.path.join(BASE_DIR, "./nutrify_multi_model.h5")
CSV_PATH = os.path.join(BASE_DIR, "../data/makanan.csv")

def load_model_and_data():
    model = tf.keras.models.load_model(MODEL_PATH)
    makanan_df = pd.read_csv(CSV_PATH)

    # Sesuaikan dengan kolom nutrisi aktual
    kolom_nutrisi = [
        "gula", "serat", "protein", "lemak", "karbohidrat", "vitamin_A", "vitamin_C",
        "zat_besi", "kalsium", "natrium", "magnesium", "kolesterol", "kalori", "fosfor",
        "kalium", "zinc", "air", "vitamin_B1", "vitamin_B11", "vitamin_B12", "vitamin_B2",
        "vitamin_B3", "vitamin_B5", "vitamin_B6", "vitamin_D", "vitamin_E", "vitamin_K"
    ]
    
    # Sesuaikan dengan kolom penyakit hasil output model
    penyakit_cols = [
        "Influenza", "Liver", "Diabetes", "Anemia", "Diare", "Batu_Ginjal", "Asma",
        "Asam_Lambung", "Serangan_Jantung", "Asam_Urat", "Radang_Paru_paru", "Jerawat",
        "Hepatitis", "Wasir", "Sinusitis", "Kolesterol", "Usus_Buntu", "Tifus",
        "Osteoporosis", "Malaria", "Alergi_Dingin", "Alergi_Kacang", "Alergi_Seafood",
        "Alergi_Susu", "Alergi_Telur_Ayam", "Alergi_Buah_Beri"
    ]

    return model, makanan_df, kolom_nutrisi, penyakit_cols

def get_nutrition_values(nama_makanan, berat, df, fitur_cols):
    """Mendapatkan nilai nutrisi untuk makanan tertentu"""
    rows = df[df["makanan"].str.lower() == nama_makanan.lower()]
    
    if rows.empty:
        rows = df[df["makanan"].str.lower().str.contains(nama_makanan.lower())]
        
    if rows.empty:
        return None
    
    # Ambil nilai nutrisi dan sesuaikan dengan berat
    nutrisi = rows.iloc[0][fitur_cols].values.astype("float32")
    return nutrisi * (berat / 100.0)

def get_disease_status(prediction):
    
    """Mengkonversi prediksi ke status dan level"""
    status_map = {
        0: {"status": "Normal Consumption", "level": "normal"},
        1: {"status": "Neutral", "level": "medium"},
        2: {"status": "Warning", "level": "high"}
    }
    
    return status_map.get(prediction, {"status": "Unknown", "level": "unknown"})

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


def prediksi_kombinasi_makanan(makanan_list, df, fitur_cols, model, label_cols):
    """
    Memprediksi status kombinasi makanan
    
    Args:
        makanan_list (list): List of tuples (nama_makanan, berat)
        df (DataFrame): Database makanan
        fitur_cols (list): List kolom nutrisi
        model: Model yang sudah dilatih
        label_cols (list): List kolom penyakit
    
    Returns:
        list: Hasil prediksi untuk kombinasi makanan
    """
    
    if not isinstance(makanan_list, list):
        return []

    # Hitung total nutrisi
    total_nutrisi = {nutrisi: 0.0 for nutrisi in fitur_cols}
    valid_makanan = []
    
    for makanan, berat in makanan_list:
        try:
            berat = float(berat)
            
            if berat <= 0:
                continue
                
            nutrisi = get_nutrition_values(makanan, berat, df, fitur_cols)
            
            if nutrisi is not None:
                for i, nutrisi_name in enumerate(fitur_cols):
                    total_nutrisi[nutrisi_name] += nutrisi[i]
                valid_makanan.append((makanan, berat))
                
        except (ValueError, TypeError):
            continue
    
    if not valid_makanan:
        return []

    # Prediksi penyakit berdasarkan total nutrisi
    total_nutrisi_array = np.array([total_nutrisi[nutrisi] for nutrisi in fitur_cols])
    preds = model.predict(total_nutrisi_array.reshape(1, -1))
    
    # Format hasil prediksi penyakit
    disease_rate = []
    
    for i, penyakit in enumerate(label_cols):
        predicted_index = np.argmax(preds[i][0])
        status_info = get_disease_status(predicted_index)
        disease_rate.append({
            "disease": penyakit,
            "status": status_info["status"],
            "level": status_info["level"]
        })
    
    # Membulatkan nilai nutrisi ke dua angka di belakang koma
    rounded_nutrisi = {k: round(v, 2) for k, v in total_nutrisi.items()}
    
    # Menerjemahkan key (nama nutrisi) dari bahasa Indonesia ke bahasa Inggris
    rounded_nutrisi_translate = translate_nutrition_keys_to_english(rounded_nutrisi)
    
    # Memformat daftar bahan makanan yang valid, menyertakan nama bahan dan dosisnya
    formatted_makanan = [
        {
            "ingredient": nama,
            "dose": int(berat) if float(berat).is_integer() else round(berat, 2)
        }
        for nama, berat in valid_makanan
    ]
    
    return {
        "food": formatted_makanan,
        "total_nutrition": rounded_nutrisi_translate,
        "disease_rate": disease_rate
    }
