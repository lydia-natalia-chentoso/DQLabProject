import streamlit as st 
import pandas as pd
from datetime import date
import base64
import numpy as np
import altair as alt
#from sklearn.cluster import KMeans

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
add_bg_from_local('Source/Image/bg1c.jpg') 
HomeContainer = st.container()
HomeContainer.title("SIAPKAH INDONESIA AKAN TEKNOLOGI?")
HomeContainer.caption("Lydia Natalia - 'TETRIS PROA : Data Analytics Fast Track' Capstone Project")
HomeContainer.write(date.today().strftime("%A, %d %B %Y"))

st.write('<div style = "background-color:white;color:black; padding:15px;">Dunia telah memasuki era Revolusi Industri 4.0 yang sangat berkaitan erat dengan perkembangan teknologi yang sangat pesat, dimana pekerjaan manusia semakin dimudahkan atau bahkan digantikan oleh berbagai macam teknologi-teknologi canggih seperti Robot Otonom (<i>Autonomous Robot</i>), Kendaraan Pintar, <i>Internet of Things</i> (IoT), Kecerdasan Buatan (<i>Artificial Intelligence</i>), <i>Big Data</i>, <i>Augmented Reality</i> (AR) dan lain sebagainya.<br><br> Pada era ini lah, masyarakat ditantang untuk sadar diri dan terus haus untuk mengembangkan keterampilan diri terutama dibidang teknologi informasi dan komputer agar tidak ketinggalan zaman / gagap teknologi karena hampir di semua aspek kehidupan masyarakat bergantung dan terintegrasi melalui teknologi digital dan internet.<br><br> Pandemi Covid-19 yang menghantam Indonesia, tak bisa dipungkiri memaksa masyarakat untuk dapat bertumpuh pada teknologi karena selama pandemi berlangsung, sektor yang masih kuat bertahan dan tetap berkembang adalah sektor industri teknologi informasi dan komunikasi. Dan selama pandemi, konsumsi teknologi digital melalui internet terus meningkat dan dampaknya semakin signifikan dan jelas disetiap aspek kehidupan masyarakat.</div>', unsafe_allow_html=True)
st.write('')

col1, col2 = st.columns(2)
#df = pd.read_excel("Source/Data/Persentase Rumah Tangga yang Pernah Mengakses Internet dalam 3 Bulan Terakhir Menurut Media Akses.xlsx")
#df = df.melt('Media', var_name='Tahun', value_name='value')
#chart = alt.Chart(df).mark_line(point=True).encode(
#  x=alt.X('Tahun:N'),
#  y=alt.Y('value:Q'),
#  color=alt.Color("Media:N"),
#tooltip=['Media', 'Tahun', 'value']
#).properties(title="Persentase Rumah Tangga yang Pernah Mengakses Internet").interactive()
#col1.altair_chart(chart, use_container_width=True)
#col1.caption("Sumber: BPS, Survei Sosial Ekonomi Nasional (Susenas). Catatan: - Pembagi adalah total rumah tangga yang mengakses internet")

col1.image("Source/Image/inet bps.jfif")
col1.caption("Sumber : https://jakarta.bps.go.id/backend/images/Internet-2020-ind.JPG")

#col2.write('<div style = "background-color:white;color:black; padding:15px;">Beberapa tahun terakhir, masyarakat yang mengakses internet didominasi oleh penggunaan media telepon seluler dan dapat dilihat penggunaan media telepon seluler terus meningkat setiap tahunnya. Bila dibandingkan dengan media lainnya, jelas signifikan berbeda, karena media lain mengalami penurun setiap tahunnya.<br> Tentunya dengan dominasi tersebut menyatakan bahwa telepon seluler adalah media terbesar yang digunakan oleh masyarakat dalam mengakses internet. <b>Tetapi yang menjadi pertanyaan besar, apakah seluruh daerah di Indonesia dapat mengakses internet?</b></div>', unsafe_allow_html=True)
col2.write('<div style = "background-color:white;color:black; padding:15px;">Menurut survei pada tahun 2020, penduduk yang berumur diatas 5 tahun yang pernah <u>mengakses internet</u> telah mencapai <b>78%</b>. Dan dilihat dari hasil survei bahwa <b>98%</b> pengguna menggunakan media <u>Ponsel/Telepon seluler</u> untuk mengakses internet. <b>Tetapi yang menjadi pertanyaan besar, apakah seluruh daerah di Indonesia dapat mengakses internet?</b></div>', unsafe_allow_html=True)
st.write('')

st.subheader('Persentase kelurahan/desa di Indonesia yang dapat mengakses internet')

df2 = pd.read_excel("Source/Data/TidakAdaSinyal.xlsx")
df2MasterKelurahan = pd.read_excel("Source/Data/Jumlah Desa_Kelurahan Menurut Provinsi.xlsx")

