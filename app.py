import streamlit as st
import pickle
import time

st.set_page_config(page_title="Spam Detector", page_icon="📧", layout="wide")



st.markdown("""
<style>
    
    header, [data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
    }

   
    [data-testid="stDecoration"] {
        display: none !important;
    }

   
    .stAppViewBlockContainer {
        padding-top: 0rem !important;
    }
    .block-container {
        padding-top: 0rem !important;
    }

  
    .stApp {
        background: linear-gradient(135deg, #e3f2fd, #fce4ec);
    }

   
    .center-box {
        max-width: 600px;
        margin: auto;
        margin-top: 0vh; 
        background: white;
        opacity:0;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
    }

 
    .title {
        font-size: 30px;
        font-weight: 600;
        color: #333;
    }

    
    .subtitle {
        color: #666;
        font-size: 14px;
        margin-bottom: 15px;
    }

   
    textarea {
        border-radius: 10px !important;
        border: 1px solid #ddd !important;
    }

 
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



model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))


st.markdown('<div class="center-box">', unsafe_allow_html=True)

st.markdown('<div class="title">📧 Spam Email Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Check whether your email is spam or not!! </div>', unsafe_allow_html=True)

text = st.text_area("", height=150 , width = 1300, placeholder="Paste your content here...")

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
