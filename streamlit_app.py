import streamlit as st
from streamlit_option_menu import option_menu  # type: ignore
from PIL import Image
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="Project Final Exam", layout="centered")

# Atur path file lokal untuk gambar latar belakang dan logo
background_image_path = r"C:\Users\Lenovo\OneDrive\Gambar\Presiden t1.jpg"  # Pastikan path-nya benar
logo_image_path = "President_University_Logo.png"  # Ganti dengan path logo yang sesuai

# Gunakan CSS untuk styling dan pusatkan semua elemen di halaman utama
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
        flex-direction: column; /* Elemen berada di tengah secara vertikal */
        text-align: center;    /* Elemen berada di tengah secara horizontal */
    }}
    .container {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: rgba(255, 255, 255, 0.8); /* Warna latar belakang semi-transparan */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    }}
    .logo {{
        width: 200px; /* Ukuran logo */
        margin-bottom: 20px; /* Jarak antara logo dan teks */
    }}
    .text {{
        font-size: 24px; /* Ukuran teks */
        color: #333333; /* Warna teks */
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# Menampilkan logo dan teks di tengah halaman
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown(f"<img src='file:///{logo_image_path}' class='logo'>", unsafe_allow_html=True)
st.markdown("<p class='text'>Project Final Exam</p>", unsafe_allow_html=True)
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
    st.markdown("<h2 style='text-align: center;'>INTRODUCTION</h2>", unsafe_allow_html=True)
    st.write("**Group Members:**")
    st.write("- Chyntia Adinda Ramadani (004202305053)")
    st.write("- Ratu Enjelita (004202305032)")
    st.write("- Salsabilla Clarysa Putri (004202305016)")
    st.write("**Program Study:** Industrial Engineering")
    st.write("**Faculty:** Engineering")

# Menu "Application"
elif select == "Application":
    st.markdown("<h2 style='text-align: center;'>APPLICATION DESCRIPTION</h2>", unsafe_allow_html=True)
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
