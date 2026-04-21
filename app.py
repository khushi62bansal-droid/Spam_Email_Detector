import streamlit as st
import pickle
import time

st.set_page_config(page_title="Spam Detector", page_icon="📧", layout="wide")

# 🌿 SOFT MINIMAL UI (CALM COLORS)
st.markdown("""
<style>

/* 🚫 REMOVE HEADER + TOOLBAR COMPLETELY */
header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stHeader"] {display: none;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}

/* REMOVE EXTRA SPACE */
.block-container {
    padding-top: 0rem;
}

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #e3f2fd, #fce4ec);
}

/* CENTER CARD */
.center-box {
    max-width: 600px;
    margin: auto;
    margin-top: 60px;
    background: white;
    padding: 30px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
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

/* TEXTAREA FIX */
.stTextArea textarea {
    border-radius: 10px !important;
    border: 1px solid #ddd !important;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #89f7fe, #66a6ff);
    color: #fff;
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
