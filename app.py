
import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model_tebet.pkl', 'rb'))

# UI
st.set_page_config(page_title="Prediksi Harga Rumah di Tebet", layout="centered")
st.title("🏠 Prediksi Harga Rumah di Tebet")

st.markdown("Masukkan data spesifikasi rumah di bawah ini:")

lt = st.number_input("Luas Tanah (m²)", 0)
lb = st.number_input("Luas Bangunan (m²)", 0)
kt = st.number_input("Jumlah Kamar Tidur", 0)
km = st.number_input("Jumlah Kamar Mandi", 0)
grs = st.number_input("Jumlah Garasi", 0)

if st.button("Prediksi Harga"):
    features = np.array([[lt, lb, kt, km, grs]])
    hasil = model.predict(features)[0]
    st.success(f"💰 Estimasi Harga Rumah: Rp {int(hasil):,}")
