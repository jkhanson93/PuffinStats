# app.py (Flask Backend)
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Puff!"

@app.route('/api/lastFed', methods=['GET'])
def get_last_fed():
    # Example: Fetch data from a database or perform a calculation
    fed_time = ""
    with open("fedpuff.txt", "r") as file:
        fed_time = file.read()
    data = {'message': f"Puffin was last fed at {fed_time}"}
    return jsonify(data)

@app.route('/api/feed', methods=['POST'])
def feed_puff():
    curr_datetime = datetime.now()
    formatted_dt = curr_datetime.strftime("%#I:%M %p on %m-%d-%Y")
    with open("fedpuff.txt", "w") as file:
        file.write(formatted_dt)
    # Example: Process the input data
    result = {'message': f"You fed the Puff at {formatted_dt}"}
    return jsonify(result)

@app.route('/api/boxStatus', methods=['GET'])
def get_box_status():
    # Example: Fetch data from a database or perform a calculation
    box_status = ""
    with open("puffbox.txt", "r") as file:
        box_status = file.read()
    data = {'message': f"{box_status}"}
    return jsonify(data)

@app.route('/api/cleanBox', methods=['POST'])
def clean_box():
    input_data = request.json
    cleaner = input_data['person']
    curr_datetime = datetime.now()
    formatted_dt = curr_datetime.strftime("%#I:%M %p on %m-%d-%Y")
    with open("puffbox.txt", "w") as file:
        file.write(f"{cleaner} cleaned Puff's box at {formatted_dt}")
    # Example: Process the input data
    result = {'message': f"{cleaner} cleaned Puff's box at {formatted_dt}"}
    return jsonify(result)

@app.route('/api/changeBox', methods=['POST'])
def change_box():
    input_data = request.json
    cleaner = input_data['person']
    curr_datetime = datetime.now()
    formatted_dt = curr_datetime.strftime("%#I:%M %p on %m-%d-%Y")
    with open("puffbox.txt", "w") as file:
        file.write(f"{cleaner} changed Puff's box at {formatted_dt}")
    # Example: Process the input data
    result = {'message': f"{cleaner} changed Puff's box at {formatted_dt}"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)