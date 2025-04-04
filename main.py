from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("Heart_disease_prediction(knn).joblib")


class HeartDiseaseInput(BaseModel):
    age: int
    sex: int
    chest_pain_type: int
    resting_blood_pressure: int
    cholestoral: int
    fasting_blood_sugar: int
    rest_ecg: int
    Max_heart_rate: int
    exercise_induced_angina: int
    oldpeak: float
    slope: int
    vessels_colored_by_flourosopy: int
    thalassemia: int

@app.get('/')
def home():
    return {"message": "Welcome to Heart Disease Prediction"}

@app.post('/predict')
def predict(data: HeartDiseaseInput):
    input_data = [[
        data.age, data.sex, data.chest_pain_type, data.resting_blood_pressure,
        data.cholestoral, data.fasting_blood_sugar, data.rest_ecg, data.Max_heart_rate,
        data.exercise_induced_angina, data.oldpeak, data.slope, data.vessels_colored_by_flourosopy,
        data.thalassemia
    ]]

    input_df = pd.DataFrame(input_data, columns=HeartDiseaseInput.model_fields.keys())
    prediction = model.predict(input_data)
    result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"
    return {"prediction": result}

# @app.get('/gettask')
# def get_all_tasks():
#     return tasks_db

# @app.get('/gettask/{owner}')
# def get_task(owner: str):
#     for task in tasks_db:
#         if task['owner'] == owner:
#             return task
#     raise HTTPException(status_code=404, detail="Task not found")

# @app.put('/completetask/{task_id}')
# def complete_task(task_id: int):
#     for task in tasks_db:
#         if task['id'] == task_id:
#             task['is_completed'] = True
#             return task
#     raise HTTPException(status_code=404, detail="Task not found")
