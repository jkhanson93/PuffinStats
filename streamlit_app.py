# streamlit_app.py (Streamlit Frontend)
import streamlit as st
import requests
from datetime import datetime

st.title("Don't Let Puffin Lie To You")

# Fetch data from Flask API
if st.button("When did the Puff last eat?"):
    response = requests.get("http://localhost:5000/api/data")
    if response.status_code == 200:
        data = response.json()
        st.write(data['message'])
        st.write(data['value'])
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
    response = requests.post("http://localhost:5000/api/process", json=payload)
    if response.status_code == 200:
        result = response.json()
        st.write(result['processed_message'])
    else:
        with open("error_log.txt", "w") as file:
            curr_dt = datetime.now()
            formatted_dt = curr_dt.strftime("%H:%M on %m-%d-%Y")
            file.write(f"Failed to feed Puff at {formatted_dt} with code {response.status_code}")
        st.error(f"Error processing data: {response.status_code}")