import streamlit as st
import pickle
import time

# Page config
st.set_page_config(page_title="Spam Detector", page_icon="📧", layout="centered")

# Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.main {
    background-color: transparent;
}

.container {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    text-align: center;
}

textarea {
    border-radius: 10px !important;
}

.stButton>button {
    background: linear-gradient(135deg, #43cea2, #185a9d);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

.result {
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# UI Card
st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown("## 📧 Spam Email Detector")
st.caption("AI-powered email classification")

input_text = st.text_area("✉️ Enter your email:", height=150, placeholder="Paste email content...")

if st.button("🔍 Analyze Email"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter email text!")
    else:
        with st.spinner("Analyzing... ⏳"):
            time.sleep(1)
            transformed = vectorizer.transform([input_text])
            result = model.predict(transformed)[0]

        if result == 1:
            st.markdown('<div class="result" style="background:#ffe6e6;color:#cc0000;">🚨 Spam Email</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result" style="background:#e6ffe6;color:#006600;">✅ Not Spam</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
