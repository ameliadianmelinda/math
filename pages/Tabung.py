import streamlit as st

st.write ("""
# Luas & Volume Tabung
Masukkan nilai jari-jari dan tinggi tabung untuk menghitung luas dan volume tabung
""")

r = st.number_input ('Masukkan nilai jari-jari :',0)
t = st.number_input ('Masukkan nilai tinggi tabung :',0)

hitung1 = st.button ('Hitung volume')
if hitung1 :
    volume = 3.14 * (r*r) * t
    st.success (f'Hasilnya, volume tabung adalah : {volume}')

hitung2 = st.button ('Hitung Luas')    
if hitung2 :
    luas = 2 * 3.14 * r * ( r + t)
    st.success (f'Hasilnya, luas permukaan tabung adalah : {luas} ')