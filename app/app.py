import streamlit as st
import pandas as pd
import joblib
import os

# --- PATHS ---
# Get the absolute path of the current script
APP_DIR = os.path.dirname(os.path.abspath(__file__))
# Go up one level to the project root
PROJECT_ROOT = os.path.dirname(APP_DIR)
# Define paths to model and columns
MODEL_PATH = os.path.join(PROJECT_ROOT, 'models', 'random_forest_model.joblib')
COLUMNS_PATH = os.path.join(PROJECT_ROOT, 'models', 'model_columns.joblib')

# --- LOAD MODEL AND COLUMNS ---
try:
    # Corrected the variable name from MODEL__PATH to MODEL_PATH
    model = joblib.load(MODEL_PATH)
    model_columns = joblib.load(COLUMNS_PATH)
except FileNotFoundError:
    st.error("FATAL ERROR: The trained model or column file was not found.")
    st.info("Please run the training script first from your terminal: `python src/train_model.py`")
    st.stop() # Stop the app from running further

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR STYLING ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# You can create a style.css file in the same `app` folder, or inject directly
# For simplicity, we'll inject it directly.
st.markdown("""
<style>
/* Main page styling */
.main .block-container {
    padding-top: 2rem;
}
h1 {
    font-size: 2.8rem;
    text-align: center;
    font-weight: 700;
    color: #FF4B4B; /* Streamlit's red */
    text-shadow: 2px 2px 4px #000000;
}
p {
    font-size: 1.1rem;
}

/* Sidebar styling */
.st-emotion-cache-16txtl3 {
    padding: 2rem 1rem;
}

/* Button styling */
div.stButton > button {
    background-color: #FF4B4B;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    padding: 12px 24px;
    width: 100%;
    font-size: 1.1em;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    transition: all 0.2s ease-in-out;
}
div.stButton > button:hover {
    transform: scale(1.02);
    background-color: #E03C3C;
    box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.3);
}

/* Success box styling */
div.stAlert {
    border-radius: 12px;
    border: 1px solid #00B36B;
    background-color: #1A3D30;
    text-align: center;
}
div.stAlert p {
    font-size: 1.5rem;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# --- SIDEBAR FOR USER INPUTS ---
with st.sidebar:
    st.header("Enter Student Information")

    previous_percentage = st.number_input(
        label='Previous Year Percentage (%)', min_value=0, max_value=100, value=80, step=1
    )
    study_hours = st.number_input(
        label='Study Hours per Day', min_value=0.0, max_value=12.0, value=5.0, step=0.5
    )
    attendance_percentage = st.number_input(
        label='Attendance Percentage (%)', min_value=0, max_value=100, value=90, step=1
    )
    parental_education = st.selectbox(
        'Parental Education Level',
        ('High School', 'Graduate', 'Postgraduate', 'Doctorate'), index=1
    )
    has_tuition = st.selectbox('Has Tuition?', ('Yes', 'No'), index=0)
    board = st.selectbox('Educational Board', ('CBSE', 'ICSE', 'State Board'), index=0)

    # The prediction button is also in the sidebar
    predict_button = st.button('Predict Score', type="primary")

# --- MAIN PAGE LAYOUT ---
st.title('🎓 Student Performance Predictor')
st.markdown("This application predicts a student's final score. Please provide the required information in the sidebar.")
st.markdown("---")

# --- PREDICTION LOGIC ---
if predict_button:
    # Create a DataFrame from the user's input
    input_data = {
        'PreviousYearPercentage': [previous_percentage],
        'StudyHoursPerDay': [study_hours],
        'AttendancePercentage': [attendance_percentage],
        'ParentalEducation': [parental_education],
        'HasTuition': [has_tuition],
        'Board': [board]
    }
    input_df = pd.DataFrame(input_data)

    # One-hot encode the categorical features
    input_df_encoded = pd.get_dummies(input_df)

    # Align the input DataFrame with the model's training columns
    final_input_df = input_df_encoded.reindex(columns=model_columns, fill_value=0)

    # Make the prediction
    prediction = model.predict(final_input_df)

    # Display the result in the main area
    st.success(f'Predicted Final Score: {prediction[0]:.2f}%')

