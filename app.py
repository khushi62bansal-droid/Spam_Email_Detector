import streamlit as st
import pickle
import time

# Page config
st.set_page_config(page_title="Spam Detector", page_icon="📧", layout="centered")

# Custom CSS (Beautiful Gradient + Glassmorphism)
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.main {
    background: transparent;
}

.container {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(15px);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    text-align: center;
}

h1 {
    color: white;
    font-weight: 600;
}

textarea {
    border-radius: 12px !important;
    padding: 10px;
}

.stButton>button {
    background: linear-gradient(135deg, #ff6a00, #ee0979);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
}

.result {
    padding: 15px;
    border-radius: 12px;
    margin-top: 15px;
    font-size: 18px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# UI
st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown("# 📧 Spam Email Detector")
st.markdown("<p style='color:white;'>✨ Beautiful AI-powered email checker</p>", unsafe_allow_html=True)

input_text = st.text_area("", height=180, placeholder="💌 Paste your email content here...")

if st.button("🚀 Analyze Now"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter email text!")
    else:
        with st.spinner("Analyzing magic... ✨"):
            time.sleep(1)
            transformed = vectorizer.transform([input_text])
            result = model.predict(transformed)[0]

        if result == 1:
            st.markdown('<div class="result" style="background:#ff4b5c;color:white;">🚨 Spam Email Detected</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result" style="background:#00c9a7;color:white;">✅ Safe Email</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
