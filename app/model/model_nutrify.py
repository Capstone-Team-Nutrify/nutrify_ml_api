# import joblib
# import numpy as np
# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # lokasi file ini
# MODEL_PATH = os.path.join(BASE_DIR, "./nutrify_multi_rf.joblib")

# model = joblib.load(MODEL_PATH)


# def ml_model(input_makanan):
#     arr = np.array(input_makanan).reshape(1, -1)
#     return model.predict(arr).tolist()


import pandas as pd
import numpy as np
import tensorflow as tf
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # lokasi file ini
MODEL_PATH = os.path.join(BASE_DIR, "./model_mlp.h5")
CSV_PATH = os.path.join(BASE_DIR, "../data/makanan.csv")

def load_model_and_data():
    model = tf.keras.models.load_model(MODEL_PATH)
    makanan_df = pd.read_csv(CSV_PATH)

    # Sesuaikan dengan kolom nutrisi aktual
    kolom_nutrisi = [
        "gula", "serat", "protein", "lemak", "karbohidrat", "vitamin_a", "vitamin_c",
        "zat_besi", "kalsium", "natrium", "magnesium", "kolesterol", "kalori", "fosfor",
        "kalium", "zinc", "air", "vitamin_b1", "vitamin_b11", "vitamin_b12", "vitamin_b2",
        "vitamin_b3", "vitamin_b5", "vitamin_b6", "vitamin_d", "vitamin_e", "vitamin_k"
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

def prediksi_status_makanan(nama_makanan, df, fitur_cols, model, label_cols):
    # Coba cari makanan dengan exact match
    rows = df[df["makanan"].str.lower() == nama_makanan.lower()]
    
    # Jika tidak ditemukan, coba cari dengan partial match
    if rows.empty:
        print("error ke 1")
        rows = df[df["makanan"].str.lower().str.contains(nama_makanan.lower())]
    
    # Jika masih tidak ditemukan, kembalikan error
    if rows.empty:
        print("error ke 2")
        return {
            "error": True,
            "message": f"Makanan '{nama_makanan}' tidak ditemukan dalam database",
            "predictions": {col: None for col in label_cols}
        }

    # Ambil baris pertama jika ada multiple matches
    baris = rows.iloc[0][fitur_cols].values.astype("float32")
    preds = model.predict(baris.reshape(1, -1))

    hasil = {}
    for i, label in enumerate(label_cols):
        predicted_index = np.argmax(preds[i][0])
        label_map = {0: "Konsumsi Wajar", 1: "Netral", 2: "Waspada"}
        hasil[label] = label_map.get(predicted_index, "Tidak diketahui")

    print("berhasil")    
    return {
        "error": False,
        "message": "Prediksi berhasil",
        "predictions": hasil
    }
