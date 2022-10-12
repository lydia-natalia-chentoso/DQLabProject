import streamlit as st 
import pandas as pd
from datetime import date
import base64
import numpy as np
import altair as alt

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        opacity: 1;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
       
st.set_page_config(layout='wide')
add_bg_from_local('Source/Image/bg1.jpg') 
HomeContainer = st.container()
HomeContainer.title("SIAPKAH MASYARAKAT INDONESIA AKAN TEKNOLOGI?")
HomeContainer.caption("Lydia Natalia - 'TETRIS PROA : Data Analytics Fast Track' Capstone Project")
HomeContainer.write(date.today().strftime("%A, %d %B %Y"))

st.write('<div style = "background-color:white;color:black; padding:15px;">Dunia telah memasuki era Revolusi Industri 4.0 yang sangat berkaitan erat dengan perkembangan teknologi yang sangat pesat, dimana pekerjaan manusia semakin dimudahkan atau bahkan digantikan oleh berbagai macam teknologi-teknologi canggih seperti Robot Otonom (<i>Autonomous Robot</i>), Kendaraan Pintar, <i>Internet of Things</i> (IoT), Kecerdasan Buatan (<i>Artificial Intelligence</i>), <i>Big Data</i>, <i>Augmented Reality</i> (AR) dan lain sebagainya.<br><br> Pada era ini lah, masyarakat ditantang untuk sadar diri dan terus haus untuk mengembangkan keterampilan diri terutama dibidang teknologi informasi dan komputer agar tidak ketinggalan zaman / gagap teknologi karena hampir di semua aspek kehidupan masyarakat bergantung dan terintegrasi melalui teknologi digital dan internet.<br><br> Pandemi Covid-19 yang menghantam Indonesia, tak bisa dipungkiri memaksa masyarakat untuk dapat bertumpuh pada teknologi karena selama pandemi berlangsung, sektor yang masih kuat bertahan dan tetap berkembang adalah sektor industri teknologi informasi dan komunikasi. Dan selama pandemi, konsumsi teknologi digital melalui internet terus meningkat dan dampaknya semakin signifikan dan jelas disetiap aspek kehidupan masyarakat.</div>', unsafe_allow_html=True)
st.write('')
col1, col2 = st.columns(2)
df = pd.read_csv("Source/Data/Persentase Rumah Tangga yang Pernah Mengakses Internet dalam 3 Bulan Terakhir Menurut Media Akses.csv")
df = df.melt('Media', var_name='Tahun', value_name='value')
chart = alt.Chart(df).mark_line().encode(
  x=alt.X('Tahun:N'),
  y=alt.Y('value:Q'),
  color=alt.Color("Media:N")
).properties(title="Persentase Rumah Tangga yang Pernah Mengakses Internet",height=300)
col1.altair_chart(chart, use_container_width=True)
col1.caption("Sumber: BPS, Survei Sosial Ekonomi Nasional (Susenas). Catatan: - Pembagi adalah total rumah tangga yang mengakses internet")

col2.write('<div style = "background-color:white;color:black; padding:15px;">Beberapa tahun terakhir, masyarakat yang mengakses internet didominasi oleh penggunaan media telepon seluler dan dapat dilihat penggunaan media telepon seluler terus meningkat setiap tahunnya. Bila dibandingkan dengan media lainnya, jelas signifikan berbeda, karena media lain mengalami penurun setiap tahunnya.<br> Tentunya dengan dominasi tersebut menyatakan bahwa telepon seluler adalah media terbesar yang digunakan oleh masyarakat dalam mengakses internet. <b>Tetapi yang menjadi pertanyaan besar, apakah seluruh daerah di Indonesia memiliki sinyal untuk mengakses internet?</b></div>', unsafe_allow_html=True)
#st.bar_chart(data=None, *, x=None, y=None, width=0, height=0, use_container_width=True)