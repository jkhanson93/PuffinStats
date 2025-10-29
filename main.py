# app.py (Flask Backend)
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Puff!"

@app.route('/api/data', methods=['GET'])
def get_data():
    # Example: Fetch data from a database or perform a calculation
    fed_time = ""
    with open("fedpuff.txt", "r") as file:
        fed_time = file.read()
    data = {'message': 'Puffin was last fed at:', 'value': fed_time}
    return jsonify(data)

@app.route('/api/process', methods=['POST'])
def process_data():
    input_data = request.json
    curr_datetime = datetime.now()
    formatted_dt = curr_datetime.strftime("%H:%M on %m-%d-%Y")
    with open("fedpuff.txt", "w") as file:
        file.write(formatted_dt)
    # Example: Process the input data
    result = {'processed_message': f"You fed the Puff at {formatted_dt}"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)