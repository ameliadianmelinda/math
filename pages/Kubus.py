import streamlit as st

st.write ("""
# Luas & Volume Kubus
Masukkan nilai sisi untuk menghitung luas dan volume kubus
""")

s = st.number_input ('Masukkan nilai sisi :',0)

hitungvolume = st.button ('HItung volume')
if hitungvolume :
    volume = s * s * s
    st.success (f'Hasilnya, volume kubus adalah : {volume}')

hitungluas = st.button ('Hitung luas')
if hitungluas :
    luas = 6 * ( s * s)    
    st.success (f'Hasilnya, luas permukaan kubus adalah : {luas}')

