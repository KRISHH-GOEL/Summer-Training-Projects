import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ==========================================================
try:
    model = joblib.load("heart_disease_model.pkl")
    encoder = joblib.load("label_encoder.pkl")
    metrics = joblib.load("metrics.pkl")
    best_params = joblib.load("best_params.pkl")

except Exception as e:
    st.error(f"Error loading model files.\n\n{e}")
    st.stop()
# ==========================================================
st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
}

.main-title{
font-size:42px;
font-weight:bold;
color:#E63946;
text-align:center;
}

.sub-title{
font-size:20px;
text-align:center;
color:gray;
margin-bottom:30px;
}

.footer{
text-align:center;
font-size:14px;
color:gray;
margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================

st.sidebar.title("❤️ Navigation")

page = st.sidebar.radio(

    "Go To",

    [
        "🏠 Home",
        "❤️ Prediction"
    ]

)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Heart Disease Prediction

Machine Learning Project

Algorithm:
Random Forest Classifier
"""
)

# ==========================================================

if page == "🏠 Home":

    st.markdown(
        "<div class='main-title'>❤️ Heart Disease Prediction System</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Machine Learning Based Clinical Decision Support System</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2 = st.columns([2,1])

    with col1:

        st.markdown(
        """
### 📌 Project Overview

This application predicts whether a patient is likely to have heart disease
using a **Random Forest Machine Learning model**.

The prediction is based on various clinical attributes including:

- Age
- Sex
- Chest Pain Type
- Blood Pressure
- Cholesterol
- Blood Sugar
- ECG Results
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope
- Number of Major Vessels
- Thallium Scan Result

The model was trained, evaluated and optimized using Scikit-Learn.

---
        """
)
#==============================================================
    st.header("📈 Model Performance")

    m1,m2,m3,m4 = st.columns(4)

    with m1:
        st.metric(
            "Accuracy",
            f"{metrics['accuracy']*100:.2f}%"
        )

    with m2:
        st.metric(
            "Precision",
            f"{metrics['precision']*100:.2f}%"
        )

    with m3:
        st.metric(
            "Recall",
            f"{metrics['recall']*100:.2f}%"
        )

    with m4:
        st.metric(
            "F1 Score",
            f"{metrics['f1']*100:.2f}%"
        )

    st.markdown("---")
#=================================================================
    st.header("🏆 Best Hyperparameters")

    st.json(best_params)
#==================================================================
    st.markdown(
"""
<div class="footer">

Made with ❤️ using Streamlit & Scikit-Learn

</div>
""",
unsafe_allow_html=True
)
    
# ==========================================================
# PREDICTION PAGE

elif page == "❤️ Prediction":

    st.title("❤️ Heart Disease Prediction")

    st.write(
        "Enter the patient's clinical information below and click "
        "**Predict** to estimate the likelihood of heart disease."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=45
        )

        sex = st.selectbox(
            "Sex",
            options=[0, 1],
            format_func=lambda x: "Female" if x == 0 else "Male"
        )

        chest_pain = st.selectbox(
            "Chest Pain Type",
            options=[1,2,3,4]
        )

        bp = st.number_input(
            "Resting Blood Pressure",
            min_value=80,
            max_value=250,
            value=120
        )

        cholesterol = st.number_input(
            "Cholesterol",
            min_value=100,
            max_value=700,
            value=200
        )

        fbs = st.selectbox(
            "Fasting Blood Sugar > 120 mg/dl",
            options=[0,1],
            format_func=lambda x:"No" if x==0 else "Yes"
        )

        ekg = st.selectbox(
            "Resting ECG",
            options=[0,1,2]
        )

    with col2:

        max_hr = st.number_input(
            "Maximum Heart Rate",
            min_value=60,
            max_value=250,
            value=150
        )

        exercise_angina = st.selectbox(
            "Exercise Induced Angina",
            options=[0,1],
            format_func=lambda x:"No" if x==0 else "Yes"
        )

        st_depression = st.number_input(
            "ST Depression",
            min_value=0.0,
            max_value=10.0,
            value=1.0,
            step=0.1
        )

        slope = st.selectbox(
            "Slope",
            options=[1,2,3]
        )

        vessels = st.selectbox(
            "Number of Major Vessels",
            options=[0,1,2,3]
        )

        thal = st.selectbox(
            "Thallium",
            options=[3,6,7]
        )

    st.markdown("---")

    if st.button("🔍 Predict Heart Disease", use_container_width=True):

        input_df = pd.DataFrame(
            [[
                age,
                sex,
                chest_pain,
                bp,
                cholesterol,
                fbs,
                ekg,
                max_hr,
                exercise_angina,
                st_depression,
                slope,
                vessels,
                thal
            ]],
            columns=[
                "Age",
                "Sex",
                "Chest pain type",
                "BP",
                "Cholesterol",
                "FBS over 120",
                "EKG results",
                "Max HR",
                "Exercise angina",
                "ST depression",
                "Slope of ST",
                "Number of vessels fluro",
                "Thallium"
            ]
        )

        prediction = model.predict(input_df)

        probability = model.predict_proba(input_df)

        result = encoder.inverse_transform(prediction)[0]

        confidence = probability.max() * 100

        st.markdown("---")

        if result.lower() == "presence":

            st.error(
                f"⚠ Prediction : {result}"
            )

        else:

            st.success(
                f"✅ Prediction : {result}"
            )

        st.progress(float(confidence/100))

        st.write(
            f"### Confidence : {confidence:.2f}%"
        )

        st.subheader("Prediction Probability")

        prob_df = pd.DataFrame({
            "Class":["Absence","Presence"],
            "Probability":probability[0]
        })

        st.dataframe(
            prob_df,
            use_container_width=True
        )