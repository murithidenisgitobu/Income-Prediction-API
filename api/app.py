from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

description = '''This API focuses on leveraging machine learning to predict whether individuals in developing
nations earn above or below a specific income threshold,
aiming to address the pressing issue of income inequality mostly witnessed in developing nations.'''

app = FastAPI(description=description)

# loading models and encoder
random = joblib.load('../toolkit/rf_model.joblib')  
xgb = joblib.load('../toolkit/xgb_model.joblib')
encoder = joblib.load('../toolkit/label_encoder.joblib')

class Features(BaseModel):
    age: int
    gender: str
    education: str
    marital_status: str
    race: str
    is_hispanic: str
    employment_commitment: str
    employment_stat: int
    wage_per_hour: int
    working_week_per_year: int
    industry_code: int
    industry_code_main: int
    occupation_code: int
    total_employed: int
    household_stat: str
    household_summary: str
    vet_benefit: int
    tax_status: str
    gains: int
    losses: int
    stocks_status: int
    citizenship: str
    mig_year: int
    country_of_birth_own: str
    country_of_birth_mother: str
    country_of_birth_father: str
    importance_of_record: float

@app.get('/')
def status_check(
    title: str = Query('Income Prediction API', title='Project Title', description='Title of the project'),
):
    status_message = {
        'message': 'API is Online: to go to the prediction page add "/docs" to the address'
    }
    return status_message

@app.post('/predict_income')
def predict_income(data: Features, model: str = Query('xgb', enum=['random','xgb'])):
    df = pd.DataFrame([data.model_dump()])
    
    # Select the model based on the query parameter
    if model == 'random':
        prediction = random.predict(df)
        probability = random.predict_proba(df)
    elif model == 'xgb':
        prediction = xgb.predict(df)
        probability = xgb.predict_proba(df)
    else:
        raise HTTPException(status_code=400, detail="Invalid model name provided.")
    
    prediction = int(prediction[0])
    prediction = encoder.inverse_transform([prediction])[0]
    probability = probability[0]
    
    return {
        'model_used': model,
        'prediction': prediction,
        'probability': f'The probability of the prediction is {probability[0]:.2f}'
    }
