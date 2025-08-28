import streamlit as st
import pickle
import numpy as np

# تحميل الموديل
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🧠 Decision Tree Classifier")
st.write("تجربة نموذج التصنيف المدرب")

# إدخال الخصائص من المستخدم
st.sidebar.header("ادخل البيانات:")

# مثال: لو عندك 4 فيتشرز زي iris dataset
feature1 = st.sidebar.number_input("Feature 1", value=0.0)
feature2 = st.sidebar.number_input("Feature 2", value=0.0)
feature3 = st.sidebar.number_input("Feature 3", value=0.0)
feature4 = st.sidebar.number_input("Feature 4", value=0.0)

features = np.array([[feature1, feature2, feature3, feature4]])

if st.button("تنبؤ"):
    prediction = model.predict(features)
    st.success(f"🎯 النتيجة: {prediction[0]}")
