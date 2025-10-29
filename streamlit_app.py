# streamlit_app.py (Streamlit Frontend)
import streamlit as st
import requests
from datetime import datetime

def get_last_fed_info():
    """Fetch the last-fed information for Puffin from the backend API.

    Sends a GET request to the local Flask backend at /api/lastFed. If the
    request succeeds (HTTP 200) the JSON-decoded response from the server is
    returned in the 'response' field. If the request fails, an error string is
    produced and a short entry is written to `error_log.txt` containing the
    timestamp and the failing status code.

    Returns:
        dict: {
            'status_code': int,
            'response': dict | str  # JSON-decoded response on success, or error text
        }
    """
    response = requests.get("http://localhost:5000/api/lastFed")
    if response.status_code == 200:
        msg = response.json()
    else:
        msg = "Failed to find when Puff ate"
        with open("error_log.txt", "w") as file:
            curr_dt = datetime.now()
            formatted_dt = curr_dt.strftime("%#I:%M %p on %m-%d-%Y")
            file.write(f"Failed to find when Puff ate at {formatted_dt} with code {response.status_code}")

    data = {
            'status_code': response.status_code,
            'response' : msg
        }

    return data

def feed_puff():
    """Notify the backend that Puff was fed (POST /api/feed).

    Sends a POST request to the local Flask backend to update the last-fed
    timestamp. On success (HTTP 200) the JSON-decoded server response is
    returned. On failure this function writes an entry to `error_log.txt` with
    a timestamp and status code and returns an error string in the
    'response' field.

    Returns:
        dict: {
            'status_code': int,
            'response': dict | str  # JSON-decoded server response or error text
        }
    """
    response = requests.post("http://localhost:5000/api/feed")
    if response.status_code == 200:
        msg = response.json()
    else:
        msg = "Failed to update Puff's last fed date"
        with open("error_log.txt", "w") as file:
            curr_dt = datetime.now()
            formatted_dt = curr_dt.strftime("%#I:%M %p on %m-%d-%Y")
            file.write(f"Failed to feed Puff at {formatted_dt} with code {response.status_code}")
    
    data = {
        'status_code': response.status_code,
        'response': msg
    }

    return data

def get_box_status():
    """Retrieve Puff's box status from the backend (GET /api/boxStatus).

    Sends a GET request to the local Flask backend. On success returns the
    JSON-decoded payload in the 'response' field. On failure writes an entry to
    `error_log.txt` with a timestamp and HTTP status code and returns an error
    string in the response field.

    Returns:
        dict: {
            'status_code': int,
            'response': dict | str
        }
    """
    response = requests.get("http://localhost:5000/api/boxStatus")
    if response.status_code == 200:
        msg = response.json()
    else:
        msg = "Failed to get Puff's box status"
        with open("error_log.txt", "w") as file:
            curr_dt = datetime.now()
            formatted_dt = curr_dt.strftime("%#I:%M %p on %m-%d-%Y")
            file.write(f"Failed to get Puff\'s box status at {formatted_dt} with code {response.status_code}")

    data = {
        'status_code': response.status_code,
        'response': msg
    }

    return data

def clean_box(user_input):
    """Report to the backend that Puff's box was cleaned by a person.

    Sends a POST request with JSON payload {"person": user_input} to
    /api/cleanBox. On success returns the server's JSON-decoded response in
    the 'response' field. On failure writes an entry to `error_log.txt` with a
    timestamp and status code and returns an error string in the response.

    Args:
        user_input (str): The name of the person who cleaned the box.

    Returns:
        dict: {
            'status_code': int,
            'response': dict | str
        }
    """
    payload = {'person': user_input}
    response = requests.post("http://localhost:5000/api/cleanBox", json=payload)
    if response.status_code == 200:
        msg = response.json()
    else:
        msg = "Failed to update Puff's box status"
        with open("error_log.txt", "w") as file:
            curr_dt = datetime.now()
            formatted_dt = curr_dt.strftime("%#I:%M %p on %m-%d-%Y")
            file.write(f"Failed to clean Puff\'s box at {formatted_dt} with code {response.status_code}")

    data = {
        'status_code': response.status_code,
        'response': msg
    }

    return data

def change_box(user_input):
    """Report to the backend that Puff's box was changed by a person.

    Sends a POST request with JSON payload {"person": user_input} to
    /api/changeBox. On success returns the server's JSON-decoded response in
    the 'response' field. On failure writes an entry to `error_log.txt` with a
    timestamp and status code and returns an error string in the response.

    Args:
        user_input (str): The name of the person who changed the box.

    Returns:
        dict: {
            'status_code': int,
            'response': dict | str
        }
    """
    payload = {'person': user_input}
    response = requests.post("http://localhost:5000/api/changeBox", json=payload)
    if response.status_code == 200:
        msg = response.json()
    else:
        msg = "Failed to update Puff's box status"
        with open("error_log.txt", "w") as file:
            curr_dt = datetime.now()
            formatted_dt = curr_dt.strftime("%#I:%M %p on %m-%d-%Y")
            file.write(f"Failed to change Puff\'s box at {formatted_dt} with code {response.status_code}")
    
    data = {
        'status_code': response.status_code,
        'response': msg
    }

    return data

st.title("Don't Let Puffin Lie To You")
status = ""

left_col, right_col = st.columns(2)

with left_col:
    st.header("Puff Intake:")
    # Fetch Puffin's Last Fed Date
    if st.button("When did the Puff last eat?"):
        status = get_last_fed_info()

    # Feed Puffin
    if st.button("I just fed the Puff"):
        status = feed_puff()

with right_col:
    st.header("Puff Output:")
    # Fetch data from Flask API
    if st.button("How's Puff's Box Doing?"):
        status = get_box_status()

    user_input = st.selectbox(
        'Who cleaned/changed Puff\'s Box?',
        ['Joel', 'Lexi', 'A Stranger']
    )
    if st.button("Cleaned Puff's Box"):
        if user_input:
            status = clean_box(user_input)
        else:
            st.error("Please enter a person")
        

    if st.button("Changed Puff's Box"):
        if user_input:
            status = change_box(user_input)
        else:
            st.error("Please enter a person")

st.header("Puff Status:")
if status:
    if status['status_code'] == 200:
        st.write(status['response']['message'])
    else:
        st.error(status['response'])