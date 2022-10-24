import streamlit as st 
import pandas as pd
from datetime import date
import base64
import numpy as np
import altair as alt
#from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
import math

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
HomeContainer.write("Selasa, 18 Oktober 2022")

st.write('<div style = "background-color:white;color:black; padding:15px;">Dunia telah memasuki era Revolusi Industri 4.0 yang sangat berkaitan erat dengan perkembangan teknologi yang sangat pesat, dimana pekerjaan manusia semakin dimudahkan atau bahkan digantikan oleh berbagai macam teknologi-teknologi canggih seperti Robot Otonom (<i>Autonomous Robot</i>), Kendaraan Pintar, <i>Internet of Things</i> (IoT), Kecerdasan Buatan (<i>Artificial Intelligence</i>), <i>Big Data</i>, <i>Augmented Reality</i> (AR) dan lain sebagainya.<br><br> Pada era ini lah, masyarakat ditantang untuk sadar diri dan terus haus untuk mengembangkan keterampilan diri terutama dibidang teknologi informasi dan komputer agar tidak ketinggalan zaman / gagap teknologi karena hampir di semua aspek kehidupan masyarakat bergantung dan terintegrasi melalui teknologi digital dan internet.<br><br> Pandemi Covid-19 yang menghantam Indonesia, tak bisa dipungkiri memaksa masyarakat untuk dapat bertumpuh pada teknologi karena selama pandemi berlangsung, sektor yang masih kuat bertahan dan tetap berkembang adalah sektor industri teknologi informasi dan komunikasi. Dan selama pandemi, konsumsi teknologi digital melalui internet terus meningkat dan dampaknya semakin signifikan dan jelas disetiap aspek kehidupan masyarakat.</div>', unsafe_allow_html=True)
st.write('')

col1, col2 = st.columns(2)
df = pd.read_excel("Source/Data/Persentase Rumah Tangga yang Pernah Mengakses Internet dalam 3 Bulan Terakhir Menurut Media Akses.xlsx")
df = df.melt('Media', var_name='Tahun', value_name='Akses Internet (%)')
df = df[df['Tahun'] == '2020']

source = pd.DataFrame(
    {"Akses Internet": ["Ya", "Tidak"], "value": [78,22]}
)
base2 = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), 
    radius=alt.Radius("value:Q", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    color="Akses Internet:N"
).properties(title="Pernah mengakses internet di Indonesia (2020) (%)",height=300, width=430)
pie = base2.mark_arc(innerRadius=20, stroke="#fff")
text = base2.mark_text(radiusOffset=15).encode(text="value:Q")
PieChart = pie + text
col1.altair_chart(PieChart)

base = alt.Chart(df).encode(
    theta=alt.Theta("Akses Internet (%):Q", stack=True),
    radius=alt.Radius("Akses Internet (%)", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    color="Media:N",
)
c1 = base.mark_arc(innerRadius=20, stroke="#fff").properties(title="Media mengakses internet di Indonesia (2020) (%)",
    width=430,
    height=300)
c2 = base.mark_text(radiusOffset=15).encode(text="Akses Internet (%):Q")
chartRadial= c1 + c2
chartRadial.configure(background='#DDEEFF')
col2.altair_chart(chartRadial)

#chart = alt.Chart(df).mark_line(point=True).encode(
#  x=alt.X('Tahun:N'),
#  y=alt.Y('Akses Internet (%):Q'),
#  color=alt.Color("Media:N"),
#tooltip=['Media', 'Tahun', 'Akses Internet (%)']
#).properties(title="Persentase Rumah Tangga yang Pernah Mengakses Internet").interactive()
#col1.altair_chart(chart, use_container_width=True)

#col1.image("Source/Image/inet bps.jfif")
#col1.caption("Sumber : https://jakarta.bps.go.id/backend/images/Internet-2020-ind.JPG")
#col2.write('<div style = "background-color:white;color:black; padding:15px;">Beberapa tahun terakhir, masyarakat yang mengakses internet didominasi oleh penggunaan media telepon seluler dan dapat dilihat penggunaan media telepon seluler terus meningkat setiap tahunnya. Bila dibandingkan dengan media lainnya, jelas signifikan berbeda, karena media lain mengalami penurun setiap tahunnya.<br> Tentunya dengan dominasi tersebut menyatakan bahwa telepon seluler adalah media terbesar yang digunakan oleh masyarakat dalam mengakses internet. <b>Tetapi yang menjadi pertanyaan besar, apakah seluruh daerah di Indonesia dapat mengakses internet?</b></div>', unsafe_allow_html=True)

st.write('<div style = "background-color:white;color:black; padding:15px;">Menurut survei pada tahun 2020, penduduk yang berumur diatas 5 tahun yang pernah <u>mengakses internet</u> telah mencapai <b>78%</b>. Dan dilihat dari hasil survei bahwa <b>98.76%</b> pengguna menggunakan media <u>Ponsel/Telepon seluler</u> untuk mengakses internet.</div>', unsafe_allow_html=True)
st.write('')
st.write('<div style = "background-color:white;color:black; padding:15px;"><b>Tetapi yang menjadi pertanyaan besar, apakah seluruh daerah di Indonesia dapat mengakses internet? Lalu apakah keterampilan masyarakat akan teknologi informasi dan komputer mendukung? Apakah 2 faktor tersebut berkolerasi?</b></div>', unsafe_allow_html=True)
st.write('')

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
    "Pilih Provinsi", Provinsis2,["RATA-RATA INDONESIA"], key="provinsi2Selected"
)
st.caption("*Hapus semua pilihan provinsi untuk melihat semua provinsi. Pilih 'INDONESIA' untuk melihat data Indonesia.")
col11,col12 = st.columns(2)

