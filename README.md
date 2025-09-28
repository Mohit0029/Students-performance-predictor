"# ?? Student Performance Analysis Project" 
Student Performance Prediction 🎓
This project analyzes key factors affecting student academic performance and deploys a machine learning model as an interactive web application to predict final scores.

Overview
In today's data-driven world, understanding the factors that contribute to academic success is crucial. This project provides a complete, end-to-end solution for predicting student performance based on demographic, socio-economic, and academic data.

The project workflow includes:

Data Cleaning and Preparation

Exploratory Data Analysis (EDA) to uncover key insights

Model Training using a Random Forest Regressor

Deployment as a user-friendly web application using Streamlit

🚀 Tech Stack
Backend: Python

Data Manipulation: Pandas, NumPy

Machine Learning: Scikit-learn

Web Framework: Streamlit

Model Persistence: Joblib

✨ Features
Interactive UI: A simple and intuitive web interface for users to input student data.

Real-Time Predictions: Get instant final score predictions based on the model's analysis.

Modular Codebase: The source code is organized into a clean, professional structure for maintainability and scalability.

🔧How to Run
To run this project locally, please follow these steps:

1. Clone the repository:

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd student-performance-analysis

2. Create and activate a virtual environment:

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install the required dependencies:

pip install -r requirements.txt

4. Run the model training script (optional, as the model is already provided):

python src/train_model.py

5. Run the Streamlit application:

streamlit run app/app.py

The application will open in your web browser.

📈 Results
The Random Forest Regressor model was trained and evaluated, achieving an R-squared (R²) score of 99.62% on the test set. This indicates a very high level of accuracy in predicting student scores based on the provided features in the synthetic dataset.
