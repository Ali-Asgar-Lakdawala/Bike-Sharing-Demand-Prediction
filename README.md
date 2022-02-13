# Bike-Sharing-Demand-Prediction

## Introduction
Seoul Bike is providing the city with a stable supply of rental bikes. It becomes a major concern to keep users satisfied. The crucial part is the prediction of bike count rents at each hour for a stable supply of rental bikes. It is important to make the rental bike available and accessible to the public, as it provides many alternatives to commuters in metropolises. There are a lot of advantages to bike rental, it is convenient because it permits people not to keep the bike all day long, whether it is at work or at school. Furthermore, it is the healthiest way to travel and it has many environmental benefits.

The studied dataset contains weather information which are the features (Temperature, Humidity, Wind speed, Visibility, Dew point, Solar radiation, Snowfall, Rainfall), the target is the number of bikes rented per hour and date information. The dataset presents the company's data between December the 1st of 2017 and finishes one year later.

This study shows that the rents of bikes are influenced by a lot of features. In this study, we understood that many people usually and mainly rent bikes during the weekdays, so we supposed that the main use is to go to school or work. There are also many conditions that contribute to the variation of the number of rents like the day of the week, the time of the day, and weather conditions as there are more rents during spring and summer. And as we expected more people are set to rent bikes when the weather is favorable.
 
We started with loading the data, then we did Exploratory Data Analysis (EDA), null values treatment, feature selection, encoding of categorical columns, and then model building. In all of these models, our accuracy ranges from 56% to 91%, which can be said to be good for such a large dataset. This performance could be due to various reasons like the proper pattern of data, large data, or because of the relevant features.
 
We performed variable importance analysis to find the most significant variables for all the models developed with the given data sets. We are getting the best results from CatBoost and LightGBM.

## Problem Statement
Currently, Rental bikes are introduced in many urban cities for the enhancement of mobility comfort. It is important to make the rental bike available and accessible to the public at the right time as it lessens the waiting time. Eventually, providing the city with a stable supply of rental bikes becomes a major concern. The crucial part is the prediction of bike count required at each hour for the stable supply of rental bikes.

## Models used 
* Linear Regression
* Polynomial Regression
* KNN
* Random Forest Regression
* Gradient Boosting Regression
* XGBoost Regression
* CatBoost Regression
* LightGBM Regression

## Deployment of Streamlit WebApp in Heroku and Streamlit

We have created front-end using Streamlit for the webapp. whose deployments and github link are as follows 

| Website | Link |
| ------ | ------ |
| Github | https://github.com/Ali-Asgar-Lakdawala/ML-deployment |
| Heroku | https://my-ml-deployments.herokuapp.com/ |
| Streamlit | https://share.streamlit.io/ali-asgar-lakdawala/ml-deployment/main/app.py |
## Conclusion

* In all of these models, our adjusted R2 revolves in the range of 56 to 91%..with the best fit model as LightGBM and Catboost model 
* We were successfull in deploying the strealit app on heruko .














