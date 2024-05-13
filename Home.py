import logging

import streamlit as st
from PIL import Image

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


st.set_page_config(
    page_title="Data Analytics Strategy",
    layout="wide"
)

st.markdown("<h1 style='text-align: center;'>RETAIL SALES DASHBOARD</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; '>Kanak Sundriyal</h2>", unsafe_allow_html=True)

image = Image.open('./images/SIKA.jpg')
st.image(image)


st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
