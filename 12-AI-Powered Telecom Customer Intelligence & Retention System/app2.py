"""
=====================================================================================
AI-POWERED TELECOM CUSTOMER INTELLIGENCE & RETENTION SYSTEM
=====================================================================================
A business-oriented Streamlit dashboard that consumes the artifacts produced by
`Train_Test_Model.ipynb` (encoders, scalers, PCA, KMeans, the trained classifier
and all evaluation metrics) together with the rule-based `retention_advisor.py`
engine. No model is retrained and no preprocessing logic is re-derived here -
every transformation is performed by calling `.transform()` / `.predict()` on the
objects that were already fitted and saved (via joblib / numpy) in the notebook.

Run with:  streamlit run app.py

Requirements:
    streamlit, pandas, numpy, scikit-learn, joblib, plotly

Expected files (same folder as this script, produced by the notebook):
    Dataset.csv, best_model.pkl, onehot_encoder.pkl, target_encoder.pkl,
    feature_names.pkl, scaler.pkl, scaler_pca.pkl, pca.pkl, kmeans.pkl,
    cluster_labels.pkl, model_comparison.csv, confusion_matrix.npy,
    metrics.pkl, best_params.pkl, retention_advisor.py
=====================================================================================
"""

import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from retention_advisor import (
    retention_advisor,
    AT_RISK,
    LOYAL_HIGH_VALUE,
    BUDGET_LOYAL,
)

# =====================================================================================
# PAGE CONFIGURATION
# =====================================================================================
st.set_page_config(
    page_title="AI-Powered Telecom Customer Intelligence & Retention System",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =====================================================================================
# CONSTANTS
# =====================================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILES = {
    "dataset": "Dataset.csv",
    "best_model": "best_model.pkl",
    "ohe": "onehot_encoder.pkl",
    "target_encoder": "target_encoder.pkl",
    "feature_names": "feature_names.pkl",
    "scaler": "scaler.pkl",
    "scaler_pca": "scaler_pca.pkl",
    "pca": "pca.pkl",
    "kmeans": "kmeans.pkl",
    "cluster_labels": "cluster_labels.pkl",
    "model_comparison": "model_comparison.csv",
    "confusion_matrix": "confusion_matrix.npy",
    "metrics": "metrics.pkl",
    "best_params": "best_params.pkl",
}

RAW_COLUMNS = [
    "gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService",
    "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup",
    "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies",
    "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges",
]

CATEGORICAL_COLS = [
    "gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
    "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
    "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
    "PaperlessBilling", "PaymentMethod",
]

# Business risk thresholds (mirrors retention_advisor.py so UI and logic stay in sync)
CRITICAL_RISK = 0.80
HIGH_RISK = 0.60
MEDIUM_RISK = 0.40

# Corporate color palette
COLOR_BLUE = "#1450A3"
COLOR_BLUE_LIGHT = "#2D6CDF"
COLOR_GREEN = "#1E8E5A"
COLOR_ORANGE = "#E8871E"
COLOR_RED = "#D64545"
COLOR_GREY = "#5A6572"
COLOR_BG_CARD = "#FFFFFF"

RISK_COLORS = {
    "Critical": COLOR_RED,
    "High": COLOR_ORANGE,
    "Medium": "#E8B71E",
    "Low": COLOR_GREEN,
}

SEGMENT_ICONS = {
    BUDGET_LOYAL: "💰",
    AT_RISK: "⚠️",
    LOYAL_HIGH_VALUE: "💎",
}

SEGMENT_DESCRIPTIONS = {
    BUDGET_LOYAL: "Price-sensitive customers with moderate tenure and stable, "
                   "low-to-mid monthly spend. They stay because the value equation "
                   "works for them - the priority is protecting that value perception.",
    AT_RISK: "Customers showing patterns strongly associated with churn - typically "
              "shorter tenure, month-to-month contracts, and fewer bundled services. "
              "This segment needs proactive retention outreach.",
    LOYAL_HIGH_VALUE: "Long-tenured customers with high monthly/total spend and strong "
                       "service adoption. They are the most profitable segment and the "
                       "highest priority to protect and reward.",
}

