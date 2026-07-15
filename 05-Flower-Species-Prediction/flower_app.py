import streamlit as st
import joblib 


@st.cache_resource        # model loaded once when called 
def load_model():
    return joblib.load("flower_prediction_model.pkl")

loaded_model = load_model()

st.set_page_config(
    page_title = "species_prediction",
    page_icon = "🌸",
    layout="centered"
)
#======================================================
st.title("🌸 Flower Species Predictor")
st.markdown(
    """
Predict species of a flower using a machine learning.
Enter the details below and click **Predict Species**.
"""
)
#=========================================================
st.sidebar.title("🌼 About")
st.sidebar.write("""
This application predicts the species of an Iris flower using a trained Logistic Regression model.

Species:
- 🌷 Setosa
- 🌼 Versicolor
- 🌺 Virginica
""")
#===============================================================
species_dict = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}
#=====================================================================
st.subheader("Enter Flower Measurements")

col1, col2 = st.columns(2)
with col1:
    sepal_length = st.slider(
    "Sepal Lenght (cm)",
    1.0,8.0,
    step= .02
    )
    sepal_width = st.slider(
    "Sepal Width (cm)",
    1.0,8.0,
    step= .02
    )
with col2:
    petal_length = st.slider(
    "Petal Lenght (cm)",
    1.0,8.0,
    step= .02
    )
    petal_width = st.slider(
    "Petal Width (cm)",
    1.0,8.0,
    step= .02
    )

if st.button("🔍 Predict Species"):
    flower = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width 
        ]]
    
    prediction = loaded_model.predict(flower)
    
    species_dict = {
        0: "🌷 Setosa",
        1: "🌼 Versicolor",
        2: "🌺 Virginica"
    }

    species_name = species_dict[int(prediction[0])]

    st.success("Prediction Completed ✅")

    st.metric(
        label="Predicted Species",
        value=species_name
    )
#==================================================================
st.markdown("---")

st.markdown(
"""
Made with ❤️ using

- Python
- Streamlit
- Scikit-Learn
"""
)