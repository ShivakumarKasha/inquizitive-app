# app.py
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/data')
def get_data():
    data = {'Teacher': 'xyz'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
