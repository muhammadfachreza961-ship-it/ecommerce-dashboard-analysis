import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.header('E-Commerce Performance Dashboard 📊')

# --- LOAD DATA ---
@st.cache_data
def load_data():
    # Pastikan path ini sesuai dengan struktur folder di GitHub Anda
    # Kita muat 3 file utama untuk digabungkan
    orders = pd.read_csv("E-Commerce Public Dataset/orders_dataset.csv")
    items = pd.read_csv("E-Commerce Public Dataset/order_items_dataset.csv")
    customers = pd.read_csv("E-Commerce Public Dataset/customers_dataset.csv")
    
    # Gabungkan data agar kolom order_id, price, dan customer_state tersedia di satu DF
    main_df = orders.merge(items, on="order_id")
    main_df = main_df.merge(customers, on="customer_id")
    
    return main_df

try:
    df = load_data()

    # --- METRICS ---
    col1, col2 = st.columns(2)
    with col1:
        # Sekarang order_id sudah pasti ada karena sudah di-merge
        st.metric("Total Orders", value=df.order_id.nunique())
    with col2:
        st.metric("Total Revenue", value=f"R$ {df.price.sum():,.2f}")

    st.divider()

    # --- VISUALISASI ---
    st.subheader("Top 10 States by Revenue")
    state_revenue = df.groupby("customer_state").price.sum().sort_values(ascending=False).head(10).reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=state_revenue, x='price', y='customer_state', palette="viridis", ax=ax)
    ax.set_xlabel("Total Revenue (R$)")
    ax.set_ylabel("State")
    st.pyplot(fig)

except Exception as e:
    st.error(f"Error: {e}")
    st.info("Pastikan folder 'E-Commerce Public Dataset' ada di GitHub dan berisi file CSV yang benar.")