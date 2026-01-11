from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Student Performance Predictor")

# Enable CORS (useful for dev, though less critical if serving strictly from same origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model, scaler, and feature names
# Use robust path finding for deployment envs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'student_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'models', 'scaler.pkl')
FEATURES_PATH = os.path.join(BASE_DIR, 'models', 'feature_names.pkl')

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    feature_names = joblib.load(FEATURES_PATH)
except Exception as e:
    print(f"Error loading models: {e}")
    # In production, you might want to crash or handle this gracefully
    model = None

class StudentData(BaseModel):
    Attendance: float
    Study_Hours: float
    Previous_Scores: float
    Sleep_Hours: float
    Extracurricular: int

@app.post("/predict")
async def predict(data: StudentData):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded correctly")
        
    try:
        # Prepare input
        input_data = np.array([[
            data.Attendance,
            data.Study_Hours,
            data.Previous_Scores,
            data.Sleep_Hours,
            data.Extracurricular
        ]])
        
        # Scale
        input_scaled = scaler.transform(input_data)
        
        # Predict
        prediction = int(model.predict(input_scaled)[0])
        probabilities = model.predict_proba(input_scaled)[0].tolist()
        
        # Classes: 0: At-Risk, 1: Average, 2: Excellent
        result_map = {0: "At-Risk", 1: "Average", 2: "Excellent"}
        result = result_map[prediction]
        
        # Generate suggestions
        suggestions = []
        if data.Attendance < 85:
            suggestions.append("Increase classroom attendance to at least 90%.")
        if data.Study_Hours < 5:
            suggestions.append("Dedicate more hours to self-study (aim for 6+ hours/day).")
        if data.Sleep_Hours < 7:
            suggestions.append("Ensure at least 7-8 hours of sleep for better cognitive function.")
        if data.Previous_Scores < 70:
            suggestions.append("Review previous exam materials and seek tutoring for weak subjects.")
            
        if not suggestions:
            suggestions.append("Keep up the great work! Maintain your current routine.")

        return {
            "prediction_code": prediction,
            "status": result,
            "probabilities": probabilities,
            "suggestions": suggestions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mount frontend
# We check if the directory exists to avoid errors during development if paths differ
frontend_path = os.path.join(BASE_DIR, 'app/frontend')
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    # Port 8000 is default, but Render/Heroku provide PORT env var
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
