from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the trained model (model.joblib)
model_path = os.path.join(current_dir, 'model.joblib')

# Load the pre-trained RandomForest model from the file
model = joblib.load(model_path)

# Initialize the FastAPI app with metadata (title, description, version)
app = FastAPI(title="Calories ML API", description="Gender (0-Male, 1-Female), Age in years, Height in cm, Heart Rate in bpm, Body Temperature in °C", version="1.0")

# Define the structure of incoming request data using Pydantic BaseModel
class CaloriesDataRequest(BaseModel):
    Gender: int = Field(..., description="Gender (0-Male, 1-Female)")
    Age: int = Field(..., description="Age in years")
    Height: int = Field(..., description="Height in cm")
    Heart_Rate: int = Field(..., description="Heart Rate in bpm")
    Body_Temp: float = Field(..., description="Body Temperature in °C")

# Define a root route (GET request) for testing the API
@app.get("/", tags=['Welcome'])
async def read_root():
	return {"message": "Welcome to the model API!"}

# Define the /predict/ endpoint (POST request) for making predictions
@app.post("/predict/", tags=['Predict Calories Burned'])
async def predict(request: CaloriesDataRequest):
	# Extract features from the incoming request
	features = [request.Gender, request.Age, request.Height, request.Heart_Rate, request.Body_Temp]

	# Use the pre-loaded model to make a prediction
	prediction = model.predict([features])

	# Return the predicted calories burned as a response
	return {"Predicted Calories Burned": prediction[0]}