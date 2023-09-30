import streamlit as st
import pandas as pd

# Load data from Excel file
excel_file_path = "data_dokter_1.xlsx"  # Ganti dengan path file Excel Anda
df = pd.read_excel(excel_file_path)

# Set page title
st.set_page_config(page_title="Admin Panel")

# Page header
st.header("Admin Panel")

# Sidebar untuk konfigurasi informasi
st.sidebar.subheader("Pengaturan")
selected_day = st.sidebar.selectbox("Pilih Hari", df["Hari"].unique())
show_all_doctors = st.sidebar.checkbox("Tampilkan Semua Dokter")

# Tombol untuk menampilkan data di layar utama
if st.sidebar.button("Tampilkan di Layar"):
    # Menampilkan informasi dokter yang dipilih atau semua dokter
    if show_all_doctors:
        filtered_df = df[df["Hari"] == selected_day]
    else:
        filtered_df = df[(df["Hari"] == selected_day)]

    # Menghilangkan kolom "Hari" dari tabel
    filtered_df = filtered_df.drop(columns=["Hari"])
    
    # Urutkan berdasarkan kolom jam praktek (jika ada)
    if "Jam" in filtered_df.columns:
        filtered_df = filtered_df.sort_values(by=["Jam"])  # Ganti "Jam" dengan nama kolom jam praktek
        
    # Tampilkan nama hari di atas kanan tabel
    st.markdown(f"**Hari: {selected_day}**")
    
    # Tampilkan informasi dokter dalam bentuk tabel tanpa nomor urut
    st.markdown(filtered_df.to_markdown(index=False), unsafe_allow_html=True)
