import streamlit as st
import pickle
import numpy as np

# تحميل الموديل
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌸 Iris Flower Classifier")
st.write("أدخل القيم وتوقع نوع الزهرة")

# إدخال القيم من المستخدم
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width  = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width  = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)

if st.button("توقع"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    
    classes = ["Setosa", "Versicolor", "Virginica"]
    st.success(f"🌼 التوقع: {classes[prediction[0]]}")
