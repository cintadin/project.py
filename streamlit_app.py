import streamlit as st
from PIL import Image
import io

# Konfigurasi halaman
st.set_page_config(page_title="Rotate and Download Image", layout="centered")

# Sidebar untuk menampilkan nama anggota
with st.sidebar:
    st.image("Presiden_University_Logo.png")
    st.title("Group Members")
    st.write("1. Chyntia Adinda Ramadani")
    st.write("2. Salsabilla Clarysa Putri")
    st.write("3. Ratu Enjelita")

# Judul halaman
st.title("Image Rotation and Download Application")

# Upload gambar
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Mengecek jika gambar diupload
if uploaded_file is not None:
    # Membuka gambar
    image = Image.open(uploaded_file)

    # Menampilkan gambar yang diupload
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Input sudut rotasi
    angle = st.slider("Select rotation angle", min_value=0, max_value=360, value=90, step=1)

    # Melakukan rotasi
    rotated_image = image.rotate(angle)

    # Menampilkan gambar yang telah diputar
    st.image(rotated_image, caption=f"Rotated Image by {angle}°", use_container_width=True)

    # Menyimpan gambar rotasi sementara dalam format yang bisa didownload
    def image_to_bytes(img, format='PNG'):
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=format)
        img_byte_arr.seek(0)
        return img_byte_arr

    # Fitur untuk mendownload gambar hasil rotasi
    st.subheader("Download Rotated Image")
    
    # Pilihan format file untuk download
    download_format = st.selectbox("Choose download format", ["PNG", "JPEG", "PDF"])

    if download_format == "PNG":
        img_bytes = image_to_bytes(rotated_image, format="PNG")
        st.download_button(
            label="Download as PNG",
            data=img_bytes,
            file_name="rotated_image.png",
            mime="image/png"
        )
    elif download_format == "JPEG":
        img_bytes = image_to_bytes(rotated_image, format="JPEG")
        st.download_button(
            label="Download as JPEG",
            data=img_bytes,
            file_name="rotated_image.jpg",
            mime="image/jpeg"
        )
    elif download_format == "PDF":
        # Convert image to PDF
        pdf_bytes = io.BytesIO()
        rotated_image.convert("RGB").save(pdf_bytes, format="PDF")
        pdf_bytes.seek(0)
        st.download_button(
            label="Download as PDF",
            data=pdf_bytes,
            file_name="rotated_image.pdf",
            mime="application/pdf"
        )
