import streamlit as st

st.write ("""
# Luas & Volume Kerucut
Masukkan nilai jari-jari dan tinggi kerucut untuk menghitung luas dan volume kerucut
""")

r = st.number_input ('Masukkan nilai jari-jari :',0)
t = st.number_input ('Masukkan nilai tinggi kerucut :',0)
s = st.number_input ('Masukkan nilai sisi pada kerucut :',0)

hitung1 = st.button ('Hitung volume')
if hitung1 :
    volume = 1/3 * 3.14 * (r * r) * t
    st.success (f'Hasilnya, volume kerucut adalah : {volume}')

hitung2 = st.button ('Hitung luas')
if hitung2 :
    luas = 3.14 * r * (s + r)
    st.success (f'Hasilnya, luas permukaan tabung adalah : {luas}')
