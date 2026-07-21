import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Banknote Authentication",
    page_icon="💵",
    layout="wide"
)

model = joblib.load("banknote_model.pkl")
scaler = joblib.load("scaler.pkl")
evaluation = joblib.load("evaluation_metrics.pkl")

df = pd.read_csv("data_banknote_authentication.csv")


st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "🏠 Home",
        "ℹ About Model"
    ]
)

# HOME PAGE

if page == "🏠 Home":

    st.title("💵 Banknote Authentication using KNN")

    st.write(
        """
        Predict whether a banknote is **Genuine** or **Forged**
        using a trained K-Nearest Neighbors classifier.
        """
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Input Features")

        variance = st.number_input(
            "Variance",
            value=0.0,
            format="%.4f"
        )

        skewness = st.number_input(
            "Skewness",
            value=0.0,
            format="%.4f"
        )

        curtosis = st.number_input(
            "Curtosis",
            value=0.0,
            format="%.4f"
        )

        entropy = st.number_input(
            "Entropy",
            value=0.0,
            format="%.4f"
        )

        predict = st.button("Predict")

    with col2:

        st.subheader("Prediction")

        if predict:

            sample = np.array([
                [variance,
                 skewness,
                 curtosis,
                 entropy]
            ])

            sample_scaled = scaler.transform(sample)

            prediction = model.predict(sample_scaled)[0]

            probability = model.predict_proba(sample_scaled)[0]

            confidence = np.max(probability) * 100

            if prediction == 0:
                st.success("Prediction : Genuine Banknote")
            else:
                st.error("Prediction : Forged Banknote")

            st.metric(
                "Prediction Confidence",
                f"{confidence:.2f}%"
            )

            st.write("### Class Probabilities")

            prob_df = pd.DataFrame({
                "Class": ["Genuine (0)", "Forged (1)"],
                "Probability": probability
            })

            st.dataframe(
                prob_df,
                use_container_width=True
            )

    st.divider()

    st.subheader("Entered Values")

    input_df = pd.DataFrame({

        "Feature":[
            "Variance",
            "Skewness",
            "Curtosis",
            "Entropy"
        ],

        "Value":[
            variance,
            skewness,
            curtosis,
            entropy
        ]

    })

    st.dataframe(
        input_df,
        use_container_width=True
    )

# ABOUT PAGE

else:

    st.title("ℹ About the Model")

    st.header("Dataset")

    st.write("""

The Banknote Authentication dataset is built from images of genuine
and forged banknotes.

Each image was transformed using Wavelet Transform,
producing four numerical features.

Target Classes

• 0 → Genuine

• 1 → Forged

    """)

    if df is not None:

        st.subheader("Dataset Overview")

        c1, c2, c3 = st.columns(3)

        c1.metric("Rows", df.shape[0])
        c2.metric("Columns", df.shape[1])
        c3.metric("Features", df.shape[1]-1)

        st.write("Sample Dataset")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

    st.divider()

    st.header("Model Information")

    st.write("""

Algorithm Used

• K-Nearest Neighbors Classifier

Distance Metric

• Euclidean Distance

Scaling

• StandardScaler

    """)

    st.divider()

    st.header("Model Evaluation")

    st.dataframe(
        evaluation,
        use_container_width=True
    )
    st.divider()

    st.header("Feature Description")

    feature_info = pd.DataFrame({

        "Feature":[
            "Variance",
            "Skewness",
            "Curtosis",
            "Entropy"
        ],

        "Description":[
            "Variance of Wavelet Transformed image",
            "Skewness of Wavelet Transformed image",
            "Curtosis of Wavelet Transformed image",
            "Entropy of Image"
        ]

    })

    st.dataframe(
        feature_info,
        use_container_width=True
    )