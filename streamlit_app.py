import streamlit as st
from streamlit_option_menu import option_menu
import base64
from PIL import Image

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
background_image_path = "Presiden t1.jpg"
logo_image_path = "Logo PU-HD-2.jpg"

# Set gambar latar belakang
set_background_image(background_image_path)

# Menampilkan logo di tengah halaman dan memperbesar ukuran logo
def display_logo():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(logo_image_path, width=700)
    st.markdown("</div>", unsafe_allow_html=True)

display_logo()

# Fungsi untuk memusatkan konten
def center_content(content):
    return f"<p style='text-align: center;'>{content}</p>"

# Fungsi untuk menampilkan heading dengan CSS
def custom_heading(text, level):
    if level == 1:
        return f"<h1 style='text-align: center; font-size: 36px; font-family: Arial, sans-serif;'>{text}</h1>"
    elif level == 2:
        return f"<h2 style='text-align: left; font-size: 30px; font-family: Arial, sans-serif;'>{text}</h2>"  # Rata kiri untuk h2
    elif level == 3:
        return f"<h3 style='text-align: center; font-size: 24px; font-family: Arial, sans-serif;'>{text}</h3>"

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
    st.markdown(custom_heading("INTRODUCTION", 1), unsafe_allow_html=True)

    # Teks biasa (tanpa hyperlink) dengan rata kanan kiri
    st.markdown(
        """
        <div style="text-align: justify;">
        We from Group 3 Industrial Engineering 1, introduce an image transformation application based on Streamlit. 
        We developed this application as part of our final project, which presents various features such as rotation, 
        translation, scale, and others. With a simple yet innovative design, this application is real evidence of the 
        application of image processing technology in real life.
        </div>
        """, unsafe_allow_html=True
    )

    # Informasi anggota
    st.markdown(custom_heading("Group Members", 2), unsafe_allow_html=True)
    st.text("Chyntia Adinda Ramadani (004202305053)")
    st.text("Ratu Enjelita (004202305032)")
    st.text("Salsabilla Clarysa Putri (004202305016)")

    # Program studi dan fakultas
    st.markdown(custom_heading("Program Study", 2), unsafe_allow_html=True)
    st.text("Industrial Engineering")
    st.markdown(custom_heading("Faculty", 2), unsafe_allow_html=True)
    st.text("Engineering")

    # Foto anggota
    st.markdown(custom_heading("Member Photo", 2), unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("cinta2.jpg", caption="Chyntia Adinda", use_container_width=True)
    with col2:
        st.image("ratu2.jpg", caption="Ratu Enjelita", use_container_width=True)
    with col3:
        st.image("salsa2.jpg", caption="Salsabilla Clarysa", use_container_width=True)

# Menu "Application"
elif select == "Application":
    st.markdown(custom_heading("APPLICATION DESCRIPTION", 1), unsafe_allow_html=True)
    st.write(
        "This application allows users to perform various transformations on images, such as rotation, skew, zoom, scale, resize, brightness adjustment, and transparency."
    )
