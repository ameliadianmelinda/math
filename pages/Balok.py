import streamlit as st

st.write ("""
# Luas & Volume Balok
Masukkan nilai panjang, lebar dan tinggi untuk menghitung luas dan volume balok
""")

p = st.number_input ('Masukkan nilai panjang :' ,0)
l = st.number_input ('Masukkan nilai lebar :' ,0)
t = st.number_input ('Masukkan nilai tinggi :' ,0)

hitungvolume =  st.button ('Hitung volume')
if hitungvolume :
    volume = p * l * t 
    st.success (f'Hasilnya, volume balok adalah : {volume}')

hitungluas =  st.button ('Hitung luas')
if hitungluas :
    luas = 2* ((p * l) + (p * t) + (l * t))
    st.success (f'Hasilnya, luas permukaan balok adalah : {luas}')       