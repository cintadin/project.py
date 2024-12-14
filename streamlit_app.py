import streamlit as st
from streamlit_option_menu import option_menu  # type: ignore
from PIL import Image
import numpy as np
import base64

# Konfigurasi halaman
st.set_page_config(page_title="Project Final Exam", layout="centered")

# Fungsi untuk mengonversi gambar ke base64 (untuk latar belakang)
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Pilihan untuk mengunggah gambar latar belakang
uploaded_bg_image = st.sidebar.file_uploader("Upload Background Image", type=["jpg", "png", "jpeg"])

# Jika gambar latar belakang diunggah, gunakan gambar tersebut
if uploaded_bg_image is not None:
    img = get_img_as_base64(uploaded_bg_image)
    page_bg_img = f"""
    <style>
    body {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        margin: 0;
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
    """
else:
    # Gambar latar belakang default jika tidak ada file yang diunggah
    background_image_path = "https://images.unsplash.com/photo-1501426026826-31c667bdf23d"  # Gambar default
    page_bg_img = f"""
    <style>
    body {{
        background-image: url("{background_image_path}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        margin: 0;
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
    """

# Terapkan CSS untuk latar belakang
st.markdown(page_bg_img, unsafe_allow_html=True)

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

        # Pilih jenis transformasi
        transformation = st.selectbox("Select Transformation", ["Select", "Rotate", "Translate", "Scale", "Shear", "Resize", "Skew", "Brightness", "Transparency", "Remove Background"])

        if transformation == "Rotate":
            angle = st.slider("Enter Rotation Angle (degrees)", min_value=0, max_value=360, value=90, step=1)
            rotated_image = image.rotate(angle)
            st.image(rotated_image, caption=f"Rotated Image by {angle}°", use_container_width=True)

        elif transformation == "Translate":
            tx = st.slider("Translate X (pixels)", min_value=-500, max_value=500, value=0, step=1)
            ty = st.slider("Translate Y (pixels)", min_value=-500, max_value=500, value=0, step=1)
            img_array = np.array(image)  # Konversi gambar PIL ke numpy array
            M = np.float32([[1, 0, tx], [0, 1, ty]])  # Matriks translasi
            translated_image = cv2.warpAffine(img_array, M, (img_array.shape[1], img_array.shape[0]))
            st.image(translated_image, caption="Translated Image", use_container_width=True)
