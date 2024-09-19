import streamlit as st
import requests

# Set the title of the Streamlit app
st.title('Calories Burned Prediction')

# Create a radio button to select gender
gender = st.radio("**Gender**", ["Male", "Female"],)
# Convert gender input to integer values (0 for Male, 1 for Female)
if gender == 'Female':
    gender_value = 1
else:
    gender_value = 0

# Slider input for age (0-100 years)
age = st.slider('**Age**', 0, 100)

# Slider input for height (1-250 cm)
height = st.slider('**Height (cm)**', 1, 250)

# Slider input for heart rate (1-200 bpm)
heart_rate = st.slider('**Heart Rate (bpm)**', 1, 200)

# Slider input for body temperature (1.0-50.0°C, step size of 0.1°C)
body_temp = st.slider('**Body Temperature (°C)**', 1.0, 50.0, step=0.1)

# Display the selected input features in the app
display = {
    "Gender": 'Male' if gender_value == 0 else 'Female',
    "Age": float(age),
    "Height": float(height),
    "Heart_Rate": float(heart_rate),
    "Body_Temp": float(body_temp)
}

# Show the user-selected features in the app
st.write('**Features**', display)

# Prepare the input data to send to the FastAPI backend as JSON
input_data = {
    "Gender": gender_value,
    "Age": int(age),
    "Height": int(height),
    "Heart_Rate": int(heart_rate),
    "Body_Temp": float(body_temp)
}

# Send a POST request to the FastAPI backend's /predict/ endpoint
response = requests.post('http://backend:8000/predict/', json=input_data)

# Parse the JSON response from the API (prediction result)
prediction = response.json()
st.write('**Prediction Result**', prediction)