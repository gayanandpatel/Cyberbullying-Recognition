import streamlit as st
from PIL import Image
# This function should contain all your ML model loading and prediction logic
from functions import custom_input_prediction

# --- Page Setup ---
st.set_page_config(page_title="Cyberbullying Recognition", page_icon="🛡️", layout="wide")

# --- Header ---
col1, col2 = st.columns([1, 10], vertical_alignment="center")
with col1:
    try:
        image = Image.open('images/logo.png')
        st.image(image, width=100)
    except FileNotFoundError:
        st.error("Logo not found.")
with col2:
    st.title("Cyberbullying Recognition")
    st.caption("An AI-powered tool for analyzing tweet content.")
st.divider()


left_column, right_column = st.columns(2)


with left_column:
    st.header("Analyze a Tweet")
    st.markdown("Enter the text below and click 'Analyze' to see the classification on the right.")

    with st.form(key='tweet_form'):
        tweet_input = st.text_area(
            "Tweet Text",
            height=200,
            placeholder="What's on your mind?",
            label_visibility="collapsed"
        )
        submitted = st.form_submit_button("Analyze Text", use_container_width=True)


with right_column:
    if submitted:
        if tweet_input:
            prediction = custom_input_prediction(tweet_input)
            image_mapping = {
                "Age": "images/age_cyberbullying.png",
                "Ethnicity": "images/ethnicity_cyberbullying.png",
                "Gender": "images/gender_cyberbullying.png",
                "Not Cyberbullying": "images/not_cyberbullying.png",
                "Other Cyberbullying": "images/other_cyberbullying.png",
                "Religion": "images/religion_cyberbullying.png"
            }

            st.header("Analysis Result")
            st.markdown("The model classified the tweet as:")

            with st.container(border=True):
                col_result, col_image = st.columns([2, 1], vertical_alignment="center")
                with col_result:
                    st.subheader(f"{prediction}")
                with col_image:
                    image_path = image_mapping.get(prediction)
                    if image_path:
                        try:
                            result_image = Image.open(image_path)
                           
                            st.image(result_image, width=200) 
                        except FileNotFoundError:
                            st.error("Img not found.")
        else:
            st.warning("Please enter a tweet in the text box on the left to analyze.")
    else:
        st.info("Your analysis results will appear here.")


# --- About Section ---
st.divider()
with st.expander("About this App"):
    st.markdown("""
        **How does it work?**
        1. You enter the text of a tweet on the left.
        2. Click 'Analyze Text' or press `Ctrl+Enter`.
        3. A pre-trained machine learning model classifies the text.
        4. The result is displayed instantly on the right.

        ***Disclaimer:*** *This application is for demonstration purposes only. Designed by Gayanand Patel*
        """)