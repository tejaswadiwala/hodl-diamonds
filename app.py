from flask import Flask, jsonify
from flask_cors import CORS
from src.logger import logger

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    logger.info('Health check is fine')
    return jsonify({'data': 'ok'}), 200