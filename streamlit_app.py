import streamlit as st
from streamlit_option_menu import option_menu  # type: ignore
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Project Final Exam", layout="centered")

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
