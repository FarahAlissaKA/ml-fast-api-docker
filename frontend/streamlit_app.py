import streamlit as st
import requests

st.title('Calories Burned Prediction')

gender = st.radio("**Gender**", ["Male", "Female"],)
if gender == 'Female':
    gender_value = 1
else:
    gender_value = 0
age = st.slider('**Age**', 0, 100)
height = st.slider('**Height (cm)**', 1, 250)
heart_rate = st.slider('**Heart Rate (bpm)**', 1, 200)
body_temp = st.slider('**Body Temperature (°C)**', 1.0, 50.0, step=0.1)

display = {
    "Gender": 'Male' if gender_value == 0 else 'Female',
    "Age": float(age),
    "Height": float(height),
    "Heart_Rate": float(heart_rate),
    "Body_Temp": float(body_temp)
}

st.write('**Features**', display)

input_data = {
    "Gender": gender_value,
    "Age": float(age),
    "Height": float(height),
    "Heart_Rate": float(heart_rate),
    "Body_Temp": float(body_temp)
}

response = requests.post('http://backend:8000/predict/', json=input_data)

prediction = response.json()
st.write('**Prediction Result**', prediction)