import streamlit as st
from PIL import Image
from gemini_utility import gemini_pro_vision_response

# Configure Streamlit page settings
st.set_page_config(
    page_title="Image Captioning with Gemini-Pro",
    page_icon="📷",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Image captioning page
st.title("📷 Snap Narrate")

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if st.button("Generate Caption"):
    if uploaded_image:
        image = Image.open(uploaded_image)

        col1, col2 = st.columns(2)

        with col1:
            resized_img = image.resize((800, 500))
            st.image(resized_img)

        default_prompt = "write a short caption for this image"  # Change this prompt as per your requirement

        # Get the caption of the image from the gemini-pro-vision LLM
        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)
    else:
        st.error("Please upload an image.")
