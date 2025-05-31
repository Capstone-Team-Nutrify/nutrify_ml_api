from flask import Blueprint, request, jsonify
from .libs.predict import handle_prediction

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

        if not data or "makanan" not in data:
            return jsonify({"error": "Field 'makanan' is missing"}), 400

        makanan_input = data["makanan"]

        # Optional: cek validitas masing-masing item
        for item in makanan_input:
            if "bahan" not in item or "dose" not in item:
                return jsonify({"error": "Each item must have 'bahan' and 'dose'"}), 400

        response = handle_prediction(data)

        result = {
            "status": 200,
            "message": "success",
            "predict": response
        }
        return jsonify(result), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500
