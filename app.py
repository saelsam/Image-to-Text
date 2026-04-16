import streamlit as st
import pytesseract
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image to Text App", layout="centered")

st.title("📷 Image to Text App")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # tampilkan gambar
    image = Image.open(uploaded_file)
    display_image = image.copy()
    display_image.thumbnail((500, 500))
    st.image(display_image, caption="Uploaded Image", use_container_width=True)

    # konversi ke numpy array
    img = np.array(image)

    # preprocessing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (5,5), 0)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    #st.subheader("🛠️ Preprocessing")
    #foto abu abu
    #st.image(thresh, caption="Hasil threshold", use_container_width=True)

    # OCR
    with st.spinner("Membaca teks..."):
        text = pytesseract.image_to_string(thresh)

    st.subheader("📄 Hasil Teks")
    st.text_area("Output:", text, height=200)

    # tombol download hasil
    st.download_button(
        label="Download text",
        data=text,
        file_name="text result.txt"
    )