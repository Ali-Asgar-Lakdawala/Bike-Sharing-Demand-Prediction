from pydantic import BaseModel

class BikeDemand(BaseModel):
    Seasons_Spring:float
    Seasons_Summer:float
    Seasons_Winter:float
    Holiday_No_Holiday:float
    Functioning_Day_Yes:float
    Hour:float
    Temperature_C:float
    Humidity_per:float
    Wind_speed_m_per_sec:float
    Visibility_10m:float
    Dew_point_temp_c:float
    Solar_Radiation:float
    Rainfall_mm:float
    Snowfall_cm:float
    month:float
    weekdays_weekend:float






