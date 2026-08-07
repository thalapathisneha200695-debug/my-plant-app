import streamlit as st
import google.generativeai as genai
from PIL import Image

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

st.set_page_config(page_title="Ultra Bio-Analyzer AI", page_icon="🔬")
st.title("🔬 Ultra Bio-Analyzer & Genomic AI")

uploaded_file = st.file_uploader("செடியின் படத்தைத் தேர்ந்தெடுக்கவும்...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='பதிவேற்றப்பட்ட மாதிரி', width=300)
    
    if st.button('அல்ட்ரா பகுப்பாய்வைத் தொடங்கு'):
        st.info("🔍 பகுப்பாய்வு நடக்கிறது...")
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            prompt = "Analyze this plant image and provide detailed info in Tamil regarding chemical compounds, benefits, harms, and medical uses."
            response = model.generate_content([prompt, image])
            
            st.subheader("📊 பகுப்பாய்வு முடிவுகள்:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"பிழை ஏற்பட்டது: {e}")
