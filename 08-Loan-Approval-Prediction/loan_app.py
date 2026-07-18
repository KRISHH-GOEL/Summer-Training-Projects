import streamlit as st
import joblib
import pandas as pd

# ================================================

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="wide"
)

# =================================================

st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

.title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#0E4D92;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}

.stButton>button{
    width:100%;
    background-color:#0E4D92;
    color:white;
    font-size:18px;
    border-radius:10px;
    height:3em;
}

.stButton>button:hover{
    background-color:#1565C0;
    color:white;
}

.metric-box{
    background-color:#ffffff;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)

# ========================================================

@st.cache_resource
def load_model():
    return joblib.load("loan_prediction_model.pkl")

loaded_model = load_model()

#=========================================================

st.sidebar.title("🏦 Loan Approval Predictor")

st.sidebar.info("""
This application predicts whether a loan application is likely to be approved using a **Decision Tree Classifier**.

### Model
- Decision Tree Classifier

### Algorithm
- Supervised Learning
- Classification

### Developed Using
- Python
- Scikit-Learn
- Streamlit
""")

st.sidebar.success("Model Accuracy : 74%")

#==============================================================================

st.markdown("<div class='title'>🏦 Loan Approval Prediction</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Predict whether a customer's loan application will be Approved or Rejected.</div>", unsafe_allow_html=True)

st.divider()


#================================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("👤 Applicant Details")

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    married = st.selectbox(
        "Married",
        ["No","Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        [0,1,2,3]
    )

    education = st.selectbox(
        "Education",
        ["Graduate","Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["No","Yes"]
    )

    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0,
        value=5000
    )

with col2:

    st.subheader("💰 Loan Details")

    coapplicant_income = st.number_input(
        "Co-applicant Income",
        min_value=0,
        value=2000
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=150
    )

    loan_term = st.selectbox(
        "Loan Amount Term",
        [12,36,60,84,120,180,240,300,360,480]
    )

    credit_history = st.selectbox(
        "Credit History",
        ["Good","Bad"]
    )

# =====================================================

gender = 1 if gender=="Male" else 0

married = 1 if married=="Yes" else 0

education = 0 if education=="Graduate" else 1

self_employed = 1 if self_employed=="Yes" else 0

credit_history = 1 if credit_history=="Good" else 0


# =========================================================

st.divider()

if st.button("🔮 Predict Loan Status"):

    input_df = pd.DataFrame({

        "Gender":[gender],

        "Married":[married],

        "Dependents":[dependents],

        "Education":[education],

        "Self_Employed":[self_employed],

        "ApplicantIncome":[applicant_income],

        "CoapplicantIncome":[coapplicant_income],

        "LoanAmount":[loan_amount],

        "Loan_Amount_Term":[loan_term],

        "Credit_History":[credit_history],

    })

    prediction = loaded_model.predict(input_df)[0]

    probability = loaded_model.predict_proba(input_df)[0]

    st.subheader("Prediction Result")

    if prediction == 1:

        st.success("✅ Loan Approved")

        st.metric(
            "Confidence",
            f"{probability[1]*100:.2f}%"
        )

    else:

        st.error("❌ Loan Rejected")

        st.metric(
            "Confidence",
            f"{probability[0]*100:.2f}%"
        )

    st.divider()

    st.subheader("📋 Application Summary")

    summary = pd.DataFrame({

        "Feature":[
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self Employed",
            "Applicant Income",
            "Co-applicant Income",
            "Loan Amount",
            "Loan Term",
            "Credit History",
        ],

        "Value":[
            "Male" if gender else "Female",
            "Yes" if married else "No",
            dependents,
            "Graduate" if education==0 else "Not Graduate",
            "Yes" if self_employed else "No",
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term,
            "Good" if credit_history else "Bad",
        ]

    })

    st.table(summary)

st.divider()

st.subheader("📖 About This Project")

st.markdown("""
### Objective

Predict whether a customer's loan application will be approved based on applicant details.

### Machine Learning Model

- Decision Tree Classifier

### Input Features

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Term
- Credit History
- Property Area

### Output

- ✅ Loan Approved
- ❌ Loan Rejected

### Tech Stack

- Python
- Pandas
- Scikit-Learn
- Streamlit
""")

st.divider()

st.caption("👨‍💻 Developed by Krish Goel | Machine Learning Portfolio Project")