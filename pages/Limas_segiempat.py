import streamlit as st

st.write ("""
# Luas & Volume Limas Segiempat
Masukkan nilai sisi alas, tinggi limas dan tinggi sisi tegak untuk menghitung luas dan volume limas segiempat
""")

s = st.number_input ('Masukkan nilai sisi alas :',0)
tl = st.number_input ('Masukkan nilai tinggi limas :',0)
ts = st.number_input ('Masukkan nilai tinggi sisi tegak :',0)

hitung1 = st.button ('Hitung volume')
if hitung1 :
    volume = 1/3 * (s * s) * tl
    st.success (f'Hasilnya, volume limas segiempat adalah : {volume}')

hitung2 = st.button ('Hitung Luas')
if hitung2 :
    luas = (s * s) + (4 * s * ts * 1/2)
    st.success (f'Hasilnya, luas permukaan limas segiempat adalah : {luas}')    