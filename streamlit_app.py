import streamlit as st
from streamlit_option_menu import option_menu
import base64
from PIL import Image, ImageEnhance
import numpy as np
import io

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
st.set_page_config(page_title="Project of CRS", layout="centered")

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
        return f"<h3 style='text-align: center; font-size: 30px; font-family: Arial, sans-serif;'>{text}</h3>"

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

    # Menambahkan jarak antar teks 
    st.markdown("<br><br>", unsafe_allow_html=True)  # Menambahkan 2 baris kosong

    # Informasi anggota
    st.markdown(custom_heading("Group Members", 2), unsafe_allow_html=True)
    st.text("1. Chyntia Adinda Ramadani (004202305053)")
    st.text("2. Ratu Enjelita (004202305032)")
    st.text("3. Salsabilla Clarysa Putri (004202305016)")

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
    st.markdown(
        """
        <div style="text-align: justify;">
        The application allows users to upload images and apply various transformations, such as rotation, skew, zoom, scale, resize, brightness adjustment, transparency, shear, translation, and RGB color channel adjustment. Users can customize each transformation with specified parameters and download the transformed image in PNG, JPG, or PDF format.
        </div>
        """, unsafe_allow_html=True)
    
    # Menambahkan jarak antar teks dan elemen upload
    st.markdown("<br>", unsafe_allow_html=True)  # Menambahkan 1 baris kosong

    # Upload Image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Transformasi gambar
        transformation = st.selectbox("Select Transformation", ["Select", "Rotate", "Skew", "Zoom", "Scale", "Resize", "Brightness", "Transparency", "Shear", "Translate", "Adjust RGB"])

        transformed_image = image
        if transformation == "Rotate":
            angle = st.number_input("Enter Rotation Angle (degrees)", min_value=0, max_value=360, value=90, step=1)
            transformed_image = image.rotate(angle)

        elif transformation == "Skew":
            skew_factor = st.number_input("Enter Skew Factor", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            img_array = np.array(image)
            rows, cols = img_array.shape[:2]
            transformed_image = image.transform((cols, rows), Image.AFFINE, (1, skew_factor, 0, 0, 1, 0))

        elif transformation == "Zoom":
            zoom_factor = st.number_input("Enter Zoom Factor", min_value=1.0, max_value=10.0, value=1.5, step=0.1)
            width, height = image.size
            transformed_image = image.resize((int(width * zoom_factor), int(height * zoom_factor)))

        elif transformation == "Scale":
            scale_factor = st.number_input("Enter Scale Factor", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            width, height = image.size
            transformed_image = image.resize((int(width * scale_factor), int(height * scale_factor)))

        elif transformation == "Resize":
            new_width = st.number_input("Enter New Width", min_value=100, max_value=2000, value=image.width, step=10)
            new_height = st.number_input("Enter New Height", min_value=100, max_value=2000, value=image.height, step=10)
            transformed_image = image.resize((new_width, new_height))

        elif transformation == "Brightness":
            brightness = st.slider("Adjust Brightness", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            enhancer = ImageEnhance.Brightness(image)
            transformed_image = enhancer.enhance(brightness)

        elif transformation == "Transparency":
            transparency = st.slider("Adjust Transparency", min_value=0.0, max_value=1.0, value=1.0, step=0.1)
            if image.mode != 'RGBA':
                image = image.convert('RGBA')
            data = np.array(image)
            data[..., 3] = (data[..., 3] * transparency).astype(np.uint8)
            transformed_image = Image.fromarray(data, 'RGBA')

        elif transformation == "Shear":
            shear_factor = st.slider("Adjust Shear Factor", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
            img_array = np.array(image)
            rows, cols = img_array.shape[:2]
            transformed_image = image.transform((cols, rows), Image.AFFINE, (1, shear_factor, 0, 0, 1, 0))

        elif transformation == "Translate":
            tx = st.slider("Translate X", min_value=-200, max_value=200, value=0, step=1)
            ty = st.slider("Translate Y", min_value=-200, max_value=200, value=0, step=1)
            img_array = np.array(image)
            rows, cols = img_array.shape[:2]
            transformed_image = image.transform((cols, rows), Image.AFFINE, (1, 0, tx, 0, 1, ty))

        elif transformation == "Adjust RGB":
            # Adjust Red, Green, and Blue channels
            r_factor = st.slider("Adjust Red", min_value=0.0, max_value=2.0, value=1.0, step=0.1)
            g_factor = st.slider("Adjust Green", min_value=0.0, max_value=2.0, value=1.0, step=0.1)
            b_factor = st.slider("Adjust Blue", min_value=0.0, max_value=2.0, value=1.0, step=0.1)

            img_array = np.array(image)
            img_array[..., 0] = np.clip(img_array[..., 0] * r_factor, 0, 255)  # Red channel
            img_array[..., 1] = np.clip(img_array[..., 1] * g_factor, 0, 255)  # Green channel
            img_array[..., 2] = np.clip(img_array[..., 2] * b_factor, 0, 255)  # Blue channel
            transformed_image = Image.fromarray(img_array)

        st.image(transformed_image, caption="Transformed Image", use_container_width=True)

        # Pilih format file untuk unduhan
        download_format = st.selectbox("Select download format", ["PNG", "JPG", "PDF"])

        # Fungsi untuk konversi gambar
        def convert_image_for_download(image, format):
            img_io = io.BytesIO()
            if format == "PNG":
                image.save(img_io, "PNG")
            elif format == "JPG":
                image.save(img_io, "JPEG")
            elif format == "PDF":
                image.save(img_io, "PDF")
            img_io.seek(0)
            return img_io

        # Tampilkan tombol unduh setelah format dipilih
        if transformed_image:
            img_io = convert_image_for_download(transformed_image, download_format)
            st.download_button(
                label=f"Download as {download_format}",
                data=img_io,
                file_name=f"transformed_image.{download_format.lower()}",
                mime=f"image/{download_format.lower()}"
            )