allDataSinyal = df2.melt('Provinsi', var_name='Tahun', value_name='value')

if provinsi2Selected:
    df2 = df2[df2['Provinsi'].isin(provinsi2Selected)]

df2 = df2.melt('Provinsi', var_name='Tahun', value_name='value')
chart2 = alt.Chart(df2, padding={"left": 10, "top": 10, "right": 10, "bottom": 10}).mark_line(point=True).encode(
x=alt.X('Tahun:N'),
y=alt.Y('value', axis=alt.Axis(title='Percentage')),
color=alt.Color("Provinsi:N"),
tooltip=['Provinsi', 'Tahun', 'value']
).properties(title="Desa/Kelurahan yang mendapatkan sinyal telekomunikasi / internet").interactive()
col11.altair_chart(chart2, use_container_width=True)
#col11.caption("Sumber: BPS, Pendataan Potensi Desa")

col11.write('<div style = "background-color:white;color:black; padding:15px;">Sinyal komunikasi adalah hal utama untuk masyarakat dalam mengakses internet. Pada grafik diatas, persentase desa / kelurahan di Indonesia yang memiliki sinyal mengalami trend kenaikan setiap tahunnya, dalam arti setiap tahun pemerintah dan swasta terus mengembangkan dan membangun BTS (<i>Base Transceiver Station</i>) sehingga mengurangi daerah terisolir sinyal. BTS adalah salah satu bentuk infrastruktur telekomunikasi yang berperan penting dalam mewujudkan komunikasi nirkabel antara jaringan operator dengan perangkat komunikasi. Pengembangan dari salah satu infrastruktur BTS yang dilakukan terus berlanjut dan memberikan nilai positif. Selama periode 2014-2021, keseluruhan Indonesia mengalami kenaikan sebesar <b>3.3%</b>.</div>', unsafe_allow_html=True)

df3 = pd.read_excel("Source/Data/Proporsi Remaja Dan Dewasa Usia 15-59 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Provinsi.xlsx")
allDataTIK = df3.melt('Provinsi', var_name='Tahun', value_name='value')

if provinsi2Selected:
    df3 = df3[df3['Provinsi'].isin(provinsi2Selected)]

df3 = df3.melt('Provinsi', var_name='Tahun', value_name='value')
chart3 = alt.Chart(df3).mark_line(point=True).encode(
x=alt.X('Tahun:O'),
y=alt.Y('value', axis=alt.Axis(title='Percentage')),
color=alt.Color("Provinsi:N"),
tooltip=['Provinsi', 'Tahun', 'value']
).interactive().properties(title='Keterampilan Teknologi Informasi Dan Komputer (TIK)')

