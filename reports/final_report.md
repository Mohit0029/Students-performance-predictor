"# Final Report and Insights"

Final Report and Insights: Student Performance Analysis

1\. Project Objective

The primary objective of this project was to analyze the factors influencing student academic performance and to develop a machine learning model capable of predicting a student's final score with high accuracy. The project culminated in the deployment of this model as an interactive web application using Streamlit.



2\. Data Overview

The analysis was performed on a synthetic dataset of 1,500 Indian students. The dataset contained a rich set of features, including:



Student Demographics: Age, Gender, City, State



Academic Background: Educational Board, Previous Year Percentage, Attendance



Socio-Economic Factors: Parental Education, Parental Occupation, Family Income



Study Habits: Study Hours per Day, Tuition Status



The data was found to be complete and well-structured, with no missing values or duplicate entries, providing a solid foundation for analysis and modeling.



3\. Key Insights from Exploratory Data Analysis (EDA)

The EDA phase focused on visualizing the data to uncover patterns and relationships. The following key insights were derived:



Insight 1: Study Hours and Previous Performance are Strong Indicators

The scatter plot of Final Score vs. Study Hours per Day revealed a clear positive correlation. As the number of daily study hours increased, the final score tended to increase as well. Similarly, PreviousYearPercentage was a very strong predictor. This confirms the intuitive understanding that consistent effort and a strong academic foundation are critical for success.



Insight 2: Parental Education Correlates with Higher Scores

The box plot comparing Final Scores across different Parental Education Levels showed a distinct trend. The median final score increased as the parental education level rose from 'High School' to 'Graduate', 'Postgraduate', and 'Doctorate'. This suggests that the parental academic background can be a significant influencing factor, possibly due to a more supportive learning environment at home.



Insight 3: Score Distribution is Normal

The histogram of Final Scores showed a roughly normal distribution (a bell curve), centered around the mid-80s. This indicates that most students perform around the average, with fewer students at the extreme high and low ends of the performance spectrum.



4\. Modeling and Performance

Two regression models were trained and evaluated to predict the FinalScore.



Models Used:

Linear Regression: Chosen as a baseline model for its simplicity and interpretability.



Random Forest Regressor: Chosen for its high accuracy and ability to capture complex, non-linear relationships in the data.



Performance Results:

The models were evaluated using the R-squared (R²) metric, which measures the proportion of the variance in the target variable that is predictable from the independent variables.



Linear Regression R² Score: 99.90%



Random Forest R² Score: 99.62%



Both models achieved exceptionally high R-squared scores. This is primarily due to the clean and predictable nature of the synthetic dataset. Interestingly, the simpler Linear Regression model slightly outperformed the Random Forest, suggesting the relationships in the data were largely linear and did not require the complexity of an ensemble model to be captured effectively.



For the final application, the Random Forest model was chosen as it is generally more robust and performs better on more complex, real-world data.



5\. Conclusion

This project successfully demonstrated the end-to-end process of building a predictive analytics tool. The analysis confirmed that factors like study habits and parental background are strong indicators of student performance. The resulting machine learning model was able to predict final scores with a very high degree of accuracy and was successfully deployed in a user-friendly Streamlit web application.

