# app.py (Flask Backend)
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Simple health endpoint for the Puffin app.

    Returns a plain-text greeting. Useful for a quick smoke test to verify
    the Flask app is running and reachable.

    Returns:
        str: A short greeting message.
    """
    return "Hello, Puff!"

@app.route('/api/lastFed', methods=['GET'])
def get_last_fed():
    # Example: Fetch data from a database or perform a calculation
    fed_time = ""
    with open("fedpuff.txt", "r") as file:
        fed_time = file.read()

    """Return the last time Puffin was fed.

    Reads the timestamp stored in `fedpuff.txt` and returns it as a JSON
    message. If the file is missing an exception will be raised by the file
    open/read operation (caller should ensure the file exists or handle the
    exception in production code).

    Returns:
        flask.wrappers.Response: JSON response with shape {'message': str}
    """
    data = {'message': f"Puffin was last fed at {fed_time}"}
    return jsonify(data)

@app.route('/api/feed', methods=['POST'])
def feed_puff():
    curr_datetime = datetime.now()
    formatted_dt = curr_datetime.strftime("%#I:%M %p on %m-%d-%Y")
    """Record the current time as the last-fed time for Puffin.

    Writes a human-readable timestamp to `fedpuff.txt` and returns a JSON
    confirmation message. The timestamp format matches the display used in
    the Streamlit frontend.

    Returns:
        flask.wrappers.Response: JSON response with shape {'message': str}
    Side effects:
        Writes to `fedpuff.txt` in the current working directory.
    """
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

    """Return Puff's current box status.

    Reads the content of `puffbox.txt` and returns it as a JSON message. The
    file is used here as a simple persistent store for human-readable status
    messages. If the file is missing an exception will be raised by the file
    operations.

    Returns:
        flask.wrappers.Response: JSON response with shape {'message': str}
    """
    data = {'message': f"{box_status}"}
    return jsonify(data)

@app.route('/api/cleanBox', methods=['POST'])
def clean_box():
    input_data = request.json
    cleaner = input_data['person']
    curr_datetime = datetime.now()
    formatted_dt = curr_datetime.strftime("%#I:%M %p on %m-%d-%Y")
    """Mark Puff's box as cleaned by the provided person.

    Expects a JSON POST body with the shape {'person': <name>}. Writes a
    human-readable message into `puffbox.txt` and returns a JSON confirmation
    message. If the POST body is missing or malformed a KeyError may be
    raised; production code should validate the incoming JSON.

    Returns:
        flask.wrappers.Response: JSON response with shape {'message': str}
    Side effects:
        Writes to `puffbox.txt` in the current working directory.
    """
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
    """Mark Puff's box as changed by the provided person.

    Expects a JSON POST body with the shape {'person': <name>}. Writes a
    human-readable message into `puffbox.txt` and returns a JSON confirmation
    message. If the POST body is missing or malformed a KeyError may be
    raised; production code should validate the incoming JSON.

    Returns:
        flask.wrappers.Response: JSON response with shape {'message': str}
    Side effects:
        Writes to `puffbox.txt` in the current working directory.
    """
    with open("puffbox.txt", "w") as file:
        file.write(f"{cleaner} changed Puff's box at {formatted_dt}")

    # Example: Process the input data
    result = {'message': f"{cleaner} changed Puff's box at {formatted_dt}"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)