import streamlit as st 
import pandas as pd
from datetime import date
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        opacity: 0.5;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
       
#add_bg_from_local('bg.jpg') 
HomeContainer = st.container()
HomeContainer.markdown("""
    <style>
    .homeContainer {
        background-color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)
HomeContainer.title("SIAPKAH MASYARAKAT INDONESIA AKAN TEKNOLOGI?")
HomeContainer.caption("Lydia Natalia - 'TETRIS PROA : Data Analytics Fast Track' Capstone Project")
HomeContainer.write(date.today().strftime("%A, %d %B %Y"))
