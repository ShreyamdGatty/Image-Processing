import streamlit as st
import cv2
import numpy as np

# Function to read an image from the uploaded file
def read_image(uploaded_file):
    img_array = np.frombuffer(uploaded_file.read(), np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return image


# CSS for background image and custom text styles
def add_custom_css():
    background_image_url = "https://images.alphacoders.com/853/85391.jpg"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# Add custom CSS
add_custom_css()

# Streamlit UI
st.title("Image Processing")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Read the image from the uploaded file
        image = read_image(uploaded_file)

        # Resize the image
        new_width, new_height = 300, 300
        resized_image = cv2.resize(image, (new_width, new_height))

        # Convert to grayscale
        gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        # Convert to black and white using thresholding
        threshold_value = 127
        _, bw_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

        # Crop the image
        x_start, y_start = 150, 150  # Adjust crop dimensions
        x_end, y_end = 250, 250
        crop_image = resized_image[y_start:y_end, x_start:x_end]

        # Display images
        st.image(resized_image, caption="Resized Image", use_container_width=True)
        st.image(gray_image, caption="Grayscale Image", use_container_width=True, channels="GRAY")
        st.image(bw_image, caption="Black and White Image", use_container_width=True, channels="GRAY")
        st.image(crop_image, caption="Cropped Image", use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred while processing the image: {e}")
else:
    st.warning("Please upload an image file.")




