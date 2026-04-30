import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Judul Dashboard
st.header('E-Commerce Performance Dashboard 📊')

# Load Data
df = pd.read_csv("E-Commerce Public Dataset/customers_dataset.csv")

# Tampilkan metrik sederhana (Contoh)
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Orders", value=df.order_id.nunique())
with col2:
    st.metric("Total Revenue", value=f"R$ {df.price.sum():,.2f}")

# Visualisasi Pertanyaan 1 (Contoh: Delivery Performance)
st.subheader("Rata-rata Selisih Pengiriman per State")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df.head(10), x='customer_state', y='price', ax=ax) # Ganti y dengan kolom durasi kamu
st.pyplot(fig)