dfMerge = pd.merge(df2,df2MasterKelurahan,on=['Provinsi'])
dfMerge['2014'] = (dfMerge['2014_y'] - dfMerge['2014_x']) / dfMerge['2014_y'] * 100
dfMerge['2018'] = (dfMerge['2018_y'] - dfMerge['2018_x']) / dfMerge['2018_y'] * 100
dfMerge['2019'] = (dfMerge['2019_y'] - dfMerge['2019_x']) / dfMerge['2019_y'] * 100
dfMerge['2020'] = (dfMerge['2020_y'] - dfMerge['2020_x']) / dfMerge['2020_y'] * 100
dfMerge['2021'] = (dfMerge['2021_y'] - dfMerge['2021_x']) / dfMerge['2021_y'] * 100
df2 = dfMerge[['Provinsi','2014','2018','2019','2020','2021']]

Provinsis2 = df2['Provinsi'].tolist()
provinsi2Selected = st.multiselect(
    "Pilih Provinsi", Provinsis2,["INDONESIA"], key="provinsi2Selected"
)
st.caption("*Hapus semua pilihan provinsi untuk melihat semua provinsi. Pilih 'INDONESIA' untuk melihat data Indonesia.")
col11,col12 = st.columns(2)

if provinsi2Selected:
    df2 = df2[df2['Provinsi'].isin(provinsi2Selected)]

col12.write(df2)
df2 = df2.melt('Provinsi', var_name='Tahun', value_name='value')
chart2 = alt.Chart(df2).mark_line(point=True).encode(
x=alt.X('Tahun:N'),
y=alt.Y('value:Q'),
color=alt.Color("Provinsi:N"),
tooltip=['Provinsi', 'Tahun', 'value']
).properties(title="Pesentase Desa/Kelurahan yang mendapatkan sinyal telekomunikasi").interactive()
col11.altair_chart(chart2, use_container_width=True)
st.caption("Sumber: BPS, Pendataan Potensi Desa")

st.write('<div style = "background-color:white;color:black; padding:15px;">Sinyal komunikasi adalah hal utama untuk masyarakat dalam mengakses internet. Pada grafik dan table diatas, persentase desa / kelurahan di Indonesia yang memiliki sinyal mengalami trend kenaikan setiap tahunnya, dalam arti setiap tahun pemerintah dan swasta terus mengembangkan dan membangun jaringan (<i>Base Transceiver Station</i>) sehingga mengurangi daerah terisolir sinyal. Pengembangan dari sisi infrastruktur yang dilakukan terus berlanjut dan memberikan nilai positif. <b>Lalu apakah keterampilan masyarakat akan teknologi informasi dan komputer juga ikut berkolerasi?</b></div>', unsafe_allow_html=True)
st.write('')
st.subheader('Proporsi Masyarakat Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Provinsi')

df3 = pd.read_excel("Source/Data/Proporsi Remaja Dan Dewasa Usia 15-59 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Provinsi.xlsx")
#st.write(df3)
Provinsis = df3['Provinsi'].tolist()
provinsiSelected = st.multiselect(
    "Pilih Provinsi", Provinsis,["INDONESIA"], key="provinsiSelected"
)
st.caption("*Hapus semua pilihan provinsi untuk melihat semua provinsi. Pilih 'INDONESIA' untuk melihat data Indonesia.")
if provinsiSelected:
    df3 = df3[df3['Provinsi'].isin(provinsiSelected)]

df3 = df3.melt('Provinsi', var_name='Tahun', value_name='value')
chart3 = alt.Chart(df3).mark_line(point=True).encode(
x=alt.X('Tahun:O'),
y=alt.Y('value:Q'),
color=alt.Color("Provinsi:N"),
tooltip=['Provinsi', 'Tahun', 'value']
).interactive()

labels3 = alt.Chart(df3).mark_text(align='left', dx=3).encode(
alt.X('Tahun:O', aggregate='max', axis=alt.Axis(title='Tahun')),
alt.Y('value:Q', aggregate={'argmax': 'Tahun'}, scale=alt.Scale(type='log'), axis=alt.Axis(title='Value')),
alt.Text('Provinsi'),
alt.Color('Provinsi:N', legend=None, scale=alt.Scale(domain=Provinsis,type='ordinal')), 
).properties(title='Proporsi Remaja Dan Dewasa Usia 15-59 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) di Indonesia',height=500)

st.altair_chart(alt.layer(chart3, labels3).resolve_scale(color='independent'), use_container_width=True)
st.caption("Sumber: BPS")
st.write('<div style = "background-color:white;color:black; padding:15px;">Dari grafik diatas menyatakan hampir diseluruh provinsi di Indonesia, proporsi masyarakat usia 15-59 tahun yang memiliki keterampilan teknologi informasi dan komputer (TIK) terus mengalami meningkat. Selama periode 2015-2021, secara keseluruhan di Indonesia mengalami kenaikan sebesar <b>43.13 %</b>.</div>', unsafe_allow_html=True)

st.write('')
st.subheader('Analisa korelasi antara ketersediaan jaringan telekomunikasi / internet dengan keterampilan teknologi informasi dan komputer (TIK) di Indonesia')



