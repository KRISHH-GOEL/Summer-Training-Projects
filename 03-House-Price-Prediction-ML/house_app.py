import streamlit as st
import joblib

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)
@st.cache_resource
def load_model():
    return joblib.load("house_price_model.pkl")

loaded_model = load_model()
#============================================================================================================
st.title("🏠 House Price Prediction")

st.markdown(
"""
Predict house prices using a **Machine Learning Linear Regression Model**.
Enter the details below and click **Predict House Price**.
"""
)
#=============================================================================================================
col1, col2 = st.columns(2)

with col1:
    income = st.number_input(
    "Enter Avg. Area Income",
    min_value = 0.0,
    value = 80000.00
    )
    age = st.number_input(
    "Enter Avg. Area House Age",
    min_value=0.0,
    value=7.85
    )
    rooms = st.number_input(
    "Enter Avg. Area Number of Rooms",
    min_value=0.0,
    value=6.52
    )

with col2:
    bedrooms = st.number_input(
    "Enter Avg. Area Number of Bedrooms",
    min_value=0.0,
    value=4.35
    )
    population = st.number_input(
    "Enter Area Population",
    min_value=0.0,
    value=35000.00
    )
#================================================================================================================
if st.button("Predict House Price"):
    st.write("Income:", income)
    st.write("House Age:", age)
    st.write("Rooms:", rooms)
    st.write("Bedrooms:", bedrooms)
    st.write("Population:", population)


    new_house=[[income,
                age,
                rooms,
                bedrooms,
                population]]

    prediction = loaded_model.predict(new_house)
    st.success("Prediction Completed ✅")
    st.metric(
        label="Estimated House Price",
        value=f"₹ {prediction[0]:,.2f}"
    )

st.warning("prediction may be incorrect ")

st.markdown("---")

st.caption(
    "Built using Streamlit • Scikit-Learn • Linear Regression"
)