col12.altair_chart(alt.layer(chart3, padding={"left": 10, "top": 10, "right": 10, "bottom": 10}).resolve_scale(color='independent'), use_container_width=True)
#col12.caption("Sumber: BPS. Keterangan : Masyarakat usia 15-59 tahun")
col12.write('<div style = "background-color:white;color:black; padding:15px;">Dari grafik diatas menyatakan hampir diseluruh provinsi di Indonesia, proporsi masyarakat yang memiliki keterampilan teknologi informasi dan komputer (TIK) terus mengalami meningkat. Selama periode 2015-2021, secara keseluruhan di Indonesia mengalami kenaikan sebesar <b>43.13 %</b>.</div>', unsafe_allow_html=True)

st.write('')
st.subheader('Analisa korelasi antara ketersediaan jaringan telekomunikasi / internet dengan keterampilan teknologi informasi dan komputer (TIK) di Indonesia')
YearSelected = st.multiselect(
    "Pilih Tahun", ['2018','2019','2020','2021'],['2020','2021'], key="YearSelected"
)
df2['Key'] = df2['Provinsi'] +'-'+ df2['Tahun']
df3['Key'] = df3['Provinsi'] +'-'+ df3['Tahun']

btsData = df2[df2['Tahun'].isin(YearSelected)]
tikData = df3[df3['Tahun'].isin(YearSelected)]

kolerasiMerge = pd.merge(btsData,tikData,on=['Key'])
allKolerasiMeger = kolerasiMerge[['Provinsi_x','Tahun_x','value_x','value_y']]
allKolerasiMeger.columns = ['Provinsi','Tahun', 'Akses internet', 'Kemampuan TIK']
allKolerasiMeger = allKolerasiMeger.sort_values(by=['Provinsi','Tahun'])

kolerasiMerge = kolerasiMerge[['Key','value_x','value_y']]
kolerasiMerge.columns = ['Provinsi - Tahun', 'Akses internet', 'Kemampuan TIK']

col31,col32 = st.columns(2)
col31.dataframe(allKolerasiMeger.set_index('Provinsi'))

chart4 = alt.Chart(kolerasiMerge, padding={"left": 10, "top": 10, "right": 10, "bottom": 10}).mark_circle(size=60).encode(
    alt.X('Akses internet',axis=alt.Axis(title='Persentase daerah yang dapat akses internet (memiliki sinyal dan BTS)')),
    alt.Y('Kemampuan TIK',axis=alt.Axis(title='Proporsi Masyarakat Dengan Keterampilan TIK')),
    color='Provinsi - Tahun',
    tooltip=['Provinsi - Tahun', 'Akses internet', 'Kemampuan TIK']
).interactive()
col32.altair_chart(chart4, use_container_width=True)

barPerbandingan = alt.Chart(allKolerasiMeger).mark_bar().encode(
    x='Provinsi',
    y='Akses internet',
    color='Tahun:N'
).interactive()
col32.altair_chart(barPerbandingan, use_container_width=True)

col41,col42,col43 = st.columns(3)
col41.write("Hasil Korelasi Pearson :")
correlation = kolerasiMerge.corr(method='pearson')
#correlation.columns['Persentase daerah yang dapat akses internet (memiliki sinyal dan BTS)','Proporsi Masyarakat Dengan Keterampilan TIK']
col41.write(correlation)
nilaiCorr = math.nan
if math.isnan(correlation.iloc[1][0]) != True:
    col41.write("Nilai Kolerasi : <b>"+str(round(correlation.iloc[1][0],2)) +"</b>", unsafe_allow_html=True)
    nilaiCorr = round(correlation.iloc[1][0],2)

fig, ax = plt.subplots()
sns.heatmap(correlation, ax=ax)
col42.write(fig)

col43.write('<div style = "background-color:white;color:black; padding:10px; font-size:12px;">Keterangan :<br>0 : Tidak ada korelasi<br>0.00 - 0.25 : korelasi sangat lemah<br>0.25 - 0.50 : korelasi cukup<br>0.50 - 0.75 : korelasi kuat<br>0.75 - 0.99 : korelasi sangat kuat<br>1 : korelasi sempurna</div>', unsafe_allow_html=True)
col43.write('')
col43.write('<div style = "background-color:white;color:black; padding:10px; font-size:12px;">Keterangan :<br>Akses internet : Persentase daerah yang dapat akses internet (memiliki sinyal dan BTS)<br>Kemampuan TIK : Proporsi Masyarakat Dengan Keterampilan TIK</div>', unsafe_allow_html=True)

kataCorr = ""
if nilaiCorr < 0:
    kataCorr = "BERKORELASI BERLAWANAN"
