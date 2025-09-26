import streamlit as st
from PIL import Image
# This function should contain all your ML model loading and prediction logic
from functions import custom_input_prediction

# --- Page Setup ---
# Set the page title and icon for a professional touch in the browser tab
st.set_page_config(page_title="Cyberbullying Recognition", page_icon="🛡️", layout="centered")

# --- Redesigned Header ---
# We use columns to create a balanced, modern layout with the logo and title next to each other.
# The 'vertical_alignment' ensures they look good together.
col1, col2 = st.columns([1, 5], vertical_alignment="center")

with col1:
    try:
        # Open the logo image
        image = Image.open('images/logo.png')
        # Control the size of the logo by setting a specific width
        st.image(image, width=100)
    except FileNotFoundError:
        # Display a simple error if the logo isn't where it's supposed to be
        st.error("Logo not found.")

with col2:
    # Main title and a brief, professional subtitle
    st.title("Cyberbullying Recognition")
    st.caption("An AI-powered tool for analyzing tweet content.")

st.write("""
This app predicts if a tweet falls into one of 6 categories: **Age, Ethnicity, Gender, Religion, Other Cyberbullying,** or **Not Cyberbullying.**
""")
st.divider()

# --- Tweet Input ---
st.header('Enter Tweet for Analysis')
tweet_input = st.text_area(
    "Tweet Input",
    height=150,
    placeholder="Paste or type a tweet here...",
    label_visibility="collapsed"
)

# Add a button to trigger the analysis. Using type="primary" makes it stand out.
analyze_button = st.button("Analyze Text", type="primary")

# --- Prediction and Output ---
# The analysis now runs only when the 'Analyze Text' button is clicked.
if analyze_button:
    # First, check if the user has actually entered any text.
    if tweet_input:
        # Add a divider for clear separation between input and output sections
        st.divider()

        # Perform prediction using the function from functions.py
        prediction = custom_input_prediction(tweet_input)

        # A dictionary to map prediction results to their corresponding images
        image_mapping = {
            "Age": "images/age_cyberbullying.png",
            "Ethnicity": "images/ethnicity_cyberbullying.png",
            "Gender": "images/gender_cyberbullying.png",
            "Not Cyberbullying": "images/not_cyberbullying.png",
            "Other Cyberbullying": "images/other_cyberbullying.png",
            "Religion": "images/religion_cyberbullying.png"
        }

        # Display the prediction result
        st.subheader("Analysis Result")
        st.info(f"The tweet is classified as: **{prediction}**")

        # Display the corresponding image for the prediction
        image_path = image_mapping.get(prediction)
        if image_path:
            try:
                result_image = Image.open(image_path)
                # Add a caption to the result image for better context
                st.image(result_image, caption=f"Category: {prediction}", use_container_width=True)
            except FileNotFoundError:
                st.error(f"Result image not found at '{image_path}'.")
        else:
            st.warning("No result image available for this prediction category.")
    else:
        # If the button is clicked with no text, show a warning.
        st.warning("Please enter a tweet to analyze.")


st.divider()

# --- About Section ---
with st.expander("About this App"):
    st.markdown("""
        **How does it work?**
        1. You enter the text of a tweet into the input box.
        2. Click the 'Analyze Text' button.
        3. Our pre-trained machine learning model analyzes the text.
        4. The model predicts the most likely category of cyberbullying.
        5. The prediction is displayed along with a corresponding image.

        ***Disclaimer:*** *This application is for demonstration purposes only and should not be used for making real-world decisions.*
        """)