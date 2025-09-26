import streamlit as st
from PIL import Image
# This function should contain all your ML model loading and prediction logic
from functions import custom_input_prediction

# --- Page Setup ---
st.set_page_config(page_title="Cyberbullying Recognition", page_icon="🛡️", layout="centered")

# --- Redesigned Header ---
col1, col2 = st.columns([1, 5], vertical_alignment="center")

with col1:
    try:
        image = Image.open('images/logo.png')
        st.image(image, width=100)
    except FileNotFoundError:
        st.error("Logo not found.")

with col2:
    st.title("Cyberbullying Recognition")
    st.caption("An AI-powered tool for analyzing tweet content.")

st.write("""
This app predicts if a tweet falls into one of 6 categories: **Age, Ethnicity, Gender, Religion, Other Cyberbullying,** or **Not Cyberbullying.**
""")
st.divider()

# --- Tweet Input Form ---
# By wrapping the input and button in a form, both Ctrl+Enter and the button click will work.
st.header('Enter Tweet for Analysis')

with st.form(key='tweet_form'):
    tweet_input = st.text_area(
        "Tweet Input",
        height=150,
        placeholder="Paste or type a tweet here...",
        label_visibility="collapsed"
    )
    
    # Use st.form_submit_button instead of st.button
    submitted = st.form_submit_button("Analyze Text")


# --- Prediction and Output ---
# This logic now runs when the form is submitted.
if submitted:
    if tweet_input:
        st.divider()

        prediction = custom_input_prediction(tweet_input)

        image_mapping = {
            "Age": "images/age_cyberbullying.png",
            "Ethnicity": "images/ethnicity_cyberbullying.png",
            "Gender": "images/gender_cyberbullying.png",
            "Not Cyberbullying": "images/not_cyberbullying.png",
            "Other Cyberbullying": "images/other_cyberbullying.png",
            "Religion": "images/religion_cyberbullying.png"
        }

        st.subheader("Analysis Result")
        st.info(f"The tweet is classified as: **{prediction}**")

        image_path = image_mapping.get(prediction)
        if image_path:
            try:
                result_image = Image.open(image_path)
                st.image(result_image, caption=f"Category: {prediction}", use_container_width=True)
            except FileNotFoundError:
                st.error(f"Result image not found at '{image_path}'.")
        else:
            st.warning("No result image available for this prediction category.")
    else:
        st.warning("Please enter a tweet to analyze.")

st.divider()

# --- About Section ---
with st.expander("About this App"):
    st.markdown("""
        **How does it work?**
        1. You enter the text of a tweet into the input box.
        2. Click the 'Analyze Text' button or press `Ctrl+Enter`.
        3. Our pre-trained machine learning model analyzes the text.
        4. The model predicts the most likely category of cyberbullying.
        5. The prediction is displayed along with a corresponding image.

        ***Disclaimer:*** *This application is for demonstration purposes only and should not be used for making real-world decisions.*
        """)