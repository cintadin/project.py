import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image, ImageEnhance
import base64
import numpy as np

# Fungsi untuk mengubah file gambar lokal menjadi Base64
def set_background_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        st.markdown(
            f"""
            <style>
            [data-testid="stAppViewContainer"] {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}
            [data-testid="stSidebar"] {{
                background-color: rgba(255, 255, 255, 0.8);
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error("File background tidak ditemukan. Periksa path gambar Anda.")

# Konfigurasi halaman
st.set_page_config(page_title="Project Final Exam", layout="centered")

# Atur path file lokal untuk gambar latar belakang dan logo
background_image_path = "Presiden t1.jpg"  # Pastikan path-nya benar
logo_image_path = "Logo PU-HD-2.jpg"  # Ganti dengan path logo yang sesuai

# Set gambar latar belakang
set_background_image(background_image_path)

# Menampilkan logo di tengah halaman dan memperbesar ukuran logo
def display_logo():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(logo_image_path, width=700)  # Perbesar logo dengan mengubah nilai width
    st.markdown("</div>", unsafe_allow_html=True)

display_logo()

# Navigasi sidebar
with st.sidebar:
    select = option_menu(
        "Project Final Exam", 
        ["Introduction", "Application"], 
        default_index=0
    )

# Membuat konten terpusat
def center_content(content):
    return f"""
    <div style="text-align: center; max-width: 900px; margin: auto;">
        {content}
    </div>
    """

# Menu "Introduction"
if select == "Introduction":
    # Header
    st.markdown(center_content("<h2>INTRODUCTION</h2>"), unsafe_allow_html=True)

    # Informasi anggota
    st.markdown(center_content("<h3>Group Members</h3>"), unsafe_allow_html=True)
    st.write("Chyntia Adinda Ramadani (004202305053)")
    st.write("Ratu Enjelita (004202305032)")
    st.write("Salsabilla Clarysa Putri (004202305016)")

    # Program studi dan fakultas
    st.markdown(center_content("<h3>Program Study</h3>"), unsafe_allow_html=True)
    st.write("Industrial Engineering")
    st.markdown(center_content("<h3>Faculty</h3>"), unsafe_allow_html=True)
    st.write("Engineering")

    # Foto anggota
    st.markdown(center_content("<h3>Member Photo</h3>"), unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("cinta2.jpg", caption="Chyntia Adinda", use_container_width=True)
    with col2:
        st.image("ratu2.jpg", caption="Ratu Enjelita", use_container_width=True)
    with col3:
        st.image("salsa2.jpg", caption="Salsabilla Clarysa", use_container_width=True)

# Menu "Application"
elif select == "Application":
    st.markdown(center_content("<h2>APPLICATION DESCRIPTION</h2>"), unsafe_allow_html=True)
    st.write(
        "This application allows users to perform various transformations on images, such as rotation, skew, zoom, scale, resize, brightness adjustment, and transparency."
    )

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        transformation = st.selectbox(
            "Select Transformation", 
            ["Select", "Rotate", "Translate", "Scale", "Shear", "Resize", "Skew", "Brightness", "Transparency", "Remove Background"]
        )

        if transformation == "Rotate":
            angle = st.slider("Enter Rotation Angle (degrees)", min_value=0, max_value=360, value=90, step=1)
            rotated_image = image.rotate(angle)
            st.image(rotated_image, caption=f"Rotated Image by {angle}°", use_container_width=True)

        elif transformation == "Translate":
            tx = st.slider("Translate X (pixels)", min_value=-500, max_value=500, value=0, step=1)
            ty = st.slider("Translate Y (pixels)", min_value=-500, max_value=500, value=0, step=1)
            translated_image = image.transform(
                image.size, 
                Image.AFFINE, 
                (1, 0, tx, 0, 1, ty)
            )
            st.image(translated_image, caption="Translated Image", use_container_width=True)
