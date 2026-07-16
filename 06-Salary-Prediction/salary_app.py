import streamlit as st
import joblib

@st.cache_resource
def load_model():
    return joblib.load("salary_prediction_model")

loaded_model = load_model()

st.set_page_config(
    page_title = "salar_preddiction",
    page_icon = "💵",
    layout="centered"
)
#===================================================================
st.title("💰 Salary Prediction App")

st.markdown("""
            Predict salary based on years of experience.
            """)
#=====================================================================
st.sidebar.title("About")
st.sidebar.write("""
This application predicts salary using a
Decision Tree Regression model trained on
Years of Experience.
""")
#====================================================================
experience = st.number_input(
    "Year of experience",
    min_value = 0.0,
    max_value = 50.0,
    value=25.0,
    step = 1.0
)
#====================================================================
if st.button("Predict Salary"):
    st.write(f"The average salary of someone with experience of {experience} years is ")
    prediction = loaded_model.predict([[experience]])
    st.markdown(f"# ₹ {prediction[0]:,.2f}")
#====================================================================
st.markdown("---")

st.markdown(
"""
Decision Tree Regressor Machine Learning Model Made with ❤️ using

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy

"""
)