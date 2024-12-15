import streamlit as st
from streamlit_option_menu import option_menu  # type: ignore
from PIL import Image
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="Project Final Exam", layout="centered")

# Atur path file lokal untuk gambar latar belakang dan logo
background_image_path = r"C:\Users\Lenovo\OneDrive\Gambar\Presiden t1.jpg"  # Pastikan path-nya benar
logo_image_path = "Logo PU-HD-2.jpg"  # Ganti dengan path logo yang sesuai

# Gunakan CSS untuk styling dan latar belakang
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('file:///{background_image_path}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center; /* Pusatkan teks dan elemen di tengah secara horizontal */
    }}
    .container {{
        text-align: center;
        margin-top: 20px;
    }}
    img {{
        display: block;
        margin: 0 auto; /* Pusatkan gambar */
        width: 300px; /* Ukuran logo */
    }}
    h2, h3 {{
        color: #333333;
        text-align: center; /* Pusatkan teks */
    }}
    </style>
    """, unsafe_allow_html=True)

# Menampilkan logo di tengah halaman
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.image(logo_image_path, width=300)  # Logo di tengah
st.markdown("</div>", unsafe_allow_html=True)

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
    st.markdown("<h2>INTRODUCTION</h2>", unsafe_allow_html=True)

    # Informasi anggota
    st.markdown("<h3>Group Members</h3>", unsafe_allow_html=True)
    st.write("Chyntia Adinda Ramadani (004202305053)")
    st.write("Ratu Enjelita (004202305032)")
    st.write("Salsabilla Clarysa Putri (004202305016)")

    # Program studi dan fakultas
    st.markdown("<h3>Program Study</h3>", unsafe_allow_html=True)
    st.write("Industrial Engineering")
    st.markdown("<h3>Faculty</h3>", unsafe_allow_html=True)
    st.write("Engineering")

    # Foto anggota
    st.markdown("<h3>Member Photo</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("cinta2.jpg", caption="Chyntia Adinda", use_container_width=True)
    with col2:
        st.image("ratu2.jpg", caption="Ratu Enjelita", use_container_width=True)
    with col3:
        st.image("salsa2.jpg", caption="Salsabilla Clarysa", use_container_width=True) 

# Menu "Application"
elif select == "Application":
    st.markdown("<h2>APPLICATION DESCRIPTION</h2>", unsafe_allow_html=True)
    st.write(
        "This application allows users to perform various transformations on images, such as rotation, skew, zoom, scale, resize, brightness adjustment, and transparency."
    )

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        transformation = st.selectbox(
            "Select Transformation", 
            ["Select", "Rotate", "Translate", "Scale", "Shear", "Resize", "Skew", "Brightness", "Transparency", "Remove Background"]
        )

        if transformation == "Rotate":
            angle = st.slider("Enter Rotation Angle (degrees)", min_value=0, max_value=360, value=90, step=1)
            rotated_image = image.rotate(angle)
            st.image(rotated_image, caption=f"Rotated Image by {angle}°", use_column_width=True)

        elif transformation == "Translate":
            tx = st.slider("Translate X (pixels)", min_value=-500, max_value=500, value=0, step=1)
            ty = st.slider("Translate Y (pixels)", min_value=-500, max_value=500, value=0, step=1)
            img_array = np.array(image)
            M = np.float32([[1, 0, tx], [0, 1, ty]])
            translated_image = cv2.warpAffine(img_array, M, (img_array.shape[1], img_array.shape[0]))
            st.image(translated_image, caption="Translated Image", use_column_width=True)
