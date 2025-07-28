import streamlit as st
import numpy as np
import joblib
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(base_dir, 'model.pkl'))
columns = joblib.load(os.path.join(base_dir, 'columns.pkl'))


st.title("🏥 Medical Charges Predictor")

age = st.slider("Age", 18, 100, 30)
bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
children = st.selectbox("Number of Children", [0, 1, 2, 3, 4, 5])
sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])


sex_male = 1 if sex == "male" else 0
smoker_yes = 1 if smoker == "yes" else 0

region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0


input_data = np.array([[age, bmi, children, sex_male, smoker_yes,
                        region_northwest, region_southeast, region_southwest]])

if st.button("Predict 💰 Medical Charges"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Charges: $ {prediction[0]:,.2f}")
