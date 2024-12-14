import streamlit as st
from streamlit_option_menu import option_menu  # type: ignore
from PIL import Image, ImageEnhance
import numpy as np
import cv2

# Konfigurasi halaman
st.set_page_config(page_title="Kelompok Project", layout="centered")

# Navigasi sidebar
with st.sidebar:
    select = option_menu(
        'Project Final Exam',
        ['Introduction', 'Application'],
        default_index=0
    )

if select == 'Introduction':
    st.markdown("<p class='title'>INTRODUCTION</p>", unsafe_allow_html=True)

    # Informasi kelompok
    st.markdown("<p class='subheader'>Group 3 IEN 1 2024</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Chyntia Adinda Ramadani (004202305053)</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Ratu Enjelita (004202305032)</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Salsabilla Clarysa Putri (004202305016)</p>", unsafe_allow_html=True)

    # Tampilkan logo universitas
    st.image("President_University_Logo.png", use_container_width=True)

    st.markdown("<p class='subheader'>Program Study</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Industrial Engineering</p>", unsafe_allow_html=True)

    st.markdown("<p class='subheader'>Faculty</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Engineering</p>", unsafe_allow_html=True)

    # Foto anggota
    st.markdown("<p class='subheader'>Member Photo</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: st.image("cinta2.jpg", caption="Chyntia Adinda", use_container_width=True)
    with col2: st.image("ratu2.jpg", caption="Ratu Engelita", use_container_width=True)
    with col3: st.image("salsa2.jpg", caption="Salsabilla Clarysa", use_container_width=True)

elif select == 'Application':
    st.markdown("<p class='title'>APPLICATION DESCRIPTION</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Transform images: rotate, skew, zoom, scale, resize, brightness, transparency.</p>", unsafe_allow_html=True)

    # Upload gambar
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Pilihan transformasi gambar
        transformation = st.selectbox("Select Transformation", ["Select", "Rotate", "Skew", "Zoom", "Scale", "Resize", "Brightness", "Transparency"])

        # Implementasi transformasi
        if transformation == "Rotate":
            angle = st.number_input("Rotation Angle (degrees)", 0, 360, 90)
            st.image(image.rotate(angle), caption="Rotated Image", use_container_width=True)
        elif transformation == "Skew":
            skew_factor = st.number_input("Skew Factor", 0.1, 10.0, 1.0)
            skewed_image = cv2.warpAffine(np.array(image), np.float32([[1, skew_factor, 0], [0, 1, 0]]), (image.width, image.height))
            st.image(skewed_image, caption="Skewed Image", use_container_width=True)
        elif transformation == "Zoom":
            zoom_factor = st.number_input("Zoom Factor", 1.0, 10.0, 1.5)
            zoomed_image = cv2.resize(np.array(image), (int(image.width * zoom_factor), int(image.height * zoom_factor)))
            st.image(zoomed_image, caption="Zoomed Image", use_container_width=True)
        elif transformation == "Scale":
            scale_factor = st.number_input("Scale Factor", 0.1, 10.0, 1.0)
            st.image(image.resize((int(image.width * scale_factor), int(image.height * scale_factor))), caption="Scaled Image", use_container_width=True)
        elif transformation == "Resize":
            new_width = st.number_input("New Width", 100, 2000, image.width)
            new_height = st.number_input("New Height", 100, 2000, image.height)
            st.image(image.resize((new_width, new_height)), caption="Resized Image", use_container_width=True)
        elif transformation == "Brightness":
            brightness = st.slider("Adjust Brightness", 0.1, 10.0, 1.0)
            st.image(ImageEnhance.Brightness(image).enhance(brightness), caption="Brightness Adjusted Image", use_container_width=True)
        elif transformation == "Transparency":
            transparency = st.slider("Adjust Transparency", 0.0, 1.0, 1.0)
            image = image.convert('RGBA')
            data = np.array(image)
            data[..., 3] = (data[..., 3] * transparency).astype(np.uint8)
            st.image(Image.fromarray(data, 'RGBA'), caption="Transparency Adjusted Image", use_container_width=True)
