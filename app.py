import streamlit as st
import pickle
import time

st.set_page_config(page_title="Spam Detector", page_icon="📧", layout="wide")


# 🌿 SOFT MINIMAL UI (CALM COLORS)
st.markdown("""
<style>
    /* 1. THE NUCLEAR FIX FOR THE WHITE HEADER */
    header, [data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
    }

    /* 2. REMOVE THE TOP DECORATION LINE */
    [data-testid="stDecoration"] {
        display: none !important;
    }

    /* 3. REMOVE EXTRA SPACE AT THE TOP */
    .stAppViewBlockContainer {
        padding-top: 0rem !important;
    }
    .block-container {
        padding-top: 0rem !important;
    }

    /* SOFT BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #e3f2fd, #fce4ec);
    }

    /* CENTER CARD */
    .center-box {
        max-width: 600px;
        margin: auto;
        margin-top: 5vh; 
        background: white;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
    }

    /* TITLE */
    .title {
        font-size: 30px;
        font-weight: 600;
        color: #333;
    }

    /* SUBTEXT */
    .subtitle {
        color: #666;
        font-size: 14px;
        margin-bottom: 15px;
    }

    /* TEXTAREA */
    textarea {
        border-radius: 10px !important;
        border: 1px solid #ddd !important;
    }

    /* BUTTON (SOFT GRADIENT) */
    .stButton>button {
        background: linear-gradient(135deg, #89f7fe, #66a6ff) !important;
        color: #fff !important;
        border-radius: 10px;
        height: 42px;
        width: 100%;
        font-size: 15px;
        border: none;
        margin-top: 10px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.03);
    }
</style>
""", unsafe_allow_html=True)


# Load model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# UI
st.markdown('<div class="center-box">', unsafe_allow_html=True)

st.markdown('<div class="title">📧 Spam Email Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Check whether your email is spam or not!! </div>', unsafe_allow_html=True)

text = st.text_area("", height=150, placeholder="Paste your content here...")

if st.button("🔍 Predict"):
    if text.strip() == "":
        st.warning("⚠️ Enter email text")
    else:
        with st.spinner("Checking..."):
            time.sleep(1)
            result = model.predict(vectorizer.transform([text]))[0]

        if result == 1:
            st.error("🚨 Spam Email")
        else:
            st.success("✅ Safe Email")

st.markdown('</div>', unsafe_allow_html=True)