# =====================================================================================
# CUSTOM CSS
# =====================================================================================
def load_css():
    st.markdown(
        f"""
        <style>
            .main {{ background-color: #F5F7FA; }}
            #MainMenu, footer {{visibility: hidden;}}
            header[data-testid="stHeader"] {{
                background-color: transparent;
            }}

            h1, h2, h3 {{ color: #14213D; font-family: 'Segoe UI', sans-serif; }}

            .hero-box {{
                background: linear-gradient(135deg, {COLOR_BLUE} 0%, {COLOR_BLUE_LIGHT} 100%);
                padding: 2.2rem 2.5rem;
                border-radius: 14px;
                color: white;
                margin-bottom: 1.6rem;
            }}
            .hero-box h1 {{ color: white; margin-bottom: 0.3rem; font-size: 2.1rem; }}
            .hero-box p {{ color: #DCE6F7; font-size: 1.05rem; margin: 0; }}

            .metric-card {{
                background-color: {COLOR_BG_CARD};
                border-radius: 12px;
                padding: 1.1rem 1.3rem;
                box-shadow: 0 1px 4px rgba(20,33,61,0.08);
                border-left: 5px solid {COLOR_BLUE};
                margin-bottom: 0.8rem;
            }}

            .section-card {{
                background-color: {COLOR_BG_CARD};
                border-radius: 12px;
                padding: 1.4rem 1.6rem;
                box-shadow: 0 1px 4px rgba(20,33,61,0.08);
                margin-bottom: 1.2rem;
            }}

            .badge {{
                display: inline-block;
                padding: 0.30rem 0.85rem;
                border-radius: 20px;
                font-size: 0.82rem;
                font-weight: 600;
                margin: 0.15rem 0.3rem 0.15rem 0;
                color: white;
            }}

            .tech-badge {{
                display: inline-block;
                background-color: #EAF1FB;
                color: {COLOR_BLUE};
                border: 1px solid {COLOR_BLUE_LIGHT};
                padding: 0.35rem 0.9rem;
                border-radius: 20px;
                font-size: 0.85rem;
                font-weight: 600;
                margin: 0.25rem 0.35rem 0.25rem 0;
            }}

            .flow-step {{
                background-color: #EAF1FB;
                border: 1px solid {COLOR_BLUE_LIGHT};
                border-radius: 10px;
                padding: 0.9rem 0.5rem;
                text-align: center;
                font-weight: 600;
                color: {COLOR_BLUE};
                font-size: 0.85rem;
            }}

            .rec-card {{
                background-color: #FFFFFF;
                border-radius: 10px;
                padding: 0.8rem 1rem;
                margin-bottom: 0.6rem;
                border-left: 5px solid {COLOR_GREY};
                box-shadow: 0 1px 3px rgba(20,33,61,0.06);
            }}

            .stButton>button {{
                background-color: {COLOR_BLUE};
                color: white;
                font-weight: 600;
                border-radius: 8px;
                border: none;
                padding: 0.55rem 1.4rem;
            }}
            .stButton>button:hover {{ background-color: {COLOR_BLUE_LIGHT}; color: white; }}

            section[data-testid="stSidebar"] {{
                background-color: #14213D;
            }}
            section[data-testid="stSidebar"] * {{ color: #F5F7FA !important; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def badge(text, color):
    return f'<span class="badge" style="background-color:{color};">{text}</span>'


def priority_color(priority):
    return {
        "Critical": COLOR_RED,
        "Immediate Action": COLOR_RED,
        "High": COLOR_ORANGE,
        "Medium": "#E8B71E",
        "Low": COLOR_GREEN,
    }.get(priority, COLOR_GREY)


# =====================================================================================
# ARTIFACT LOADING (cached — read once, reused across pages)
# =====================================================================================
def _path(key):
    return os.path.join(BASE_DIR, FILES[key])


@st.cache_resource(show_spinner=False)
def load_artifacts():
    """Load every saved model / encoder / transformer produced by the notebook."""
    missing = [FILES[k] for k in
               ["best_model", "ohe", "target_encoder", "feature_names",
                "scaler", "scaler_pca", "pca", "kmeans", "cluster_labels"]
               if not os.path.exists(_path(k))]
    if missing:
        return None, missing

    artifacts = {
        "model": joblib.load(_path("best_model")),
        "ohe": joblib.load(_path("ohe")),
        "target_encoder": joblib.load(_path("target_encoder")),
        "feature_names": joblib.load(_path("feature_names")),
        "scaler": joblib.load(_path("scaler")),
        "scaler_pca": joblib.load(_path("scaler_pca")),
        "pca": joblib.load(_path("pca")),
        "kmeans": joblib.load(_path("kmeans")),
        "cluster_labels": joblib.load(_path("cluster_labels")),
    }
    return artifacts, []


@st.cache_resource(show_spinner=False)
def load_eval_artifacts():
    """Load evaluation artifacts (metrics, params, confusion matrix, comparison table)."""
    out = {}
    if os.path.exists(_path("metrics")):
        out["metrics"] = joblib.load(_path("metrics"))
    if os.path.exists(_path("best_params")):
        out["best_params"] = joblib.load(_path("best_params"))
    if os.path.exists(_path("confusion_matrix")):
        out["confusion_matrix"] = np.load(_path("confusion_matrix"))
    if os.path.exists(_path("model_comparison")):
        out["comparison_df"] = pd.read_csv(_path("model_comparison"))
    return out


@st.cache_data(show_spinner=False)
def load_dataset():
    if not os.path.exists(_path("dataset")):
        return None
    return pd.read_csv(_path("dataset"))


# =====================================================================================
# PREPROCESSING — replicates the notebook pipeline using ONLY .transform()/.predict()
# =====================================================================================
def preprocess_raw_df(df_raw, ohe, feature_names):
    """
    Reproduces the exact feature-engineering + encoding pipeline from the notebook
    for an arbitrary raw dataframe (single customer or full dataset), using the
    already-fitted OneHotEncoder. No fitting happens here.
    """
    df = df_raw.copy()

    # Same cleanup performed in the notebook
    df.replace({"No internet service": "No", "No phone service": "No"}, inplace=True)
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)
    df["tenure"] = pd.to_numeric(df["tenure"], errors="coerce").fillna(0)
    df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"], errors="coerce").fillna(0)
    df["SeniorCitizen"] = pd.to_numeric(df["SeniorCitizen"], errors="coerce").fillna(0)

    # Feature engineering (identical formula to the notebook)
    df["AvgMonthlySpend"] = df["TotalCharges"] / (df["tenure"] + 1)

    cat_cols = [c for c in CATEGORICAL_COLS if c in df.columns]
    encoded = ohe.transform(df[cat_cols])
    encoded_df = pd.DataFrame(
        encoded, columns=ohe.get_feature_names_out(cat_cols), index=df.index
    )

    X = df.drop(columns=cat_cols)
    X = pd.concat([X, encoded_df], axis=1)
    X = X.reindex(columns=feature_names, fill_value=0)
    return X


def predict_customer(raw_input, artifacts):
    """Runs the full inference pipeline (classification + clustering) for one customer."""
    df_raw = pd.DataFrame([raw_input])[RAW_COLUMNS]
    X_row = preprocess_raw_df(df_raw, artifacts["ohe"], artifacts["feature_names"])

    # --- Classification (best_model.pkl == tuned Logistic Regression) ---
    X_scaled = artifacts["scaler"].transform(X_row)
    proba = float(artifacts["model"].predict_proba(X_scaled)[0][1])
    pred = int(artifacts["model"].predict(X_scaled)[0])

    # --- Clustering (PCA + KMeans, same encoded feature space) ---
    X_scaled_pca = artifacts["scaler_pca"].transform(X_row)
    X_pca = artifacts["pca"].transform(X_scaled_pca)
    cluster_id = int(artifacts["kmeans"].predict(X_pca)[0])
    segment = artifacts["cluster_labels"].get(cluster_id, f"Cluster {cluster_id}")

    return {
        "prediction": pred,
        "probability": proba,
        "segment": segment,
        "cluster_id": cluster_id,
        "X_row": X_row,
        "X_scaled": X_scaled,
        "X_pca": X_pca,
    }


def get_decision_breakdown(model, feature_names, X_scaled, top_n=6):
    """
    For the Logistic Regression model: contribution = coefficient * scaled feature
    value for this specific customer. Positive => pushes prediction toward churn,
    negative => pushes toward retention. This is the model's own linear reasoning,
    not an approximation.
    """
    if not hasattr(model, "coef_"):
        return pd.DataFrame(columns=["Feature", "Contribution"])

    coefs = model.coef_[0]
    contributions = coefs * X_scaled[0]
    df = pd.DataFrame({"Feature": feature_names, "Contribution": contributions})
    df["AbsContribution"] = df["Contribution"].abs()
    df = df.sort_values("AbsContribution", ascending=False).head(top_n)
    return df.drop(columns="AbsContribution")


@st.cache_data(show_spinner=False)
def compute_segment_view(_artifacts, dataset_hash):
    """
    Applies the saved encoders/scaler/PCA/KMeans to the FULL dataset (transform only)
    to build the segment visualization + cluster business profiles. Nothing is fit here.
    `dataset_hash` is only used to key the cache.
    """
    df = load_dataset()
    if df is None:
        return None

    work = df.drop(columns=["customerID"], errors="ignore").drop_duplicates().reset_index(drop=True)
    churn_col = work["Churn"] if "Churn" in work.columns else None
    feature_src = work.drop(columns=["Churn"], errors="ignore")

    X_full = preprocess_raw_df(feature_src, _artifacts["ohe"], _artifacts["feature_names"])
    X_scaled_pca = _artifacts["scaler_pca"].transform(X_full)
    X_pca = _artifacts["pca"].transform(X_scaled_pca)
    clusters = _artifacts["kmeans"].predict(X_pca)

    view = work.copy()

    # Coerce numeric columns — TotalCharges in particular loads as text because
    # the raw CSV contains blank-string values for a handful of rows.
    for num_col in ["tenure", "MonthlyCharges", "TotalCharges"]:
        if num_col in view.columns:
            view[num_col] = pd.to_numeric(view[num_col], errors="coerce").fillna(0)

    view["Cluster"] = clusters
    view["Segment"] = view["Cluster"].map(_artifacts["cluster_labels"])
    view["PC1"] = X_pca[:, 0]
    view["PC2"] = X_pca[:, 1]
    if churn_col is not None:
        view["ChurnFlag"] = (view["Churn"] == "Yes").astype(int)
    return view


# =====================================================================================
# SMALL UI HELPERS
# =====================================================================================
def kpi_card(label, value, icon="📊", color=COLOR_BLUE):
    st.markdown(
        f"""
        <div class="metric-card" style="border-left-color:{color};">
            <div style="font-size:0.85rem;color:{COLOR_GREY};font-weight:600;">{icon} {label}</div>
            <div style="font-size:1.55rem;font-weight:700;color:#14213D;">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def risk_gauge(probability):
    color = (
        COLOR_RED if probability >= CRITICAL_RISK else
        COLOR_ORANGE if probability >= HIGH_RISK else
        "#E8B71E" if probability >= MEDIUM_RISK else
        COLOR_GREEN
    )
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=round(probability * 100, 1),
        number={"suffix": "%", "font": {"size": 36}},
        gauge={
            "axis": {"range": [0, 100], "tickwidth": 1},
            "bar": {"color": color, "thickness": 0.35},
            "steps": [
                {"range": [0, 40], "color": "#E7F5EC"},
                {"range": [40, 60], "color": "#FCF3D9"},
                {"range": [60, 80], "color": "#FCE6D2"},
                {"range": [80, 100], "color": "#FBE1E1"},
            ],
            "threshold": {
                "line": {"color": "#14213D", "width": 3},
                "thickness": 0.8,
                "value": round(probability * 100, 1),
            },
        },
        title={"text": "Churn Probability", "font": {"size": 15}},
    ))
    fig.update_layout(height=260, margin=dict(l=20, r=20, t=50, b=10))
    return fig


