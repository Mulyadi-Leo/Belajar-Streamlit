import streamlit as st
# Sidebar untuk navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Halaman Awal", "List Barang", "Alamat"])

# Halaman Awal
if page == "Halaman Awal":
    st.title("Selamat Datang di Aplikasi Streamlit")
    st.write("Ini adalah halaman awal dari aplikasi demo menggunakan Streamlit.")

# Halaman List Barang
elif page == "List Barang":
    st.title("Daftar Barang")
    barang = [
        {"nama": "Laptop", "harga": 10000000},
        {"nama": "Mouse", "harga": 150000},
        {"nama": "Keyboard", "harga": 300000},
        {"nama": "Monitor", "harga": 2000000}
    ]
    
    for b in barang:
        st.subheader(b["nama"])
        st.write(f"Harga: Rp {b['harga']:,}")

# Halaman Alamat
elif page == "Alamat":
    st.title("Alamat Toko")
    st.write("Toko Elektronik Cerdas")
    st.write("Jl. Teknologi No. 123, Jakarta Selatan")
    st.write("Email: info@tokocerdas.com")
    st.write("Telepon: (021) 123-4567")