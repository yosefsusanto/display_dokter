import streamlit as st
import pandas as pd

# Load data from Excel file
excel_file_path = "data_dokter.xlsx"  # Ganti dengan path file Excel Anda
df = pd.read_excel(excel_file_path)

# Set page title
st.set_page_config(page_title="Display Informasi Praktek Dokter")

# Page header
st.header("Informasi Praktek Dokter")

# Sidebar untuk filter dokter
st.sidebar.subheader("Filter Dokter")
selected_day = st.sidebar.selectbox("Pilih Hari", df["Hari"].unique())
selected_time = st.sidebar.selectbox("Pilih Jam", df["Jam"].unique())

# Filter data berdasarkan hari dan jam yang dipilih
filtered_df = df[(df["Hari"] == selected_day) & (df["Jam"] == selected_time)]

# Tampilkan data dokter
st.subheader("Daftar Dokter")
st.table(filtered_df)

# Tampilkan kuota dan status dokter
st.subheader("Status Dokter")
for index, row in filtered_df.iterrows():
    st.write(f"Dokter: {row['Dokter']}")
    st.write(f"Kuota: {row['Kuota']}")
    st.write(f"Status: {'Tutup' if row['Status'] == 'Tutup' else 'Buka'}")

# Informasi tambahan
st.info("Data di atas adalah informasi praktek dokter berdasarkan hari dan jam yang dipilih.")
