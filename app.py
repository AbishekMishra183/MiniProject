import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Student Performance Prediction", layout="centered")

st.title("📊 Student Performance Prediction System")

st.markdown("Fill in the details below to predict the student's math score using our trained machine learning model.")

# Form input
with st.form("prediction_form"):
    gender = st.selectbox("Gender", ["male", "female"])
    # Removed ethnicity input
    parental_level_of_education = st.selectbox("Parental Level of Education", [
        "some high school", "high school", "some college",
        "associate's degree", "bachelor's degree", "master's degree"
    ])
    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=70)
    writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=70)

    submitted = st.form_submit_button("Predict")

# Prediction logic
if submitted:
    try:
        # Create data instance without race_ethnicity
        data = CustomData(
            gender=gender,
            # race_ethnicity removed
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        # Convert to DataFrame
        df = data.get_data_as_data_frame()
        st.subheader("🧾 Input Summary")
        st.dataframe(df)

        # Prediction
        pipeline = PredictPipeline()
        result = pipeline.predict(df)

        # Show result
        st.success(f"📈 Predicted Math Score: **{round(result[0], 2)}**")

    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
