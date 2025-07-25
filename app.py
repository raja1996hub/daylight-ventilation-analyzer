import streamlit as st
import pytesseract
from PIL import Image
from analyze import analyze_description

# 👁 Set tesseract executable path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 🖼️ UI
st.set_page_config(page_title="🌞 Daylight & Ventilation Analyzer")
st.title("🌞 Daylight & Ventilation Analyzer")
st.markdown("Upload your sketch, floor plan, or text description to get AI feedback on daylight and ventilation potential.")

input_method = st.radio("Choose input method:", ["Upload Image", "Enter Text"])

raw_text = ""

if input_method == "Upload Image":
    uploaded_file = st.file_uploader("Upload a PNG, JPG, or JPEG file", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Plan", use_container_width=True)
        image = Image.open(uploaded_file)
        raw_text = pytesseract.image_to_string(image)
        st.subheader("📝 OCR Extracted Text")
        st.code(raw_text)

else:
    raw_text = st.text_area("✍️ Enter your design description here", height=200)

# 🔍 Analyze button
if st.button("🔎 Analyze Daylight & Ventilation") and raw_text.strip():
    with st.spinner("Analyzing..."):
        result = analyze_description(raw_text)
        st.success("✅ Analysis Complete")
        st.subheader("📋 Result:")
        st.markdown(result)
