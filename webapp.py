import streamlit as st
from PIL import Image
import time
import random

# This function would normally be in a separate file.
# For demonstration, we'll create a mock function here.
def mock_custom_input_prediction(tweet_text):
    """
    Mock function to simulate model prediction.
    In a real app, this would call your actual machine learning model.
    """
    # Simulate a delay for model processing
    time.sleep(1.5)
    
    # Possible prediction categories
    categories = [
        "Age", "Ethnicity", "Gender", "Religion",
        "Other Cyberbullying", "Not Cyberbullying"
    ]
    
    # Randomly choose a category and a confidence score
    prediction = random.choice(categories)
    confidence = random.uniform(0.75, 0.98)
    
    return prediction, confidence

# --- Page Configuration ---
st.set_page_config(
    page_title="Cyberbullying Recognition",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for modern UI elements ---
st.markdown("""
<style>
    /* Main container styling */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Card-like containers for input and output */
    .st-emotion-cache-1r6slb0, .st-emotion-cache-1r6slb0 {
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        background-color: #ffffff;
    }
    
    /* Style the title */
    h1 {
        color: #1e3a8a; /* A deep blue color */
        text-align: center;
    }
    
    /* Style the header */
    h2 {
        color: #3b5998; /* A softer blue */
    }

    /* Style the buttons */
    .stButton>button {
        border-radius: 8px;
        border: 1px solid #1e3a8a;
        color: #ffffff;
        background-color: #1e3a8a;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #2563eb;
        border-color: #2563eb;
    }

    /* Center the logo */
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


# --- Session State Initialization ---
# This helps maintain state between reruns
if 'prediction' not in st.session_state:
    st.session_state.prediction = None
if 'confidence' not in st.session_state:
    st.session_state.confidence = None
if 'tweet_input' not in st.session_state:
    st.session_state.tweet_input = ""


# --- Header and Logo ---
try:
    image = Image.open('images/logo.png')
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image(image, width=150)
    st.markdown('</div>', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Logo image not found at 'images/logo.png'. Skipping logo.")

st.title("Cyberbullying Tweet Recognition")
st.markdown("<p style='text-align: center; color: #4b5563;'>A modern tool to analyze and classify harmful content online.</p>", unsafe_allow_html=True)
st.markdown("---")


# --- Main Layout (Input and Output side-by-side) ---
col1, col2 = st.columns([0.55, 0.45], gap="large")

with col1:
    st.header("Tweet Analysis")
    st.write("Enter the text of a tweet below. Our AI model will predict if it falls into one of six categories, including various types of cyberbullying.")
    
    tweet_input = st.text_area(
        "Tweet Content",
        height=180,
        placeholder="Example: 'You are not smart enough to have an opinion on this subject.'",
        label_visibility="collapsed",
        key="tweet_input_area"
    )

    if st.button("Analyze Tweet", type="primary"):
        if tweet_input:
            # Show a spinner while processing
            with st.spinner('Analyzing the tweet... Our model is thinking.'):
                prediction, confidence = mock_custom_input_prediction(tweet_input)
                # Store results in session state
                st.session_state.prediction = prediction
                st.session_state.confidence = confidence
                st.session_state.tweet_input = tweet_input
        else:
            st.warning("Please enter some text to analyze.")

    # --- About Section ---
    with st.expander("About This Application"):
        st.markdown("""
            **How does it work?**
            1. **Input**: You provide the text from a tweet.
            2. **Processing**: The text is processed using natural language processing techniques.
            3. **Prediction**: A pre-trained machine learning model classifies the text into one of the following categories: *Age, Ethnicity, Gender, Religion, Other Cyberbullying, or Not Cyberbullying*.
            4. **Output**: The application displays the prediction along with a confidence score.

            *Disclaimer: This application is a demonstration and should not be used for real-world moderation without further validation.*
        """)

with col2:
    st.header("Analysis Result")

    if st.session_state.prediction:
        # --- Define colors and icons for each category ---
        category_info = {
            "Age": {"icon": "🎂", "color": "#ef4444"},
            "Ethnicity": {"icon": "🌍", "color": "#f97316"},
            "Gender": {"icon": "♀️♂️", "color": "#ec4899"},
            "Religion": {"icon": "⛪", "color": "#8b5cf6"},
            "Other Cyberbullying": {"icon": "❗", "color": "#d946ef"},
            "Not Cyberbullying": {"icon": "✅", "color": "#22c55e"}
        }

        # Get info for the current prediction
        prediction = st.session_state.prediction
        info = category_info.get(prediction, {"icon": "❓", "color": "#6b7280"})
        icon = info["icon"]
        
        # Display the analyzed tweet
        st.write("**Analyzed Tweet:**")
        st.info(st.session_state.tweet_input)
        
        # Display the result using a metric
        st.metric(label="**Prediction Category**", value=f"{icon} {prediction}")

        # Display confidence score
        st.write("**Confidence Score:**")
        st.progress(st.session_state.confidence)
        st.markdown(f"<p style='text-align: right; color: #4b5563; margin-top: -10px;'>{st.session_state.confidence:.2%}</p>", unsafe_allow_html=True)
        
    else:
        # --- Initial placeholder state ---
        st.info("Your analysis results will appear here once you enter a tweet and click 'Analyze'.")
        st.image("https://placehold.co/600x400/f0f2f6/3b5998?text=Waiting+for+Input...&font=inter", use_column_width=True)