def render_recommendations(recommendations):
    for rec in recommendations:
        color = priority_color(rec["Priority"])
        st.markdown(
            f"""
            <div class="rec-card" style="border-left-color:{color};">
                {badge(rec['Priority'], color)} {badge(rec['Category'], COLOR_GREY)}
                <div style="margin-top:0.4rem;color:#14213D;">{rec['Message']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =====================================================================================
# SIDEBAR NAVIGATION
# =====================================================================================
def sidebar_nav():
    with st.sidebar:
        st.markdown("## 📡 Telecom AI Suite")
        st.caption("Customer Intelligence & Retention System")
        st.markdown("---")
        page = st.radio(
            "Navigate",
            [
                "🏠 Dashboard",
                "🔍 Customer Analysis",
                "📊 Model Analytics",
                "👥 Customer Segments",
                "🤖 Retention Advisor",
                "ℹ About Project",
            ],
            label_visibility="collapsed",
        )
        st.markdown("---")
        if "last_result" in st.session_state:
            st.success("✅ Customer analyzed")
            st.caption(f"Segment: {st.session_state['last_result']['result']['segment']}")
        else:
            st.info("No customer analyzed yet")
        st.markdown("---")
        st.caption("Built on: Logistic Regression · PCA · K-Means")
    return page


# =====================================================================================
# PAGE: DASHBOARD
# =====================================================================================
def page_dashboard(artifacts, eval_art, dataset):
    st.markdown(
        """
        <div class="hero-box">
            <h1>📡 AI-Powered Telecom Customer Intelligence & Retention System</h1>
            <p>Predict churn risk, segment your customer base, and generate data-driven
            retention actions — all in one business-ready dashboard.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    metrics = eval_art.get("metrics", {})
    n_records = len(dataset) if dataset is not None else "N/A"
    n_features = len(artifacts["feature_names"]) if artifacts else "N/A"
    best_model_name = type(artifacts["model"]).__name__ if artifacts else "N/A"
    accuracy = f"{metrics.get('accuracy', 0)*100:.1f}%" if metrics else "N/A"
    recall = f"{metrics.get('recall', 0)*100:.1f}%" if metrics else "N/A"
    n_segments = len(artifacts["cluster_labels"]) if artifacts else "N/A"

    st.markdown("### Key Performance Indicators")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    with c1: kpi_card("Dataset Size", f"{n_records:,}" if isinstance(n_records, int) else n_records, "🗂️")
    with c2: kpi_card("Features Used", n_features, "🧬")
    with c3: kpi_card("Best Model", "Logistic Reg." if "Logistic" in best_model_name else best_model_name, "🏆", COLOR_GREEN)
    with c4: kpi_card("Accuracy", accuracy, "🎯", COLOR_GREEN)
    with c5: kpi_card("Recall", recall, "📈", COLOR_ORANGE)
    with c6: kpi_card("Customer Segments", n_segments, "👥", COLOR_BLUE_LIGHT)

    st.markdown("### AI Workflow")
    steps = ["📁 Dataset", "🧹 Preprocessing", "🧠 Classification", "📉 PCA", "🎯 K-Means", "🤖 Retention Advisor"]
    cols = st.columns(len(steps))
    for col, step in zip(cols, steps):
        with col:
            st.markdown(f'<div class="flow-step">{step}</div>', unsafe_allow_html=True)

    st.markdown("###")
    left, right = st.columns([1.4, 1])
    with left:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("#### Project Overview")
        st.write(
            "This system combines a supervised churn classifier with unsupervised "
            "customer segmentation to give telecom business teams a single view of "
            "**who is likely to churn, why, and what to do about it**. Every customer "
            "analyzed on the *Customer Analysis* page is scored for churn risk, mapped "
            "to a behavioral segment, and paired with prioritized retention actions "
            "generated by a rule-based advisor engine — ready for the retention team "
            "to act on immediately."
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("#### Technology Stack")
        badges = ["Python", "scikit-learn", "Streamlit", "Logistic Regression",
                  "PCA", "K-Means", "Pandas", "NumPy", "Plotly"]
        st.markdown("".join(f'<span class="tech-badge">{b}</span>' for b in badges), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


# =====================================================================================
# PAGE: CUSTOMER ANALYSIS
# =====================================================================================
def page_customer_analysis(artifacts):
    st.markdown("## 🔍 Customer Analysis")
    st.caption("Enter customer details to generate a real-time churn risk assessment.")

    form_col, result_col = st.columns([1, 1.4])

    with form_col:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        with st.form("customer_form"):
            with st.expander("👤 Personal Information", expanded=True):
                gender = st.selectbox("Gender", ["Female", "Male"])
                senior = st.selectbox("Senior Citizen", ["No", "Yes"])
                partner = st.selectbox("Has Partner", ["No", "Yes"])
                dependents = st.selectbox("Has Dependents", ["No", "Yes"])

            with st.expander("📄 Account Information"):
                tenure = st.slider("Tenure (months)", 0, 72, 12)
                contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
                paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
                payment = st.selectbox(
                    "Payment Method",
                    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
                )

            with st.expander("📶 Services"):
                phone_service = st.selectbox("Phone Service", ["Yes", "No"])
                multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes"], disabled=(phone_service == "No"))
                internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
                internet_on = internet_service != "No"
                online_security = st.selectbox("Online Security", ["No", "Yes"], disabled=not internet_on)
                online_backup = st.selectbox("Online Backup", ["No", "Yes"], disabled=not internet_on)
                device_protection = st.selectbox("Device Protection", ["No", "Yes"], disabled=not internet_on)
                tech_support = st.selectbox("Tech Support", ["No", "Yes"], disabled=not internet_on)
                streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"], disabled=not internet_on)
                streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"], disabled=not internet_on)

            with st.expander("💳 Billing"):
                monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0, step=1.0)
                total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, float(monthly_charges * max(tenure, 1)), step=10.0)

            submitted = st.form_submit_button("🔎 Analyze Customer", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if submitted:
        if artifacts is None:
            st.error("Model artifacts are not available. Please add the required .pkl files to the app folder.")
            return

        raw_input = {
            "gender": gender,
            "SeniorCitizen": 1 if senior == "Yes" else 0,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "PhoneService": phone_service,
            "MultipleLines": "No" if phone_service == "No" else multiple_lines,
            "InternetService": internet_service,
            "OnlineSecurity": "No" if not internet_on else online_security,
            "OnlineBackup": "No" if not internet_on else online_backup,
            "DeviceProtection": "No" if not internet_on else device_protection,
            "TechSupport": "No" if not internet_on else tech_support,
            "StreamingTV": "No" if not internet_on else streaming_tv,
            "StreamingMovies": "No" if not internet_on else streaming_movies,
            "Contract": contract,
            "PaperlessBilling": paperless,
            "PaymentMethod": payment,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges,
        }

        with st.spinner("Running churn model and segmentation engine..."):
            result = predict_customer(raw_input, artifacts)
            report = retention_advisor(
                customer=raw_input,
                churn_prediction=result["prediction"],
                churn_probability=result["probability"],
                segment=result["segment"],
            )
            breakdown = get_decision_breakdown(
                artifacts["model"], artifacts["feature_names"], result["X_scaled"]
            )
            business_impact = round(
                min(100, result["probability"] * 70 + min(monthly_charges / 120, 1) * 30), 1
            )

        st.session_state["last_result"] = {
            "raw_input": raw_input,
            "result": result,
            "report": report,
            "breakdown": breakdown,
            "business_impact": business_impact,
        }

    with result_col:
        if "last_result" not in st.session_state:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.info("👈 Fill in the customer form and click **Analyze Customer** to generate an assessment.")
            st.markdown('</div>', unsafe_allow_html=True)
            return

        data = st.session_state["last_result"]
        result, report = data["result"], data["report"]
        risk_level = report["Risk Level"]
        risk_color = RISK_COLORS.get(risk_level, COLOR_GREY)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("#### 📋 Executive Summary")
        pred_text = "🔴 Likely to Churn" if result["prediction"] == 1 else "🟢 Not Likely to Churn"
        st.markdown(
            f"**Prediction:** {pred_text}  \n"
            f"**Segment:** {SEGMENT_ICONS.get(result['segment'], '📌')} {result['segment']}  \n"
            f"**Risk Level:** {badge(risk_level, risk_color)}  \n"
            f"**Business Priority:** {badge(report['Business Priority'], priority_color(report['Business Priority']))}",
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)

        m1, m2, m3 = st.columns(3)
        with m1: kpi_card("Churn Probability", f"{result['probability']*100:.1f}%", "📉", risk_color)
        with m2: kpi_card("Business Impact Score", f"{data['business_impact']}/100", "💼", COLOR_BLUE)
        with m3: kpi_card("Customer Segment", result["segment"].split()[0], SEGMENT_ICONS.get(result["segment"], "📌"))

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.plotly_chart(risk_gauge(result["probability"]), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("#### 🧠 AI Decision Breakdown")
        st.caption("Top factors driving this prediction (Logistic Regression coefficient × feature value).")
        if not data["breakdown"].empty:
            bd = data["breakdown"].copy()
            bd["Direction"] = np.where(bd["Contribution"] > 0, "Increases Churn Risk", "Reduces Churn Risk")
            fig = px.bar(
                bd.sort_values("Contribution"),
                x="Contribution", y="Feature", color="Direction", orientation="h",
                color_discrete_map={"Increases Churn Risk": COLOR_RED, "Reduces Churn Risk": COLOR_GREEN},
            )
            fig.update_layout(height=320, margin=dict(l=10, r=10, t=10, b=10), legend_title_text="")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.caption("Feature-level breakdown is only available for linear models.")
        st.markdown('</div>', unsafe_allow_html=True)

# =====================================================================================
# PAGE: MODEL ANALYTICS
# =====================================================================================
def page_model_analytics(artifacts, eval_art):
    st.markdown("## 📊 Model Analytics")
    st.caption("Performance evidence behind the selected production model.")

    if artifacts is None:
        st.error("Model artifacts not found.")
        return

    metrics = eval_art.get("metrics", {})
    best_params = eval_art.get("best_params", {})
    model_name = type(artifacts["model"]).__name__

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("#### 🏆 Selected Production Model")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1: kpi_card("Model", "Logistic Regression" if "Logistic" in model_name else model_name, "🏆", COLOR_GREEN)
    with c2: kpi_card("Accuracy", f"{metrics.get('accuracy',0)*100:.2f}%", "🎯")
    with c3: kpi_card("Precision", f"{metrics.get('precision',0)*100:.2f}%", "🎯")
    with c4: kpi_card("Recall", f"{metrics.get('recall',0)*100:.2f}%", "📈")
    with c5: kpi_card("F1 Score", f"{metrics.get('f1',0)*100:.2f}%", "⚖️")

    if best_params:
        st.markdown("**Best Hyperparameters (via GridSearchCV):**")
        st.code(", ".join(f"{k} = {v}" for k, v in best_params.items()), language="text")
    st.markdown('</div>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["📋 Model Comparison", "🧩 Confusion Matrix", "📈 Performance Charts", "🔬 Feature Importance"])

    with tab1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        comp = eval_art.get("comparison_df")
        if comp is not None:
            st.dataframe(comp.style.highlight_max(axis=0, subset=[c for c in comp.columns if comp[c].dtype != object], color="#D5F5E3"),
                         use_container_width=True)
            st.caption("Logistic Regression was selected as the best-performing, most stable model for production "
                       "deployment based on F1 score and generalization on the held-out test set.")
        else:
            st.warning(f"`{FILES['model_comparison']}` not found.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        cm = eval_art.get("confusion_matrix")
        if cm is not None:
            labels = ["No Churn", "Churn"]
            fig = px.imshow(
                cm, text_auto=True, x=labels, y=labels,
                color_continuous_scale=[[0, "#EAF1FB"], [1, COLOR_BLUE]],
                labels=dict(x="Predicted", y="Actual", color="Count"),
            )
            fig.update_layout(height=420)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning(f"`{FILES['confusion_matrix']}` not found.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        if metrics:
            perf_df = pd.DataFrame({
                "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
                "Score": [metrics.get("accuracy", 0), metrics.get("precision", 0),
                          metrics.get("recall", 0), metrics.get("f1", 0)],
            })
            fig = px.bar(perf_df, x="Metric", y="Score", color="Metric", text_auto=".2%",
                         color_discrete_sequence=[COLOR_BLUE, COLOR_GREEN, COLOR_ORANGE, COLOR_BLUE_LIGHT])
            fig.update_layout(yaxis_tickformat=".0%", showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)

            comp = eval_art.get("comparison_df")
            if comp is not None and "Model" in comp.columns:
                melt_cols = [c for c in ["Accuracy", "Precision", "Recall", "F1 Score"] if c in comp.columns]
                comp_melt = comp.melt(id_vars="Model", value_vars=melt_cols, var_name="Metric", value_name="Score")
                fig2 = px.bar(comp_melt, x="Model", y="Score", color="Metric", barmode="group", text_auto=".2f")
                fig2.update_layout(height=420, yaxis_tickformat=".0%")
                st.plotly_chart(fig2, use_container_width=True)
        else:
            st.warning(f"`{FILES['metrics']}` not found.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        model = artifacts["model"]
        feature_names = artifacts["feature_names"]
        if hasattr(model, "coef_"):
            coef_df = pd.DataFrame({"Feature": feature_names, "Importance": np.abs(model.coef_[0])})
            coef_df = coef_df.sort_values("Importance", ascending=False).head(15)
            fig = px.bar(coef_df.sort_values("Importance"), x="Importance", y="Feature", orientation="h",
                         color_discrete_sequence=[COLOR_BLUE])
            fig.update_layout(height=500, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig, use_container_width=True)
            st.caption("Importance = |Logistic Regression coefficient| on standardized features "
                       "(larger magnitude = stronger influence on churn prediction).")
        elif hasattr(model, "feature_importances_"):
            imp_df = pd.DataFrame({"Feature": feature_names, "Importance": model.feature_importances_})
            imp_df = imp_df.sort_values("Importance", ascending=False).head(15)
            fig = px.bar(imp_df.sort_values("Importance"), x="Importance", y="Feature", orientation="h",
                         color_discrete_sequence=[COLOR_BLUE])
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("The selected model does not expose feature importances.")
        st.markdown('</div>', unsafe_allow_html=True)


# =====================================================================================
# PAGE: CUSTOMER SEGMENTS
# =====================================================================================
def page_customer_segments(artifacts, dataset):
    st.markdown("## 👥 Customer Segments")
    st.caption("Behavioral segmentation via PCA + K-Means, applied to the full customer base.")

    if artifacts is None or dataset is None:
        st.error("Dataset or clustering artifacts not found.")
        return

    with st.spinner("Applying saved PCA and K-Means transforms to the dataset..."):
        view = compute_segment_view(artifacts, dataset_hash=len(dataset))

    if view is None:
        st.error("Could not build the segment view.")
        return

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("#### 🗺️ PCA Cluster Map")
    fig = px.scatter(
        view, x="PC1", y="PC2", color="Segment",
        color_discrete_map={
            BUDGET_LOYAL: COLOR_GREEN, AT_RISK: COLOR_RED, LOYAL_HIGH_VALUE: COLOR_BLUE,
        },
        opacity=0.65, hover_data=["tenure", "MonthlyCharges", "Contract"] if "Contract" in view.columns else None,
    )
    fig.update_layout(height=500, legend_title_text="Segment")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    agg_dict = {"tenure": "mean", "MonthlyCharges": "mean", "TotalCharges": "mean"}
    if "ChurnFlag" in view.columns:
        agg_dict["ChurnFlag"] = "mean"
    profile = view.groupby("Segment").agg(agg_dict).round(2)
    profile["Customers"] = view.groupby("Segment").size()
    if "ChurnFlag" in profile.columns:
        profile = profile.rename(columns={"ChurnFlag": "Churn Rate"})
        profile["Churn Rate"] = (profile["Churn Rate"] * 100).round(1).astype(str) + "%"
    profile = profile.rename(columns={
        "tenure": "Avg. Tenure (mo)", "MonthlyCharges": "Avg. Monthly Charges",
        "TotalCharges": "Avg. Total Charges",
    })

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("#### 📊 Cluster Profiles")
    st.dataframe(profile, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("#### 🧭 Segment Definitions")
    seg_cols = st.columns(3)
    for col, seg_name in zip(seg_cols, [BUDGET_LOYAL, AT_RISK, LOYAL_HIGH_VALUE]):
        with col:
            st.markdown(
                f"""
                <div class="section-card">
                    <h4>{SEGMENT_ICONS.get(seg_name,'📌')} {seg_name}</h4>
                    <p style="color:{COLOR_GREY};font-size:0.9rem;">{SEGMENT_DESCRIPTIONS.get(seg_name,'')}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


# =====================================================================================
# PAGE: RETENTION ADVISOR
# =====================================================================================
def page_retention_advisor():
    st.markdown("## 🤖 Retention Advisor")
    st.caption("Business action plan for the most recently analyzed customer.")

    if "last_result" not in st.session_state:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.info("No customer has been analyzed yet. Go to **🔍 Customer Analysis** to run an assessment first.")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    data = st.session_state["last_result"]
    report = data["report"]
    risk_level = report["Risk Level"]

    c1, c2, c3, c4 = st.columns(4)
    with c1: kpi_card("Customer Segment", report["Customer Segment"].split()[0], SEGMENT_ICONS.get(report["Customer Segment"], "📌"))
    with c2: kpi_card("Risk Level", risk_level, "🚨", RISK_COLORS.get(risk_level, COLOR_GREY))
    with c3: kpi_card("Business Priority", report["Business Priority"], "⚡", priority_color(report["Business Priority"]))
    with c4: kpi_card("Churn Probability", f"{report['Churn Probability (%)']}%", "📉")

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("#### 📌 Action Plan by Priority")
    tabs = st.tabs(["🔴 Critical", "🟠 High", "🟡 Medium", "🟢 Low"])
    priority_map = {"🔴 Critical": "Critical", "🟠 High": "High", "🟡 Medium": "Medium", "🟢 Low": "Low"}
    for tab, label in zip(tabs, priority_map.keys()):
        with tab:
            level = priority_map[label]
            filtered = [r for r in report["Recommendations"] if r["Priority"] == level]
            if filtered:
                render_recommendations(filtered)
            else:
                st.caption(f"No {level.lower()}-priority actions for this customer.")
    st.markdown('</div>', unsafe_allow_html=True)


# =====================================================================================
# PAGE: ABOUT PROJECT
# =====================================================================================
def page_about():
    st.markdown("## ℹ About Project")

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("#### Problem Statement")
    st.write(
        "Telecom operators lose significant recurring revenue every year to customer churn. "
        "This project builds an end-to-end intelligence system that predicts which customers "
        "are likely to leave, understands *why*, groups customers into actionable behavioral "
        "segments, and recommends targeted retention actions - turning raw customer data into "
        "a decision-ready business tool."
    )
    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("#### Dataset")
        st.write(
            "Telecom customer records including demographics, account information "
            "(tenure, contract, billing), subscribed services, and the churn label."
        )
        st.markdown("#### Technologies Used")
        st.markdown("".join(f'<span class="tech-badge">{b}</span>' for b in
                             ["Python", "Pandas", "NumPy", "scikit-learn", "Streamlit", "Plotly", "Joblib"]),
                    unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("#### ML Workflow")
        st.markdown(
            "1. Data cleaning & feature engineering (`AvgMonthlySpend`)\n"
            "2. One-Hot Encoding + Standard Scaling\n"
            "3. Model training & tuning: Logistic Regression, KNN, Decision Tree, Random Forest\n"
            "4. Model selection via GridSearchCV (F1-optimized)\n"
            "5. Dimensionality reduction with PCA (2 components)\n"
            "6. Customer segmentation with K-Means (k=3, elbow + silhouette validated)\n"
            "7. Rule-based Retention Advisor for recommendation generation"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("#### Core Components")
    t1, t2, t3, t4 = st.tabs(["Logistic Regression", "PCA", "K-Means Clustering", "Retention Advisor"])
    with t1:
        st.write(
            "The best-performing, most stable classifier after GridSearchCV tuning across "
            "Logistic Regression, KNN, Decision Tree, and Random Forest. Selected for its "
            "strong F1 score, interpretability (linear coefficients power the AI Decision "
            "Breakdown), and reliable generalization on the held-out test set."
        )
    with t2:
        st.write(
            "Principal Component Analysis reduces the encoded feature space to 2 dimensions "
            "for visualization and to stabilize the downstream clustering step, while "
            "preserving the dominant variance in customer behavior."
        )
    with t3:
        st.write(
            "K-Means (k=3, chosen via the elbow method and silhouette analysis) groups "
            "customers into three business-meaningful segments: Budget Loyal, At-Risk, and "
            "Loyal High-Value customers."
        )
    with t4:
        st.write(
            "A transparent, rule-based engine (`retention_advisor.py`) that combines contract "
            "type, tenure, pricing, payment method, service adoption, segment, and churn risk "
            "to generate prioritized, explainable retention recommendations."
        )
    st.markdown('</div>', unsafe_allow_html=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("#### Future Scope")
        st.markdown(
            "- Integrate SHAP for deeper model explainability\n"
            "- Real-time scoring via streaming customer events\n"
            "- A/B testing framework for retention offer effectiveness\n"
            "- CRM integration for automated action triggering"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("#### Developer Information")
        st.write("**Project:** AI-Powered Telecom Customer Intelligence & Retention System")
        st.write("**Type:** End-to-end Machine Learning + Business Intelligence Dashboard")
        st.write("**Stack:** Python · scikit-learn · Streamlit")
        st.markdown('</div>', unsafe_allow_html=True)


# =====================================================================================
# MAIN
# =====================================================================================
def main():
    load_css()

    artifacts, missing = load_artifacts()
    eval_art = load_eval_artifacts()
    dataset = load_dataset()

    if missing:
        st.warning(
            "⚠️ The following required model files were not found in the app folder: "
            f"**{', '.join(missing)}**. Place all files generated by `Train_Test_Model.ipynb` "
            "in the same directory as `app.py`, then refresh the page."
        )

    page = sidebar_nav()

    if page == "🏠 Dashboard":
        page_dashboard(artifacts, eval_art, dataset)
    elif page == "🔍 Customer Analysis":
        page_customer_analysis(artifacts)
    elif page == "📊 Model Analytics":
        page_model_analytics(artifacts, eval_art)
    elif page == "👥 Customer Segments":
        page_customer_segments(artifacts, dataset)
    elif page == "🤖 Retention Advisor":
        page_retention_advisor()
    elif page == "ℹ About Project":
        page_about()


if __name__ == "__main__":
    main()