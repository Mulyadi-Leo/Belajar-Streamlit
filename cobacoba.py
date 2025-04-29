import streamlit as st
from PIL import Image
# Sidebar untuk navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Introduction", "Project", "Contact"])

# Halaman Awal
if page == "Introduction":
    

    col_kiri, col_kanan = st.columns([2, 3])  # 40% dan 60%

    # === Kolom Kiri ===
    with col_kiri:
        st.image("mul.png",caption="Data Scientist", use_container_width=True)
        # st.markdown("<h3 style='text-align: center;'>Mulyadi</h3>", unsafe_allow_html=True)

    # === Kolom Kanan ===
    with col_kanan:
        # Bagian atas dan bawah: 80% atas untuk perkenalan, 20% bawah untuk 3 gambar
        col_atas, col_bawah = st.columns([1, 0.25])  # Trik layout agar terlihat vertikal proporsional

        # Perkenalan diri (bagian atas)
        with st.container():
            st.markdown("### Call me Mulyadi")
            st.write("""
        I’m a <span style="color: #FF5733; font-weight: bold;">Data Scientist</span> with expertise in data accuracy, validation, and exploratory data analysis (EDA). 
        I specialize in managing large datasets, creating data visualizations, and building dashboards to drive business insights. 
        Check out my <span style="color: #FF5733; font-weight: bold;">projects</span> in the navigation to see how I deliver data-driven solutions using tools like Google Colab, PostgreSQL, and Power BI.
        """, unsafe_allow_html=True)

        st.markdown("---")  # Garis pemisah opsional

        # Baris bawah (3 gambar kecil)
        col1, col2, col3 = st.columns(3)

        # Buka dan resize gambar
        img1 = Image.open("colab.png").resize((150, 150))
        img2 = Image.open("postgre.png").resize((150, 150))
        img3 = Image.open("powerbi.png").resize((150, 150))

        with col1:
            st.image(img1, use_container_width=True)
        with col2:
            st.image(img2, use_container_width=True)
        with col3:
            st.image(img3, use_container_width=True)

# Halaman List Barang
elif page == "Project":
    # st.title("Daftar Barang")
    # barang = [
    #     {"nama": "Laptop", "harga": 10000000},
    #     {"nama": "Mouse", "harga": 150000},
    #     {"nama": "Keyboard", "harga": 300000},
    #     {"nama": "Monitor", "harga": 2000000}
    # ]
    
    # for b in barang:
    #     st.subheader(b["nama"])
    #     st.write(f"Harga: Rp {b['harga']:,}")
    # st.markdown("""
    # <style>
    #     .top-container {
    #         height: 20vh;
    #         display: flex;
    #         justify-content: center;
    #         align-items: center;
    #         background-color: #F1F1F1;
    #         text-align: center;
    #     }
    #     .top-container img {
    #         max-width: 100%;
    #         max-height: 800%;
    #     }
    # </style>
    # """, unsafe_allow_html=True)

    # Bagian atas (gambar banner + caption)
    with st.container():
        st.markdown('<div class="top-container">', unsafe_allow_html=True)
        # Menampilkan gambar banner
        # st.image("medical.jpg", caption="This is the banner caption", use_container_width=True)
        st.image("red.jpg", width=1000)
        st.markdown('</div>', unsafe_allow_html=True)

    # Bagian bawah (dinamis)
    with st.container():
        st.header("Dynamic Bottom Container")
        st.write("This is the bottom container. You can add dynamic content here.")
        # Menambahkan beberapa konten dinamis
        for i in range(1, 6):
            st.write(f"Dynamic content line {i}")

# Halaman Alamat
elif page == "Alamat":
    st.title("Alamat Toko")
    st.write("Toko Elektronik Cerdas")
    st.write("Jl. Teknologi No. 123, Jakarta Selatan")
    st.write("Email: info@tokocerdas.com")
    st.write("Telepon: (021) 123-4567")