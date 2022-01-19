import numpy as np
import pickle
import pandas as pd
import streamlit as st 

pickle_in= open('finalized_model.pkl','rb')
regressor=pickle.load(pickle_in)

def index():
    return {'message': 'Hello, World'}

def predict_bike_number(Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature_C,Humidity_per
                                    ,Wind_speed_m_per_sec,Visibility_10m,Dew_point_temp_c,Solar_Radiation,Rainfall_mm,Snowfall_cm,month,weekdays_weekend):

    prediction = regressor.predict([[Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature_C,Humidity_per
                                    ,Wind_speed_m_per_sec,Visibility_10m,Dew_point_temp_c,Solar_Radiation,Rainfall_mm,Snowfall_cm,month,weekdays_weekend]])

    return {'prediction': prediction}

    

def main ():
    Seasons = st.selectbox("Seasons",['Spring','Summer','Winter'])
    if Seasons=='Spring':
        Seasons_Spring = 1
        Seasons_Summer = 0
        Seasons_Winter = 0
    elif Seasons=='Summer':
        Seasons_Spring = 0
        Seasons_Summer = 1
        Seasons_Winter = 0
    else:
        Seasons_Spring = 0
        Seasons_Summer = 0
        Seasons_Winter = 1

    Holiday_No_Holiday = st.number_input("Holiday_No_Holiday",value =1)
    Functioning_Day_Yes = st.number_input("Functioning_Day_Yes",value =1)
    Hour = st.number_input("Hour",value =15,max_value=23,min_value=1)
    Temperature_C = st.number_input("Temperature_C",value =16)
    Humidity_per = st.number_input("Humidity_per",value =14)
    Wind_speed_m_per_sec = st.number_input("Wind_speed_m_per_sec",value =2.2)
    Visibility_10m = st.number_input("Visibility_10m",value =1828)
    Dew_point_temp_c = st.number_input("Dew_point_temp_c",value =15)
    Solar_Radiation = st.number_input("Solar_Radiation",value =2.33)
    Rainfall_mm = st.number_input("Rainfall_mm",value =0)
    Snowfall_cm = st.number_input("Snowfall_cm",value =0)
    month = st.number_input("month",value =3,max_value=12,min_value=1)
    weekend = st.selectbox("weekend",['yes','no'])
    if weekend=='yes':
        weekdays_weekend = 1
    else :
        weekdays_weekend = 0

    if st.button("Predict"):
        result=predict_bike_number(Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature_C,Humidity_per
                                    ,Wind_speed_m_per_sec,Visibility_10m,Dew_point_temp_c,Solar_Radiation,Rainfall_mm,Snowfall_cm,month,weekdays_weekend)    
        st.success('The output is {}'.format(result))



if __name__ == '__main__':
    main()