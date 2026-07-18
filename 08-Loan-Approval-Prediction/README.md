# 🏦 Loan Approval Prediction using Machine Learning

A professional Machine Learning web application that predicts whether a customer's loan application is likely to be **Approved** or **Rejected** based on applicant and loan details.

The project is built using **Python**, **Scikit-Learn**, and **Streamlit**, and demonstrates the complete Machine Learning workflow from data preprocessing to model deployment.

---

## 📌 Project Overview

Financial institutions receive thousands of loan applications every day. Manually evaluating each application can be time-consuming and inconsistent.

This project uses a **Decision Tree Classifier** to automate loan approval prediction by analyzing applicant information such as income, education, credit history, loan amount, and more.

The application provides:

- Instant loan approval prediction
- Prediction confidence score
- Clean and interactive user interface
- Application summary after prediction

---

## 🚀 Features

- Professional Streamlit Web Interface
- Real-time Loan Approval Prediction
- Prediction Confidence Score
- User-friendly Input Forms
- Application Summary
- Responsive Layout
- Cached Model Loading
- Clean UI with Custom Styling

---

## 📂 Project Structure

```
Loan-Approval-Prediction/
│
├── loan_prediction.ipynb          # Model development
├── loan_app.py                    # Streamlit application
├── loan_prediction_model.pkl      # Trained ML model
├── loan_prediction_dataset.csv    # Dataset
├── requirements.txt
├── README.md
└── images/
    └── screenshot.png
```

---

## 📊 Dataset Features

The model uses the following features:

| Feature | Description |
|----------|-------------|
| Gender | Applicant Gender |
| Married | Marital Status |
| Dependents | Number of Dependents |
| Education | Education Level |
| Self Employed | Employment Status |
| Applicant Income | Monthly Applicant Income |
| Co-applicant Income | Monthly Co-applicant Income |
| Loan Amount | Requested Loan Amount |
| Loan Amount Term | Loan Repayment Term |
| Credit History | Previous Credit Record |

---

## 🤖 Machine Learning Model

**Algorithm Used**

- Decision Tree Classifier

### Problem Type

- Supervised Learning
- Binary Classification

### Workflow

- Data Cleaning
- Missing Value Handling
- Feature Encoding
- Model Training
- Model Evaluation
- Model Saving using Joblib
- Deployment with Streamlit

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Streamlit

---

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| Model | Decision Tree Classifier |
| Accuracy | **74%** |

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Loan-Approval-Prediction.git
```

Move into the project directory

```bash
cd Loan-Approval-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run loan_app.py
```

---

## 📷 Application Preview

### Home Page

> Add a screenshot of your application here.

```
images/screenshot.png
```

---

## 🧠 Input Parameters

The application accepts the following inputs:

- Gender
- Married Status
- Dependents
- Education
- Self Employed
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Term
- Credit History

---

## 📤 Output

The application predicts:

- ✅ Loan Approved
- ❌ Loan Rejected

along with the prediction confidence.

---

## 📚 Future Improvements

- Random Forest & XGBoost comparison
- Feature Importance Visualization
- SHAP Explainability
- Probability Gauge
- Database Integration
- User Authentication
- Cloud Deployment
- Model Performance Dashboard

---

## 🎯 Learning Outcomes

This project demonstrates:

- End-to-End Machine Learning Pipeline
- Data Preprocessing
- Classification Algorithms
- Model Serialization
- Streamlit Deployment
- Professional UI Development
- Machine Learning Project Structure

---

## 👨‍💻 Author

**Krish Goel**

Machine Learning | Data Science | Python Developer

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---

## 📄 License

This project is licensed under the MIT License.
