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
    
    """Mengkonversi prediksi ke status dan badge"""
    status_map = {
        0: {"status": "Konsumsi Wajar", "badge": "success"},
        1: {"status": "Netral", "badge": "secondary"},
        2: {"status": "Waspada", "badge": "danger"}
    }
    
    return status_map.get(prediction, {"status": "Tidak diketahui", "badge": "secondary"})


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
            "penyakit": penyakit,
            "status": status_info["status"],
            "badge": status_info["badge"]
        })
    
    #   
    rounded_nutrisi = {k: round(v, 2) for k, v in total_nutrisi.items()}
    
    #    
    formatted_makanan = [
        {
            "bahan": nama,
            "dose": int(berat) if float(berat).is_integer() else round(berat, 2)
        }
        for nama, berat in valid_makanan
    ]
    
    return {
        "makanan": formatted_makanan,
        "total_nutrisi": rounded_nutrisi,
        "disease_rate": disease_rate
    }
