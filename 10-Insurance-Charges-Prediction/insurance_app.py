import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Insurance Charges Predictor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

model = joblib.load("insurance_model.pkl")
scaler = joblib.load("scaler.pkl")
metrics = joblib.load("model_metrics.pkl")
dataset0 = pd.read_csv("insurance.csv")

st.markdown("""
<style>

.main{
    background-color:#F8FAFC;
}

h1,h2,h3{
    color:#0F172A;
}

.stButton>button{
    width:100%;
    background:#2563EB;
    color:white;
    border:none;
    border-radius:8px;
    height:3em;
    font-size:18px;
}

.stButton>button:hover{
    background:#1D4ED8;
    color:white;
}

.metric-card{
    padding:18px;
    border-radius:12px;
    background:white;
    box-shadow:0px 3px 10px rgba(0,0,0,0.12);
}

# .prediction-box{
#     background:#DCFCE7;
#     padding:20px;
#     border-radius:12px;
#     border-left:8px solid green;
#     font-size:22px;
#     font-weight:bold;
# }

.footer{
    text-align:center;
    color:gray;
    font-size:15px;
    padding-top:30px;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "",
    [
        "🏠 Home",
        "📊 About Model"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
**Project**

Insurance Charges Prediction

Algorithm:
K-Nearest Neighbors Regressor
"""
)

# -------------------------------------------------------
# HOME PAGE
# -------------------------------------------------------

if page=="🏠 Home":

    st.title("💰 Insurance Charges Predictor")

    st.write(
        """
Predict the estimated medical insurance charges
using a trained **K-Nearest Neighbors Regressor** model.
"""
    )

    st.markdown("---")

    col1,col2=st.columns(2)

    with col1:

        age=st.slider(
            "Age",
            18,
            65,
            25
        )

        sex=st.selectbox(
            "Sex",
            ["Male","Female"]
        )

        bmi=st.number_input(
            "BMI",
            min_value=10.0,
            max_value=60.0,
            value=25.0,
            step=1.0
        )

    with col2:

        children=st.selectbox(
            "Children",
            [0,1,2,3,4,5]
        )

        smoker=st.selectbox(
            "Smoker",
            ["No","Yes"]
        )

    st.markdown("")

    predict=st.button("Predict Insurance Charges")

    if predict:

        sex=1 if sex=="Male" else 0
        smoker=1 if smoker=="Yes" else 0

        input_data=pd.DataFrame({
            "age":[age],
            "sex":[sex],
            "bmi":[bmi],
            "children":[children],
            "smoker":[smoker],
        })

        input_scaled=scaler.transform(input_data)

        st.markdown("### 📋 Input Summary")

        summary = pd.DataFrame({
            "Feature": [
            "Age",
            "Sex",
            "BMI",
            "Children",
            "Smoker",
        ],
        "Value": [
            age,
            sex,
            bmi,
            children,
            smoker,
        ]
    })

        st.dataframe(summary, use_container_width=True, hide_index=True)

        prediction=model.predict(input_scaled)[0]

        st.markdown("---")

        st.success("Prediction Completed ✅")

        st.metric(
    label="Estimated Insurance Charges",
    value=f"₹ {prediction:,.2f}"
)

elif page == "📊 About Model":

    st.title("📊 About the Model")

    st.markdown("""
This application predicts **medical insurance charges** using a **K-Nearest Neighbors Regressor (KNNR)** trained on the **Medical Insurance Cost** dataset.
""")

    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📌 Overview",
            "📈 Performance",
            "⚙️ Hyperparameters",
            "Dataset"
        ]
    )

    with tab1:

        st.subheader("Dataset Information")

        dataset = pd.DataFrame(
            {
                "Feature":[
                    "Age",
                    "Sex",
                    "BMI",
                    "Children",
                    "Smoker",
                    "Region"
                ],

                "Description":[
                    "Age of the beneficiary",
                    "Gender",
                    "Body Mass Index",
                    "Number of dependent children",
                    "Smoking status",
                    "Residential region"
                ]
            }
        )

        st.dataframe(dataset, use_container_width=True)

        st.markdown("---")

        st.subheader("Target Variable")

        st.success("Insurance Charges")

        st.markdown("---")


    with tab2:

        st.subheader("Model Performance")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "R² Score",
                f"{metrics['R2 Score']:.4f}"
            )

            st.metric(
                "MAE",
                f"{metrics['MAE']:.2f}"
            )

        with col2:

            st.metric(
                "MSE",
                f"{metrics['MSE']:.2f}"
            )

            st.metric(
                "Cross Validation Score",
                f"{metrics['Cross Validation Score']:.4f}"
            )

        st.markdown("---")

        st.info(
"""
These metrics are calculated on the unseen test dataset after tuning the model using GridSearchCV.
"""
        )

    # -------------------------------------------------------
    # Hyperparameters
    # -------------------------------------------------------

    with tab3:

        st.subheader("Best Hyperparameters")

        params = pd.DataFrame(
            metrics["Best Parameters"].items(),
            columns=["Parameter","Value"]
        )

        st.table(params)

        st.markdown("---")

        st.subheader("Model")

        st.code("KNeighborsRegressor()", language="python")

    with tab4:

        st.subheader("Medical Insurance Dataset")

        st.write(
            """
            The model was trained on the **Medical Insurance Cost** dataset.

            Each row represents one individual along with their demographic
            and health-related information used to predict insurance charges.
            """
        )

        st.markdown("### Dataset Shape")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Rows", dataset0.shape[0])

        with col2:
            st.metric("Columns", dataset0.shape[1])

        st.markdown("### Dataset Preview")

        st.dataframe(
            dataset0.head(10),
            use_container_width=True
        )

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.markdown("---")

st.markdown(
"""
<div class="footer">

Developed using ❤️ with Streamlit & Scikit-learn

<br>

Insurance Charges Prediction using K-Nearest Neighbors Regressor

</div>
""",
unsafe_allow_html=True
)