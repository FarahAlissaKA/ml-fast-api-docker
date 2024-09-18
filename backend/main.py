from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.joblib')

model = joblib.load(model_path)

app = FastAPI(title="Calories ML API", description="API for calories dataset ml model", version="1.0")

class CaloriesDataRequest(BaseModel):
	Gender: int
	Age: int
	Height: float
	Heart_Rate: float
	Body_Temp: float

@app.get("/")
async def read_root():
	return {"message": "Welcome to the model API!"}

@app.post("/predict/", tags=['Predict Calories Burned'])
async def predict(request: CaloriesDataRequest):
	features = [request.Gender, request.Age, request.Height, request.Heart_Rate, request.Body_Temp]
	#location_features = [1 if f'location_{request.location}' in model.feature_names_in_ else 0 for _ in range(len(model.feature_names_in_) - len(features))]
	#features.extend(location_features)

	prediction = model.predict([features])
	return {"Predicted Calories Burned": prediction[0]}

#@app.post("/predict/", tags=["predictions"])
#async def predict_calories(data: dict):
#	features = np.array(data['Gender','Age','Height','Heart_Rate','Body_Temp']).reshape(1, -1)
#	prediction = model.predict(features)
#	class_name = calories.target_names[prediction][0]

#	return {"class": class_name}