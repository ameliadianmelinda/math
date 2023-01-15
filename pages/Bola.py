import streamlit as st 

st.write ("""
# Luas & Volume Bola
Masukkan nilai jaro-jari untuk menghitung luas dan volume bola
""")

r = st.number_input ('Masukkan nilai jari-jari :',0)

hitung1 = st.button ('Hitung volume')
if hitung1 :
    volume = 4 * 3.14 * (r *r)
    st.success (f'Hasilnya, volume bola adalah : {volume}')

hitung2 = st.button ('Hitung luas')
if hitung2 :
    luas = (4/3) * 3.14 * (r * r * r)    
    st.success (f'Hasilnya, luas permukaan bola adalah : {luas}')