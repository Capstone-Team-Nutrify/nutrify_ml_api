from flask import Blueprint, request, jsonify
from .libs.predict import handle_prediction, translate_keys_to_indonesian

main = Blueprint('main', __name__)

@main.route("/", methods = ["GET"])
def index():
    
     return jsonify({
        'status': {
            'code': 200,
            'message': 'Model Nutrify',
            'teamName': 'CC25-CF083'
        }
    }), 200
     
@main.route("/predict", methods = ["POST"])
def predict_route():
    try:
        data = request.get_json()
        print("Received data:", data)

        if not data or "food" not in data:
            return jsonify({"error": "Field 'makanan' is missing"}), 400

        makanan_input = data["food"]

        # Optional: cek validitas masing-masing item
        for item in makanan_input:
            if "ingredient" not in item or "dose" not in item:
                return jsonify({"error": "Each item must have 'ingeredient' and 'dose'"}), 400

        # Menerjemahkan kunci dari bahasa Inggris ke bahasa Indonesia
        translate_data = translate_keys_to_indonesian(data)
        
        #prediksi disease rate
        response = handle_prediction(translate_data)

        result = {
            "status": 200,
            "message": "success",
            "predict": response
        }
        return jsonify(result), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500
