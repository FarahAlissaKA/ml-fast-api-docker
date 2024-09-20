# Calories Burned Prediction API

## Project Overview

This project involves deploying a machine learning model using FastAPI and Docker. The goal is to develop a REST API that provides calorie burn predictions based on various input features. The model is built using a Random Forest Regressor and is integrated with FastAPI for the backend and Streamlit for the frontend. Docker is used to containerize the application, ensuring consistent environments for deployment.

## Features

- **Predicts Calories Burned**: Uses Random Forest Regressor to estimate calories burned based on gender, age, height, heart rate, and body temperature.
- **REST API**: Developed with FastAPI to serve the ML model's predictions via HTTP requests.
- **Interactive Frontend**: Built with Streamlit to allow users to input their data and receive predictions in a user-friendly interface.
- **Dockerized**: The application is containerized using Docker for easy deployment and scalability.

## Technologies Used

- **Python**: The primary programming language.
- **FastAPI**: Framework for building the REST API.
- **Streamlit**: Framework for creating the interactive frontend.
- **Docker**: Containerization platform used to package the application.
- **scikit-learn**: Library used for building the Random Forest Regressor model.
- **pandas**: Library used for data manipulation and analysis.

## Project Structure

- **backend/**: Contains the FastAPI application for serving the model.
- **frontend/**: Contains the Streamlit application for the user interface.
- **model/**: Contains code and data for building and training the ML model.
- **docker-compose.yml**: Configuration file for Docker Compose to set up and run the multi-container Docker applications.

## Installation Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/FarahAlissaKA/ml-fast-api-docker.git
   ```

2. **Build and Run with Docker Compose:**
   - Ensure Docker Engine is running on your machine.
   - Navigate your terminal to the folder containing cloned repository.
   ```bash
   docker-compose up --build
   ```

3. **Access the Applications:**
   - **API**: Accessible at `http://localhost:8000/docs`
   - **Frontend**: Accessible at `http://localhost:8501`

## Usage Instructions

1. **Using the API:**
   - Send POST requests to `http://localhost:8000/predict/` with a JSON payload containing features: `gender`, `age`, `height`, `heart_rate`, and `body_temp`.

2. **Using the Frontend:**
   - Open `http://localhost:8501` in browser to interact with the Streamlit application and get calorie burn predictions.
