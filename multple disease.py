import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabities_model = pickle.load(open("C:/Users/shrey/OneDrive/Desktop/diabetes_model.pkl", 'rb'))
heart_model = pickle.load(open("C:/Users/shrey/OneDrive/Desktop/Heart_model.pkl", 'rb'))

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",
                           ["Diabetes Prediction", "Heart Disease Prediction"],
                           icons=['activity', 'heart'],
                           default_index=0)

if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction")
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col1:
        BloodPressure = st.text_input("Blood Pressure Value")
    with col2:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col1:
        Insulin = st.text_input("Insulin Level")
    with col2:
        Age = st.text_input("Age of the Person")
    with col1:
        BMI = st.text_input("BMI Value")
    with col2:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")

    diab_diagnosis = ''

    if st.button("Diabetes Test Result"):
        try:
            input_data = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(Age),
                float(BMI), float(DiabetesPedigreeFunction)
            ]
            diab_model = diabities_model.predict([input_data])
            if diab_model[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
            st.success(diab_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")
    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col1:
        cp = st.text_input("Chest Pain Type")
    with col2:
        trestbps = st.text_input("Resting Blood Pressure")
    with col1:
        chol = st.text_input("Serum Cholesterol")
    with col2:
        fbs = st.text_input("Fasting Blood Sugar")
    with col1:
        restecg = st.text_input("Resting Electrocardiographic Results")
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")
    with col1:
        exang = st.text_input("Exercise Induced Angina")
    with col2:
        oldpeak = st.text_input("Oldpeak")
    with col1:
        slope = st.text_input("Slope of the Peak Exercise ST Segment")
    with col2:
        ca = st.text_input("Number of Major Vessels Colored by Fluoroscopy")    
    with col1:
        thal = st.text_input("Thalassemia")

    heart_diagnosis = ''
    if st.button("Heart Disease Test Result"):
        try:
            input_data = [
                float(age), float(sex), float(cp), float(trestbps), float(chol),
                float(fbs), float(restecg), float(thalach), float(exang),
                float(oldpeak), float(slope), float(ca), float(thal)
            ]
            heart_pred = heart_model.predict([input_data])
            if heart_pred[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have heart disease'
            st.success(heart_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")


