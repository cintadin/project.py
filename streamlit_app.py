import streamlit as st
from streamlit_option_menu import option_menu  # type: ignore
from PIL import Image, ImageEnhance
import numpy as np
import io

# Konfigurasi halaman
st.set_page_config(page_title="Project Final Exam", layout="centered")

# Fungsi untuk mengubah gambar menjadi byte stream
def image_to_bytes(img, format='PNG'):
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format=format)
    img_byte_arr.seek(0)
    return img_byte_arr

# Menambahkan gambar latar belakang dengan CSS (gunakan path relatif atau URL yang benar)
background_image = "images/background.jpg"  # Ganti dengan path yang sesuai (misal folder 'images')
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('{"C:\Users\Lenovo\OneDrive\Gambar\Presiden t1.jpg"}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
    }}
    .container {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
    }}
    .title {{
        font-size: 36px;
        font-weight: bold;
        color: #333333;
        text-align: center;
    }}
    .subheader {{
        font-size: 24px;
        font-weight: bold;
        color: #4CAF50;
    }}
    .content {{
        font-size: 18px;
        color: #555555;
    }}
    </style>
    """, unsafe_allow_html=True)

# Navigasi sidebar
with st.sidebar:
    select = option_menu(
        "Project Final Exam", 
        ["Introduction", "Application"], 
        default_index=0
    )

# Menu "Introduction"
if select == "Introduction":
    # Header
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.markdown("<p class='title'>INTRODUCTION</p>", unsafe_allow_html=True)

    # Informasi anggota
    st.markdown("<p class='subheader'>Group Members</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>1. Chyntia Adinda Ramadani</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>2. Salsabilla Clarysa Putri</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>3. Ratu Enjelita</p>", unsafe_allow_html=True)

    # Program studi dan fakultas
    st.markdown("<p class='subheader'>Program Study</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Industrial Engineering</p>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>Faculty</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Engineering</p>", unsafe_allow_html=True)

    # Foto anggota
    st.markdown("<p class='subheader'>Member Photo</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("cinta2.jpg", caption="Chyntia Adinda", use_container_width=True)
    with col2:
        st.image("salsa2.jpg", caption="Salsabilla Clarysa", use_container_width=True)
    with col3:
        st.image("ratu2.jpg", caption="Ratu Enjelita", use_container_width=True)

# Menu "Application"
elif select == "Application":
    # Deskripsi aplikasi
    st.markdown("<p class='title'>APPLICATION DESCRIPTION</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>This application allows users to perform various transformations on images, such as rotation, skew, zoom, scale, resize, brightness adjustment, and transparency. Users can choose the type of transformation and adjust parameters as desired, as well as see the results of image changes directly, making it easier to edit images as needed.</p>", unsafe_allow_html=True)

    # Upload gambar untuk transformasi
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
