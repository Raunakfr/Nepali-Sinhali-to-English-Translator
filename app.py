# app.py
import streamlit as st
from ocr_module import extract_text_from_image, extract_text_from_pdf
from translation_module import translate_text

st.title("Nepali & Sinhalese OCR + Translation")

# Select language manually
lang_choice = st.selectbox("Select Language", ["Nepali", "Sinhalese"])
ocr_lang = "ne" if lang_choice == "Nepali" else "si"

# File uploader
uploaded_file = st.file_uploader("Upload Image or PDF", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file:
    # OCR
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file, ocr_lang)
    else:
        text = extract_text_from_image(uploaded_file, ocr_lang)

    st.subheader("Extracted Text")
    st.text_area("OCR Output", text, height=200)

    # Translation
    translated_text = translate_text(text, ocr_lang)
    st.subheader("Translated Text")
    st.text_area("English Translation", translated_text, height=200)
