
import streamlit as st
from PIL import Image
# This function should contain all your ML model loading and prediction logic
from functions import custom_input_prediction

# --- Page Setup ---
# Set the page title and icon
st.set_page_config(page_title="Cyberbullying Recognition", page_icon="🛡️")

# --- Header and Logo ---
try:
    image = Image.open('images/logo.png')
    st.image(image, use_container_width=True)
except FileNotFoundError:
    st.error("Logo image not found. Make sure 'images/logo.png' is in the correct folder.")

st.title("Cyberbullying Tweet Recognition App")

st.write("""
This app predicts the nature of a tweet across 6 categories:
- Age
- Ethnicity
- Gender
- Religion
- Other Cyberbullying
- Not Cyberbullying
""")
st.divider()

# --- Tweet Input ---
st.header('Enter Tweet')
tweet_input = st.text_area("Tweet Input", height=150, placeholder="What's on your mind?", label_visibility="collapsed")

st.divider()

# --- Prediction and Output ---
# This block only runs if the user has entered some text
if tweet_input:
    # Display the user's input
    st.subheader("Entered Tweet")
    st.write(tweet_input)

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
    st.subheader("Prediction")
    st.info(f"The tweet is classified as: **{prediction}**")

    # Display the corresponding image for the prediction
    image_path = image_mapping.get(prediction)
    if image_path:
        try:
            result_image = Image.open(image_path)
            st.image(result_image, use_container_width=True)
        except FileNotFoundError:
            st.error(f"Result image not found at '{image_path}'.")
    else:
        st.warning("No result image available for this prediction category.")

else:
    # Message to show when no text is entered
    st.info("Please enter a tweet in the text box above to see a prediction.")

st.divider()

# --- About Section ---
with st.expander("About this App"):
    st.markdown("""
        **How does it work?**
        1. You enter text from a tweet into the input box.
        2. The app processes this text.
        3. A pre-trained machine learning model predicts which category of cyberbullying the tweet belongs to.
        4. The prediction and a corresponding image are displayed.

        *This application is for demonstration purposes only.*
    """)