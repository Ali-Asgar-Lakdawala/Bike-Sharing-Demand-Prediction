import uvicorn
from fastapi import FastAPI
from bikedemand import BikeDemand
import pickle

app=FastAPI()
pickle_in= open('finalized_model.pkl','rb')
regressor=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

@app.post('/predict')
def predict_banknote(data:BikeDemand):
    data = data.dict()
    Seasons_Spring=data['Seasons_Spring']
    Seasons_Summer=data['Seasons_Summer']
    Seasons_Winter=data['Seasons_Winter']
    Holiday_No_Holiday=data['Holiday_No_Holiday']
    Functioning_Day_Yes=data['Functioning_Day_Yes']
    Hour=data['Hour']
    Temperature_C=data['Temperature_C']
    Humidity_per=data['Humidity_per']
    Wind_speed_m_per_sec=data['Wind_speed_m_per_sec']
    Visibility_10m=data['Visibility_10m']
    Dew_point_temp_c=data['Dew_point_temp_c']
    Solar_Radiation=data['Solar_Radiation']
    Rainfall_mm=data['Rainfall_mm']
    Snowfall_cm=data['Snowfall_cm']
    month=data['month']
    weekdays_weekend=data['weekdays_weekend']

   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = regressor.predict([[Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature_C,Humidity_per
                                    ,Wind_speed_m_per_sec,Visibility_10m,Dew_point_temp_c,Solar_Radiation,Rainfall_mm,Snowfall_cm,month,weekdays_weekend]])

    return {'prediction': prediction}
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)