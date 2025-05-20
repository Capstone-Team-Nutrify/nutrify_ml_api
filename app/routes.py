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
    data = request.get_json()
    print(data)
    if not data or "makanan" not in data:
        return jsonify({"error": "No makanan provided"}), 400
    
    try:
        respone = handle_prediction(data["makanan"])
        result = {
            "status": 200,
            "message": "success",
            "diesease rate": respone
        }
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
