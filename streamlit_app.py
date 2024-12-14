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

# Navigasi sidebar
with st.sidebar:
    select = option_menu(
        "Project Final Exam", 
        ["Introduction", "Application"], 
        default_index=0
    )

# Menambahkan gambar latar belakang dengan CSS
background_image = "C:\Users\Lenovo\OneDrive\Gambar\pleciden.jpeg"  # Ganti dengan path ke gambar latar belakang Anda
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('{background_image}');
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

        # Pilih jenis transformasi
        transformation = st.selectbox("Select Transformation", ["Select", "Rotate", "Translate", "Scale", "Shear", "Resize", "Skew", "Brightness", "Transparency", "Remove Background"])

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
                (1, 0, tx, 0, 1, ty),
                resample=Image.BICUBIC
            )
            st.image(translated_image, caption="Translated Image", use_container_width=True)

        elif transformation == "Scale":
            scale_factor = st.slider("Enter Scale Factor", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
            width, height = image.size
            new_size = (int(width * scale_factor), int(height * scale_factor))
            scaled_image = image.resize(new_size)
            st.image(scaled_image, caption="Scaled Image", use_container_width=True)

        elif transformation == "Shear":
            shear_factor = st.slider("Enter Shear Factor", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
            shear_matrix = (1, shear_factor, 0, 0, 1, 0)
            sheared_image = image.transform(image.size, Image.AFFINE, shear_matrix, resample=Image.BICUBIC)
            st.image(sheared_image, caption="Sheared Image", use_container_width=True)

        elif transformation == "Resize":
            new_width = st.slider("Enter New Width", min_value=100, max_value=2000, value=image.width, step=10)
            new_height = st.slider("Enter New Height", min_value=100, max_value=2000, value=image.height, step=10)
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, caption="Resized Image", use_container_width=True)

        elif transformation == "Skew":
            skew_factor = st.slider("Enter Skew Factor", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            skew_matrix = (1, skew_factor, 0, 0, 1, 0)
            skewed_image = image.transform(image.size, Image.AFFINE, skew_matrix, resample=Image.BICUBIC)
            st.image(skewed_image, caption="Skewed Image", use_container_width=True)

        elif transformation == "Brightness":
            brightness = st.slider("Adjust Brightness", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            enhancer = ImageEnhance.Brightness(image)
            bright_image = enhancer.enhance(brightness)
            st.image(bright_image, caption="Brightness Adjusted Image", use_container_width=True)

        elif transformation == "Transparency":
            transparency = st.slider("Adjust Transparency", min_value=0.0, max_value=1.0, value=1.0, step=0.1)
            if image.mode != 'RGBA':
                image = image.convert('RGBA')
            data = np.array(image)
            data[..., 3] = (data[..., 3] * transparency).astype(np.uint8)
            transparent_image = Image.fromarray(data, 'RGBA')
            st.image(transparent_image, caption="Transparency Adjusted Image", use_container_width=True)

        elif transformation == "Remove Background":
            st.warning("Remove background feature requires additional processing, and currently, we don't have the implementation for this.")
