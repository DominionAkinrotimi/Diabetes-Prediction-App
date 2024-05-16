import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('diabetes_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the prediction function
def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age):
    features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
    prediction = model.predict(features)
    return prediction

# Streamlit interface
st.title('Diabetes Prediction')

# Add input fields
pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=0)
glucose = st.number_input('Glucose', min_value=0, max_value=200, value=100)
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=150, value=70)
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, value=20)
insulin = st.number_input('Insulin', min_value=0, max_value=900, value=0)
bmi = st.number_input('BMI', min_value=0, max_value=70, value=25)
diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5,
                                             help='A numerical score representing the likelihood of having diabetes based on family history.')
age = st.number_input('Age', min_value=0, max_value=120, value=30)

# Make prediction on button click
if st.button('Predict'):
    prediction = predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)
    if prediction[0] == 1:
        st.write('Result: Positive for Diabetes')
    else:
        st.write('Result: Negative for Diabetes')
