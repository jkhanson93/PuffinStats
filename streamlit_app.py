# streamlit_app.py (Streamlit Frontend)
import streamlit as st
import requests
from datetime import datetime

st.title("Don't Let Puffin Lie To You")
status = ""

left_col, right_col = st.columns(2)

with left_col:
    st.header("Puffin Intake:")
    # Fetch data from Flask API
    if st.button("When did the Puff last eat?"):
        response = requests.get("http://localhost:5000/api/lastFed")
        if response.status_code == 200:
            data = response.json()
            status = data['value']
        else:
            st.error("No record of Puff's last meal")
            st.error(f"Tech reason (for Joel): {response.status_code}")
            with open("error_log.txt", "w") as file:
                curr_dt = datetime.now()
                formatted_dt = curr_dt.strftime("%H:%M on %m-%d-%Y")
                file.write(f"Failed to find when Puff ate at {formatted_dt} with code {response.status_code}")

    # # Send data to Flask API for processing
    # user_input = st.text_input("Enter a message to process:")
    if st.button("I just fed the Puff"):
        payload = {'message': 'I fed Puff!'}
        response = requests.post("http://localhost:5000/api/feed", json=payload)
        if response.status_code == 200:
            result = response.json()
            status = result['message']
        else:
            with open("error_log.txt", "w") as file:
                curr_dt = datetime.now()
                formatted_dt = curr_dt.strftime("%H:%M on %m-%d-%Y")
                file.write(f"Failed to feed Puff at {formatted_dt} with code {response.status_code}")
            st.error(f"Error processing data: {response.status_code}")

with right_col:
    st.header("Puffin Output:")
    # Fetch data from Flask API
    if st.button("How's Puff's Box Doing?"):
        response = requests.get("http://localhost:5000/api/boxStatus")
        if response.status_code == 200:
            data = response.json()
            status = data['value']
        else:
            st.error("No record of Puff's box")
            st.error(f"Tech reason (for Joel): {response.status_code}")
            with open("error_log.txt", "w") as file:
                curr_dt = datetime.now()
                formatted_dt = curr_dt.strftime("%H:%M on %m-%d-%Y")
                file.write(f"Failed to get Puff\'s box status at {formatted_dt} with code {response.status_code}")

    user_input = st.selectbox(
        'Who cleaned/changed Puff\'s Box?',
        ['Joel', 'Lexi', 'A Stranger']
    )
    if st.button("Cleaned Puff's Box"):
        if user_input:
            payload = {'person': user_input}
            response = requests.post("http://localhost:5000/api/cleanBox", json=payload)
            if response.status_code == 200:
                result = response.json()
                status = result['message']
            else:
                with open("error_log.txt", "w") as file:
                    curr_dt = datetime.now()
                    formatted_dt = curr_dt.strftime("%H:%M on %m-%d-%Y")
                    file.write(f"Failed to clean Puff\'s box at {formatted_dt} with code {response.status_code}")
                st.error(f"Error processing data: {response.status_code}")
        else:
            st.error("Please enter a person")
        

    if st.button("Changed Puff's Box"):
        if user_input:
            payload = {'person': user_input}
            response = requests.post("http://localhost:5000/api/changeBox", json=payload)
            if response.status_code == 200:
                result = response.json()
                status = result['message']
            else:
                with open("error_log.txt", "w") as file:
                    curr_dt = datetime.now()
                    formatted_dt = curr_dt.strftime("%H:%M on %m-%d-%Y")
                    file.write(f"Failed to change Puff\'s box at {formatted_dt} with code {response.status_code}")
                st.error(f"Error processing data: {response.status_code}")
        else:
            st.error("Please enter a person")

st.header("Puff Status:")
if status:
    st.write(status)