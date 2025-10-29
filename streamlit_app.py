# streamlit_app.py (Streamlit Frontend)
import streamlit as st
import requests
from datetime import datetime

def get_last_fed_info():
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