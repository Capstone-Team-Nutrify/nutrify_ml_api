import os
from flask import Flask, jsonify
from flask_cors import CORS 

from .routes import main

# Inisialisasi aplikasi Flask
app = Flask(__name__)
app.json.sort_keys = False
app.config['DEBUG'] = True

CORS(app)

# Mengimpor blueprint atau routing dari file lain
app.register_blueprint(main)
