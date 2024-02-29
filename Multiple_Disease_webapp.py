# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 01:54:46 2024

@author: gurav
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models

diabeteas_model = pickle.load(open('D:/Multiple Diseases Prediction/Diabeteas_model.sav'))

heart_model = pickle.load(open('D:/Multiple Diseases Prediction/heart_model.sav'))

breast_cancer_model = pickle.load(open('D:/Multiple Diseases Prediction/breast_cancer_model.sav'))


#sidebar for navigate
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabeteas Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction'],
                           icons = ['activity','heart','lungs'],
                           default_index = 0)
    

#diabetes prediction page
if (selected == 'Diabeteas Prediction'):
    
    #page title
    st.title('Diabeteas Prediction using ML')
    
    #column for input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')    
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')   
    
    with col1:
       SkinThickness = st.text_input('Skin Thickness Value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI Vlue')
    
    with col1:
       DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
   
    with col2:
        Age = st.text_input('Age of the person')
    
    
    #Pregnancies = st.text_input('Number of Pregnancies')
    #Glucose = st.text_input('Glucose Level')
    #BloodPressure = st.text_input('Blood Pressure Value')
    #SkinThickness = st.text_input('Skin Thickness Value')
    #Insulin = st.text_input('Insulin Level')
    #BMI = st.text_input('BMI Vlue')
    #DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    #Age = st.text_input('Age of the person')
    
    
    #code for prediction
    diab_diagnosis = ''
    
    
    #creting button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabeteas_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is not Diabetic'
    st.success(diab_diagnosis)
    
    
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    #column for input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        age = st.text_input('Age of the person')
    
    with col2:
        sex = st.text_input('Gender of the perdon')    
    
    with col3:
        cp = st.text_input('CP Value')   
    
    with col4:
       trestbps = st.text_input('Trestbps Value')
    
    with col5:
        chol = st.text_input('Chol Level')
        
    with col1:
        fbs = st.text_input('fbs Vlue')
    
    with col2:
       restecg = st.text_input('restecg value')
   
    with col3:
        thalach = st.text_input('thalach Value')
    
    with col4:
        exang = st.text_input('exang Value')
    
    with col5:
        oldpeak = st.text_input('oldpeak Value')
    
    with col1:
        slope = st.text_input('slpoe Value')
        
    with col2:
        ca = st.text_input('ca Value')
        
    with col3:
         thal = st.text_input('tha Value')    
             
    #code for prediction
    heart_diagnosis = ''
    
    
    #creting button for prediction
    
    if st.button('Heart Test Result'):
        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person has healthy heart'
    st.success(heart_diagnosis)
    
if (selected == 'Breast Cancer Prediction'):
    
    #page title
    st.title('Breast Cancer Prediction using ML')
    
    #column for input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        age = st.text_input('Age of the person')
    
    with col2:
        sex = st.text_input('Gender of the perdon')    
    
    with col3:
        cp = st.text_input('CP Value')   
    
    with col4:
       trestbps = st.text_input('Trestbps Value')
    
    with col5:
        chol = st.text_input('Chol Level')
        
    with col1:
        fbs = st.text_input('fbs Value')
    
    with col2:
       restecg = st.text_input('restecg value')
   
    with col3:
        thalach = st.text_input('thalach Value')
    
    with col4:
        exang = st.text_input('exang Value')
    
    with col5:
        oldpeak = st.text_input('oldpeak Value')
    
    with col1:
        slope = st.text_input('slpoe Value')
        
    with col2:
        ca = st.text_input('ca Value')
        
    with col3:
         thal = st.text_input('tha Value')    
             
    #code for prediction
    Breast_cancer_diagnosis = ''
    
    
    #creting button for prediction
    
    if st.button('Breast Test Result'):
        Breast_Cancer_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if (Breast_Cancer_prediction[0]==1):
            Breast_Cancer_diagnosis = 'The person has Breast Cancer'
        else:
            heart_diagnosis = 'The person has not Breast Cancer'
    st.success(Breast_Cancer_diagnosis)
