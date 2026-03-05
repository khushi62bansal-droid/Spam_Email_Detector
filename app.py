import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title(" Spam Email Detector")

input_text = st.text_area("Enter Email Text")

if st.button("Predict"):
    transformed = vectorizer.transform([input_text])
    result = model.predict(transformed)[0]

    if result == 1:
        st.error("🚨 Spam Email")
    else:
        st.success("✅ Not Spam")

