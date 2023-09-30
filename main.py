import streamlit as st
import pandas as pd

# Load data from Excel file
excel_file_path = "data_dokter.xlsx"
df = pd.read_excel(excel_file_path)

# Set page title
st.set_page_config(page_title="Admin Panel")

# Page header
st.header("Admin Panel")

# Sidebar untuk pengaturan data yang akan ditampilkan
st.sidebar.subheader("Pengaturan Tampilan")
show_doctors = st.sidebar.checkbox("Tampilkan Dokter")
show_schedule = st.sidebar.checkbox("Tampilkan Jadwal Praktek")

# Menampilkan data berdasarkan pengaturan yang dipilih
if show_doctors:
    st.subheader("Informasi Dokter")
    st.table(df["Nama Dokter"])  # Menggantilah dengan nama kolom yang sesuai dengan data dokter Anda

if show_schedule:
    st.subheader("Jadwal Praktek Dokter")
    st.table(df[["Nama Dokter", "Hari", "Jam"]])  # Menggantilah dengan nama kolom yang sesuai dengan jadwal praktek Anda
