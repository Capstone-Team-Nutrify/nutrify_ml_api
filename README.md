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
    "food": [
      {
        "ingredient": "kaldu ayam",
        "dose": 250
      },
      {
        "ingredient": "wortel mentah",
        "dose": 200
      },
      {
        "ingredient": "nasi jagung",
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
    "predict": {
      "food": [
        {
          "ingredient": "kaldu ayam",
          "dose": 250
        },
        {
          "ingredient": "wortel mentah",
          "dose": 200
        },
        {
          "ingredient": "nasi jagung",
          "dose": 100
        }
      ],
      "total_nutrition": {
        "sugar": 8.8,
        "fiber": 3.8,
        "protein": 5.5,
        "fat": 1.75,
        "carbohydrate": 39.3,
        "vitamin_A": 0.2,
        "vitamin_C": 220.45,
        "iron": 55.15,
        "calcium": 94.15,
        "sodium": 50.45,
        "magnesium": 11.9,
        "cholesterol": 0.0,
        "calories": 190.0,
        "phosphorus": 106.8,
        "potassium": 543.3,
        "zinc": 26.7,
        "water": 683.4,
        "vitamin_B1": 71.8,
        "vitamin_B11": 128.0,
        "vitamin_B12": 68.0,
        "vitamin_B2": 1.18,
        "vitamin_B3": 77.6,
        "vitamin_B5": 8.3,
        "vitamin_B6": 182.1,
        "vitamin_D": 7.2,
        "vitamin_E": 35.0,
        "vitamin_K": 0.8
      },
      "disease_rate": [
        {
          "disease": "Influenza",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Liver",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Diabetes",
          "status": "Warning",
          "level": "high"
        },
        {
          "disease": "Anemia",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Diare",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Batu_Ginjal",
          "status": "Warning",
          "level": "high"
        },
        {
          "disease": "Asma",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Asam_Lambung",
          "status": "Warning",
          "level": "high"
        },
        {
          "disease": "Serangan_Jantung",
          "status": "Warning",
          "level": "high"
        },
        {
          "disease": "Asam_Urat",
          "status": "Warning",
          "level": "high"
        },
        {
          "disease": "Radang_Paru_paru",
          "status": "Warning",
          "level": "high"
        },
        {
          "disease": "Jerawat",
          "status": "Warning",
          "level": "high"
        },
        {
          "disease": "Hepatitis",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Wasir",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Sinusitis",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Kolesterol",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Usus_Buntu",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Tifus",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Osteoporosis",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Malaria",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Alergi_Dingin",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Alergi_Kacang",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Alergi_Seafood",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Alergi_Susu",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Alergi_Telur_Ayam",
          "status": "Neutral",
          "level": "medium"
        },
        {
          "disease": "Alergi_Buah_Beri",
          "status": "Normal Consumption",
          "level": "normal"
        }
      ]
    }
  }
  ```
