# Bike-Sharing-Demand-Prediction
## Introduction
Seoul Bike is providing the city with a stable supply of rental bikes. It becomes a major concern to keep users satisfied. The crucial part is the prediction of bike count rents at each hour for a stable supply of rental bikes. It is important to make the rental bike available and accessible to the public, as it provides many alternatives to commuters in metropolises. There are a lot of advantages to bike rental, it is convenient because it permits people not to keep the bike all day long, whether it is at work or school. Furthermore, it is the healthiest way to travel and it has many environmental benefits.

The studied dataset contains weather information which are the features (Temperature, Humidity, Wind speed, Visibility, Dew point, Solar radiation, Snowfall, Rainfall), the target is the number of bikes rented per hour and date information. The dataset presents the company's data between December the 1st of 2017 and finishes one year later.

This study shows that the rents of bikes are influenced by a lot of features. We understood that many people usually and mainly rent bikes during the weekdays, so we supposed that the main use is to go to school or work. Many conditions contribute to the variation of the number of rents like the day of the week, the time of the day, and weather conditions as there are more rents during spring and summer. And as we expected more people are set to rent bikes when the weather is favorable.

We started with loading the data, then we did Exploratory Data Analysis (EDA), null values treatment, feature selection, encoding of categorical columns, and then model building. In all of these models, our accuracy ranges from 56% to 91%, which can be said to be good for such a large dataset. This performance could be due to various reasons like the proper pattern of data, large data, or because of the relevant features.

We performed variable importance analysis to find the most significant variables for all the models developed with the given data sets. We are getting the best results from CatBoost and LightGBM.

## Problem Statement
Currently, Rental bikes are introduced in many urban cities for the enhancement of mobility comfort. It is important to make the rental bike available and accessible to the public at the right time as it lessens the waiting time. Eventually, providing the city with a stable supply of rental bikes becomes a major concern. The crucial part is the prediction of bike count required at each hour for the stable supply of rental bikes.

## Data Description
The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rented per hour, and date information.
* Attribute Information:
* Date : year-month-day
* Rented Bike count - Count of bikes rented at each hour
* Hour - Hour of he day
* Temperature-Temperature in Celsius
* Humidity - %
* Windspeed - m/s
* Visibility - 10m
* Dew point temperature - Celsius
* Solar radiation - MJ/m2
* Rainfall - mm
* Snowfall - cm
* Seasons - Winter, Spring, Summer, Autumn
* Holiday - Holiday/No holiday
* Functional Day - NoFunc(Non Functional Hours), Fun(Functional hours)

## Steps involved:

### Exploratory Data Analysis
After loading the dataset we compared our target variable that is the Rented Bike count Type with other independent variables. This process helped us figure out various aspects and relationships among the dependent and the independent variables. It gave us a better idea of which feature behaves in which manner compared to the dependent variable.

![](https://github.com/rahul-kr-soni/Bike-Sharing-Demand-Prediction/blob/main/Performance_matrix/Screenshot%202022-02-21%20at%2011.08.18%20PM.png)

The conclusion from above graph:

* High rise of Rented Bikes from 8:00 a.m to 9:00 p.m means people prefer rented bike during rush hour.

* We can clearly see that demand rises most at 8 a.m and 6:00 p.m so we can say that during office opening and closing time there is much high demand

### Null values Treatment
Our data set didn’t have any null values to be treated.

### Feature engineering 
Created new columns based on the date and other feature such as month, weekend etc 

### Encoding of categorical columns
We used One Hot Encoding(converting to dummy variables) to produce binary integers of 0 and 1 to encode our categorical features because categorical features that are in string format cannot be understood by the machine and needs to be converted to the numerical format.

![](https://github.com/Ali-Asgar-Lakdawala/readme_projects/blob/main/bike/77.png)
### Feature Selection
In these steps, we used correlation, VIF analysis to check the results of each feature to remove multicollinearity before apply lenaer regression
### Standardization of features
Our main motive through this step was to scale our data into a uniform format that would allow us to utilize the data in a better way while performing fitting and applying different algorithms to it.
The basic goal was to enforce a level of consistency or uniformity to certain practices or operations within the selected environment.

### Fitting different models
For modeling, we tried various classification algorithms like:
* Linear regression with regularization(lasso,ridge,elastic_net)
* Polynomial Regression
* KNN
* Random Forest Regression
* Gradient Boosting Regression
* XGBoost Regression
* CatBoost Regression
* Light GBM

### Tuning the hyperparameters for better accuracy
Tuning the hyperparameters of respective algorithms is necessary for getting better accuracy and to avoid overfitting in the case of tree-based models like Random Forest Classifier and XGBoost classifier.

### Features Explainability 
We have applied SHAP on the XGBoost and CatBoost model to determine the features that were most important while predicting an instance
And also build a feature importance graph to find out which features were important and which were redundant in a model

### Performance Metrics
![](https://github.com/rahul-kr-soni/Bike-Sharing-Demand-Prediction/blob/main/Performance_matrix/Screenshot%202022-02-21%20at%2010.35.03%20PM.png)
![](https://github.com/rahul-kr-soni/Bike-Sharing-Demand-Prediction/blob/main/Performance_matrix/Screenshot%202022-02-21%20at%2011.00.49%20PM.png)


## Deployment of Streamlit WebApp in Heroku and Streamlit

We have created front-end using Streamlit for the webapp. whose deployments and github link are as follows 

| Website | Link |
| ------ | ------ |
| Github | https://github.com/Ali-Asgar-Lakdawala/my-ml-deployment-2 |
| Heroku | https://my-ml-deployment-2.herokuapp.com/ |
| Streamlit | https://share.streamlit.io/ali-asgar-lakdawala/my-ml-deployment-2/main/app.py|

## Conclusion

* In all of these models, our adjusted R2 revolves in the range of 56 to 91%.With the best fit model as LightGBM and Catboost model 
* We were successfull in deploying the strealit app on heruko .














