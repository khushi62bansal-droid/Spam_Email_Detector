import streamlit as st
import pickle

# Page config
st.set_page_config(page_title="Spam Detector", page_icon="📧", layout="centered")

# Custom CSS for better UI
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.stTextArea textarea {
    border-radius: 10px;
    padding: 12px;
    font-size: 16px;
}
.stButton button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
.stButton button:hover {
    background-color: #45a049;
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
    text-align: center;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Header
st.markdown("""
<h1 style='text-align: center;'>📧 Spam Email Detector</h1>
<p style='text-align: center; color: gray;'>Detect whether an email is Spam or Not Spam using Machine Learning</p>
""", unsafe_allow_html=True)

# Input box
input_text = st.text_area("✉️ Enter your email text here:", height=200, placeholder="Paste your email content here...")

# Predict button
if st.button("🔍 Check Email"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter some email text!")
    else:
        transformed = vectorizer.transform([input_text])
        result = model.predict(transformed)[0]

        if result == 1:
            st.markdown("<div class='result-box' style='background-color:#ffe6e6; color:#cc0000;'>🚨 This is a SPAM Email</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-box' style='background-color:#e6ffe6; color:#006600;'>✅ This is NOT a Spam Email</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<hr>
<p style='text-align: center; font-size: 14px; color: gray;'>Built with ❤️ using Streamlit</p>
""", unsafe_allow_html=True)

