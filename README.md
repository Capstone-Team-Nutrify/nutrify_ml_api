# NUTRIFY MACHINE LEARNING API 🤖

```markdown
# Prerequisites

Before running the application, make sure you have the following installed on your machine:

- [Python 3](https://www.python.org/)
```

## Build With

![Logo](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Logo](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white)

![Logo](https://img.shields.io/badge/TensorFlow-FF3F06?style=for-the-badge&logo=tensorflow&logoColor=white)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Capstone-Team-Nutrify/nutrify_ml_api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd nutrify_ml_api
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the Flask server and run the database setup:

```bash
python main.js
```

## API URL

Coming Soon

## API Endpoints

### 1. Predict Disease Rate

- **Method:** `POST`
- **Path:** `/predict`
- **Description:** endpoint for predict disease rate, data can one or more
- **Request Body:**

  ```json
  {
    "makanan": [
      {
        "bahan": "kaldu ayam",
        "dose": 300
      },
      {
        "bahan": "wortel mentah",
        "dose": 150
      },
      {
        "bahan": "nasi jagung",
        "dose": 100
      }
    ]
  }
  ```

- **Response Body: 200**

  ```json
  {
    "status": 200,
    "message": "success",
    "description": "success insert to mongodb database",
    "predict": {
      "makanan": [
        {
          "bahan": "kaldu ayam",
          "dose": 300
        },
        {
          "bahan": "wortel mentah",
          "dose": 150
        },
        {
          "bahan": "nasi jagung",
          "dose": 100
        }
      ],
      "total_nutrisi": {
        "gula": 7.35,
        "serat": 2.95,
        "protein": 5.7,
        "lemak": 1.95,
        "karbohidrat": 36.9,
        "vitamin_A": 0.2,
        "vitamin_C": 186.7,
        "zat_besi": 44.4,
        "kalsium": 87.2,
        "natrium": 38.9,
        "magnesium": 13.0,
        "kolesterol": 0.0,
        "kalori": 183.5,
        "fosfor": 120.1,
        "kalium": 626.6,
        "zinc": 20.8,
        "air": 771.35,
        "vitamin_B1": 85.8,
        "vitamin_B11": 96.0,
        "vitamin_B12": 51.0,
        "vitamin_B2": 1.19,
        "vitamin_B3": 61.7,
        "vitamin_B5": 8.02,
        "vitamin_B6": 218.0,
        "vitamin_D": 5.4,
        "vitamin_E": 35.0,
        "vitamin_K": 0.6
      },
      "disease_rate": [
        {
          "penyakit": "Influenza",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Liver",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Diabetes",
          "status": "Waspada",
          "badge": "danger"
        },
        {
          "penyakit": "Anemia",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Diare",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Batu_Ginjal",
          "status": "Waspada",
          "badge": "danger"
        },
        {
          "penyakit": "Asma",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Asam_Lambung",
          "status": "Waspada",
          "badge": "danger"
        },
        {
          "penyakit": "Serangan_Jantung",
          "status": "Waspada",
          "badge": "danger"
        },
        {
          "penyakit": "Asam_Urat",
          "status": "Waspada",
          "badge": "danger"
        },
        {
          "penyakit": "Radang_Paru_paru",
          "status": "Waspada",
          "badge": "danger"
        },
        {
          "penyakit": "Jerawat",
          "status": "Waspada",
          "badge": "danger"
        },
        {
          "penyakit": "Hepatitis",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Wasir",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Sinusitis",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Kolesterol",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Usus_Buntu",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Tifus",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Osteoporosis",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Malaria",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Alergi_Dingin",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Alergi_Kacang",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Alergi_Seafood",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Alergi_Susu",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Alergi_Telur_Ayam",
          "status": "Netral",
          "badge": "secondary"
        },
        {
          "penyakit": "Alergi_Buah_Beri",
          "status": "Konsumsi Wajar",
          "badge": "success"
        }
      ]
    }
  }
  ```
