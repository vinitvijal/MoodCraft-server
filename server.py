from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/api/start_recording', methods=['POST'])
def start_recording():
    return jsonify({'message': 'Recording started successfully'})

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello world!'})


if __name__ == '__main__':
    app.run(debug=True)
