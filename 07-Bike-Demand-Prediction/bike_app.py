import streamlit as st
import joblib
import pandas as pd

#====================================================
@st.cache_resource
def load_model():
    return joblib.load("bike_demand_model.pkl")

loaded_model = load_model()
#=====================================================
st.set_page_config(
    page_title="Bike Demand Predictor",
    page_icon="🚲",
    layout="centered"
)
#======================================================
st.title("🚲 Bike Sharing Demand Prediction")
st.write("Enter the details below to predict the number of bike rentals.")

st.sidebar.title("Bike Demand Predictor")

st.sidebar.info("""
Predict daily bike rentals using weather conditions and calendar information.
""")

st.sidebar.success("Model : Random Forest Regressor\nR² Score : 0.88")


st.divider()
#============================================================
col1,col2 = st.columns(2)

with col1:
    season = st.selectbox(
    "Season",
    ["Spring", "Summer", "Fall", "Winter"]
    )

    yr = st.selectbox(
    "Year",
    ["2011", "2012"]
    )

    mnth = st.selectbox(
    "Month",
    list(range(1,13))
    )

    holiday = st.selectbox(
    "Holiday",
    ["No", "Yes"]
    )

    weekday = st.selectbox(
    "Weekday",
    ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    )

with col2:

    workingday = st.selectbox(
    "Working Day",
    ["No","Yes"]
    )

    weathersit = st.selectbox(
    "Weather",
    [
        "Clear",
        "Mist / Cloudy",
        "Light Rain / Snow",
        "Heavy Rain / Snow"
    ]
    )

    temp = st.slider(
    "Temperature (°C)",
    0,
    40,
    20
    )

    hum = st.slider(
    "Humidity (%)",
    0,
    100,
    50
    )

    windspeed = st.slider(
    "Wind Speed (km/hr)",
    0,
    50,
    10
    )

st.divider()
#======================================================================
season_map = {
    "Spring":1,
    "Summer":2,
    "Fall":3,
    "Winter":4
}

year_map = {
    "2011":0,
    "2012":1
}

holiday_map = {
    "No":0,
    "Yes":1
}

weekday_map = {
    "Sunday":0,
    "Monday":1,
    "Tuesday":2,
    "Wednesday":3,
    "Thursday":4,
    "Friday":5,
    "Saturday":6
}

workingday_map = {
    "No":0,
    "Yes":1
}

weather_map = {
    "Clear":1,
    "Mist / Cloudy":2,
    "Light Rain / Snow":3,
    "Heavy Rain / Snow":4
}
temp = temp / 40
hum = hum / 100
windspeed = windspeed / 50

#=========================================
if st.button("🚲 Predict Bike Demand"):

    input_data = pd.DataFrame({
        "season":[season_map[season]],
        "yr":[year_map[yr]],
        "mnth":[mnth],
        "holiday":[holiday_map[holiday]],
        "weekday":[weekday_map[weekday]],
        "workingday":[workingday_map[workingday]],
        "weathersit":[weather_map[weathersit]],
        "temp":[temp],
        "hum":[hum],
        "windspeed":[windspeed]
    })

    prediction = loaded_model.predict(input_data)
    st.success(f"Estimated Bike Rentals: {int(prediction[0])} 🚲")

st.subheader("Input Summary")
st.write(f"Season : {season}")
st.write(f"Year : {yr}")
st.write(f"Month : {mnth}")
st.write(f"Weather : {weathersit}")
st.write(f"Temperature : {temp*40:.1f} °C")
st.write(f"Humidity : {hum*100:.0f}%")
st.write(f"Wind Speed : {windspeed*50:.1f} km/h")
#====================================================================
st.divider()

st.header("About This Project")

st.write("""
This machine learning model predicts the number of bikes that are likely to be rented based on weather and calendar information.

Model Used:
- Random Forest Regressor

Performance:
- R² Score = 0.88

Developed using:
- Python
- Scikit-Learn
- Streamlit
""")