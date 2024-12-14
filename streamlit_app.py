import streamlit as st
from streamlit_option_menu import option_menu  # type: ignore
from PIL import Image
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="Project Final Exam", layout="centered")

# Atur path file lokal untuk gambar latar belakang dan logo
background_image_path = r"C:\Users\Lenovo\OneDrive\Gambar\Presiden t1.jpg"  # Pastikan path-nya benar
logo_image_path = r"C:\Users\Lenovo\belajar\LINEAR ALGEBRA\project final exam\President_University_Logo.png"  # Ganti dengan path logo yang sesuai

# Gunakan CSS untuk menambahkan gambar latar belakang dan styling lainnya
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
        text-align: center;  /* Menambahkan agar semua teks terpusat */
    }}
    .container {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        text-align: center;  /* Menambahkan agar teks di dalam container terpusat */
    }}
    .title {{
        font-size: 36px;
        font-weight: bold;
        color: #333333;
    }}
    .subheader {{
        font-size: 32px;  /* Memperbesar ukuran font subheader */
        font-weight: bold;
        color: #4CAF50;
    }}
    .content {{
        font-size: 18px;
        color: #555555;
    }}
    .logo {{
        width: 150px;  /* Menentukan ukuran logo */
        margin-bottom: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# Menampilkan logo di atas halaman
st.markdown(f'<img class="logo" src="file:///{r"C:\Users\Lenovo\belajar\LINEAR ALGEBRA\project final exam\President_University_Logo.png"}" alt="Logo">', unsafe_allow_html=True)

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
    st.markdown("<p class='content'>Chyntia Adinda Ramadani (004202305053)</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Ratu Enjelita (004202305032)</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Salsabilla Clarysa Putri (004202305016)</p>", unsafe_allow_html=True)

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
        st.image("ratu2.jpg", caption="Ratu Enjelita", use_container_width=True)
    with col3:
       st.image("salsa2.jpg", caption="Salsabilla Clarysa", use_container_width=True) 

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
