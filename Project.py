# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 09:29:53 2025

@author: Admin
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('D:/Admin/Desktop/New_Project/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('D:/Admin/Desktop/New_Project/heart_data.sav', 'rb'))

# Creating side bars for navigation, using option_menu
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                           icons = ['activity', 'hearts'],
                           default_index = 0)


if(selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')

#Creating Columns for input fields:
    col1, col2= st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Enter Glucose level')
    
    with col1:
        BloodPressure = st.text_input('Enter Blood Pressure Level')
        
    with col2:
        SkinThickness = st.text_input('Enter thickness of skin')
        
    with col1:
        Insulin = st.text_input('Enter Insulin Level')
        
    with col2:
        BMI = st.text_input('Enter BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Enter value for Diabetes Pedigree')
    
    with col2:
        Age = st.text_input('Enter your Age')
        
        
# Code for prediction
    diab_diagnosis = ''
    
    
# Creating a button
    if st.button('Diabetes Prediction Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)
        
    
    
    
if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')


#Creating Columns for input fields:
    col1, col2= st.columns(2)
    
    with col1:
        age = st.text_input('Enter your age')
        
    with col2:
        sex = st.text_input('Enter Sex(male = 1, female = 0)')
    
    with col1:
        cp = st.text_input('Enter cp value')
        
    with col2:
        trestbps = st.text_input('Enter trestbps value')
        
    with col1:
        chol = st.text_input('Enter chol value')
        
    with col2:
        fbs = st.text_input('Enter fbs value')
        
    with col1:
        restecg = st.text_input('Enter restecg')
    
    with col2:
        thalach = st.text_input('Enter thalach value')
        
    with col1:
        exang = st.text_input('Enter exang value')
    
    with col2:
        oldpeak = st.text_input('Enter oldpeak value')
        
    with col1:
        slope = st.text_input('Enter slope value')
    
    with col2:
        ca = st.text_input('Enter ca value')
        
    with col1:
        thal = st.text_input('Enter thal value')
        
        
# Code for prediction
    heart_diagnosis = ''
    
    
# Creating a button
    if st.button('Heart Prediction Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having Heart Problem'
        else:
            heart_diagnosis = 'The person is not having Heart Problem'
    st.success(heart_diagnosis)