elif nilaiCorr == 0:
    kataCorr = "TIDAK BERKORELASI"
elif nilaiCorr <= 0.25: 
    kataCorr = "KORELASI SANGAT LEMAH"
elif nilaiCorr <= 0.5: 
    kataCorr = "KORELASI CUKUP"
elif nilaiCorr <= 0.75: 
    kataCorr = "KORELASI KUAT"
elif nilaiCorr <= 0.99: 
    kataCorr = "KORELASI SANGAT KUAT"
elif nilaiCorr == 1:
    kataCorr = "KORELASI SEMPURNA"
else:
    kataCorr = "-"

if kataCorr != "-" :
    rataRataSinyal = round(kolerasiMerge['Akses internet'].mean(),2)
    rataRataTIK = round(kolerasiMerge['Kemampuan TIK'].mean(),2)
    kesimpulan = "Berdasarkan daerah dan tahun yang dipilih, menyatakan bahwa korelasi antara Persentase daerah yang dapat akses internet (memiliki sinyal dan BTS) dengan Proporsi Masyarakat Dengan Keterampilan TIK adalah <b>"+kataCorr+"</b>.<br>"
    if nilaiCorr < 0:
        kesimpulan += "Sehingga pemerintah harus memilih <b>salah satu</b> antara melakukan pengembangan secara infrastruktur seperti menambahan BTS diberbagai daerah di Indonesia agar setiap daerah mendapatkan sinyal telekomunikasi yang sama rata atau memberikan pelatihan keterampilan teknologi informasi dan komputer untuk daerah-daerah agar keterampilan teknologi informasi dan komputer diseluruh Indonesia merata."
        kesimpulan += "<br>Nilai rata-rata dari Persentase daerah yang dapat akses internet (memiliki sinyal dan BTS) adalah <b>"+str(rataRataSinyal)+"</b>."
        kesimpulan += "<br>Nilai rata-rata dari Proporsi Masyarakat Dengan Keterampilan TIK adalah  <b>"+str(rataRataTIK)+"</b>."
        kesimpulan += "<br>Bila dibandingkan nilai rata-rata tersebut, pemerintah bisa mengambil nilai terendah untuk dapat difokuskan dikembangkan."
    elif nilaiCorr <= 0.25:
        kesimpulan += "Sehingga pemerintah bisa terus melakukan pengembangan secara infrastruktur seperti menambahan BTS diberbagai daerah di Indonesia agar setiap daerah mendapatkan sinyal telekomunikasi yang sama rata, namun disisi lain juga harus memberikan pelatihan keterampilan teknologi informasi dan komputer untuk daerah-daerah agar keterampilan teknologi informasi dan komputer diseluruh Indonesia merata."
        kesimpulan += " Namun alahkah baiknya bila keduanya terus dikembangkan secara beriringan agar setiap daerah di Indonesia lebih cepat dan lebih siap akan Teknologi kedepannya."
    elif nilaiCorr <= 1:
        kesimpulan += "Nilai rata-rata dari Persentase daerah yang dapat akses internet (memiliki sinyal dan BTS) adalah <b>"+str(rataRataSinyal)+"</b>."
        kesimpulan += "<br>Nilai rata-rata dari Proporsi Masyarakat Dengan Keterampilan TIK adalah  <b>"+str(rataRataTIK)+"</b>."
        kesimpulan += "<br>Bila dibandingkan nilai rata-rata tersebut, pemerintah bisa mengambil nilai terendah untuk dapat difokuskan dikembangkan."
        if rataRataSinyal < rataRataTIK :
            kesimpulan += "<br>Pada data daerah dan tahun yang dipilih menyatakan bahwa Persentase daerah yang dapat akses internet lebih rendah bila dibandingkan dengan proporsi keterampilan masyarakat akan teknologi informasi dan komputer. Maka dari itu, pemerintah bisa fokus mengembangkan infrastruktur agar seluruh daerah di Indonesia dapat mendapatkan akses internet dan beriringan keterampilan TIK akan ikut meningkat tanpa diperlukan pelatihan khusus."
        elif rataRataSinyal == rataRataTIK :
            kesimpulan += "<br>Pada data daerah dan tahun yang dipilih menyatakan bahwa Persentase daerah yang dapat akses internet sama dengan proporsi keterampilan masyarakat akan teknologi informasi dan komputer. Maka dari itu, pemerintah bisa fokus mengembangkan infrastruktur agar seluruh daerah di Indonesia dapat mendapatkan akses internet dan beriringan memberikan pelatihan khusus agar keterampilan TIK akan ikut meningkat."
        elif rataRataSinyal > rataRataTIK :
            kesimpulan += "<br>Pada data daerah dan tahun yang dipilih menyatakan bahwa Persentase daerah yang dapat akses internet lebih tinggi bila dibandingkan dengan proporsi keterampilan masyarakat akan teknologi informasi dan komputer. Maka dari itu, pemerintah bisa fokus memberikan pelatihan khusus untuk meningkatkan keterampilan TIK diseluruh Indonesia."
        kesimpulan += " Namun alahkah baiknya bila keduanya terus dikembangkan secara beriringan agar setiap daerah di Indonesia lebih cepat dan lebih siap akan Teknologi kedepannya."
    st.write('<div style = "background-color:white;color:black; padding:10px;"><b>KESIMPULAN :</b><br>'+kesimpulan+'</div>', unsafe_allow_html=True)

    col51, col52 = st.columns(2)
    col51.write("Berikut 5 daerah yang memiliki persentase akses internet terendah per tahun 2021")
    low5Internet = allDataSinyal[allDataSinyal['Tahun'] == '2021'].sort_values(by=['value']).head()
    low5Internet = low5Internet[['Provinsi','value']]
    low5Internet['value'] = round(low5Internet['value'],2)
    low5Internet.columns = ['Provinsi', 'Persentase Akses Internet Terendah']
    col51.write(low5Internet.set_index('Provinsi'))

    col51.write("Berikut 5 daerah yang memiliki persentase akses internet tertinggi per tahun 2021")
    top5Internet = allDataSinyal[allDataSinyal['Tahun'] == '2021'].sort_values(by=['value'],ascending=False).head()
    top5Internet = top5Internet[['Provinsi','value']]
    top5Internet['value'] = round(top5Internet['value'],2)
    top5Internet.columns = ['Provinsi', 'Persentase Akses Internet Tertinggi']
    col51.write(top5Internet.set_index('Provinsi'))
    
    col52.write("Berikut 5 daerah yang memiliki proporsi keterampilan TIK terendah per tahun 2021")
    low5TIK = allDataTIK[allDataTIK['Tahun'] == '2021'].sort_values(by=['value']).head()
    low5TIK = low5TIK[['Provinsi','value']]
    low5TIK['value'] = round(low5TIK['value'],2)
    low5TIK.columns = ['Provinsi', 'Proporsi keterampilan TIK Terendah']
    col52.write(low5TIK.set_index('Provinsi'))
    
    col52.write("Berikut 5 daerah yang memiliki proporsi keterampilan TIK tertinggi per tahun 2021")
    top5TIK = allDataTIK[allDataTIK['Tahun'] == '2021'].sort_values(by=['value'],ascending=False).head()
    top5TIK = top5TIK[['Provinsi','value']]
    top5TIK['value'] = round(top5TIK['value'],2)
    top5TIK.columns = ['Provinsi', 'Proporsi keterampilan TIK Tertinggi']
    col52.write(top5TIK.set_index('Provinsi'))

st.subheader('Referensi')
st.write('<div style = "background-color:white;color:black; padding:10px; font-size:12px;">1. BPS, https://www.bps.go.id/indicator/28/1447/1/proporsi-remaja-dan-dewasa-usia-15-59-tahun-dengan-keterampilan-teknologi-informasi-dan-komputer-tik-menurut-provinsi.html <br>2. Berdasarkan Laporan BPS Provinsi/Kabupaten/Kota, https://www.bps.go.id/indicator/101/85/1/jumlah-desa.html <br>3. BPS, Survei Sosial Ekonomi Nasional (Susenas), https://www.bps.go.id/indicator/2/402/1/persentase-rumah-tangga-yang-pernah-mengakses-internet-dalam-3-bulan-terakhir-menurut-media-akses.html <br> 4. https://www.bps.go.id/indicator/2/1686/1/banyaknya-desa-kelurahan-yang-memiliki-menara-bts-menurut-provinsi-dan-penerimaan-sinyal-telepon-selular-perkotaan-perdesaan-.html</div>', unsafe_allow_html=True)
