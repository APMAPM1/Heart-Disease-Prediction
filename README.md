# Heart-Disease-Prediction

World Health Organization has estimated 12 million deaths occur worldwide, every year due to Heart diseases. Half the deaths in the United States and other developed countries are due to cardio vascular diseases. The early prognosis of cardiovascular diseases can aid in making decisions on lifestyle changes in high risk patients and in turn reduce the complications. 

## Dataset Description

I have used HeartDiseaseTrain-Test.csv

This is a multivariate type of dataset which means providing or involving a variety of separate mathematical or statistical variables, multivariate numerical data analysis. It is composed of 14 attributes which are age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise-induced angina, oldpeak - ST depression induced by exercise relative to rest, the slope of the peak exercise ST segment, number of major vessels and Thalassemia. This database includes 76 attributes, but all published studies relate to the use of a subset of 14 of them. The Cleveland database is the only one used by ML researchers to date. One of the major tasks on this dataset is to predict based on the given attributes of a patient that whether that particular person has heart disease or not and other is the experimental task to diagnose and find out various insights from this dataset which could help in understanding the problem more.

**Data Dictionary**

**age:** Age in years </br>
**sex:** male : 1 female : 0 </br>
**chest_pain_type:** 
- Value 1: typical angina
- Value 2: atypical angina
- Value 3: non-anginal pain
- Value 4: asymptomatic

**resting_blood_pressure:** (in mm Hg on admission to the hospital) </br>
**cholestoral:** serum cholestoral in mg/dl </br>
**fasting_blood_sugar:** (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false) </br>
**rest_ecg:** resting electrocardiographic results
- Value 0: normal
- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria

**Max_heart_rate:**	thalach - maximum heart rate achieved </br>
**exercise_induced_angina:** (1 = yes; 0 = no) Angina is chest pain or discomfort caused when your heart muscle doesn't get enough oxygen-rich blood. It may feel like pressure or squeezing in your chest. </br>
**oldpeak:** ST depression induced by exercise relative to rest </br>
**slope:** the slope of the peak exercise ST segment
- Value 1: upsloping
- Value 2: flat
- Value 3: downsloping

**vessels_colored_by_flourosopy:** number of major vessels (0-3) colored by flourosopy </br>
**thalassemia:** A blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect) </br>
**target:** 0 No Heart disease 1 Heart disease
