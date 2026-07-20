# 💰 Insurance Charges Prediction using Machine Learning

A Machine Learning project that predicts **medical insurance charges** based on a person's demographic and health-related information using a **K-Nearest Neighbors Regressor (KNN Regressor)**.

The project includes complete data preprocessing, model training, hyperparameter tuning using **GridSearchCV**, model evaluation, and a professional **Streamlit web application** for real-time predictions.

---

## 📌 Project Overview

Medical insurance costs vary significantly depending on several factors such as age, BMI, smoking habits, and family size.

This project builds a regression model capable of estimating insurance charges based on user inputs.

The application allows users to:

- Predict estimated insurance charges instantly
- View model performance metrics
- Explore model hyperparameters
- Preview the training dataset
- Understand how the model works

---

## 🎯 Problem Statement

Predict the expected medical insurance charges of an individual using machine learning based on their personal and health-related attributes.

---

## 📊 Dataset

The project uses the **Medical Insurance Cost Dataset**.

### Features

| Feature | Description |
|----------|-------------|
| Age | Age of the beneficiary |
| Sex | Male/Female |
| BMI | Body Mass Index |
| Children | Number of dependent children |
| Smoker | Smoking status |
| Region | Residential region |

### Target

- **Insurance Charges**

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib (during EDA)
- Jupyter Notebook

---

## 🤖 Machine Learning Model

After experimenting with different approaches, the final model selected was:

**K-Nearest Neighbors Regressor (KNN Regressor)**

The model was optimized using:

- GridSearchCV
- Cross Validation
- Feature Scaling (StandardScaler)

---

## 📈 Model Evaluation

The model was evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Cross Validation Score

The trained model, scaler, and evaluation metrics are saved using **Joblib** for deployment.

---

## 📂 Project Structure

```
Insurance-Charges-Prediction/
│
├── insurance.csv              # Dataset
├── insurance.ipynb            # Model training notebook
├── insurance_app.py           # Streamlit application
├── insurance_model.pkl        # Trained model
├── scaler.pkl                 # StandardScaler
├── model_metrics.pkl          # Saved evaluation metrics
├── README.md
└── requirements.txt
```

---

## 🚀 Streamlit Application

The application contains two main sections.

### 🏠 Home

- User-friendly prediction interface
- Input demographic details
- Predict insurance charges
- Display formatted prediction
- Input summary table

### 📊 About Model

- Dataset information
- Model performance metrics
- Best hyperparameters
- Dataset preview
- Project overview

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Insurance-Charges-Prediction.git
```

Move into the project directory

```bash
cd Insurance-Charges-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run insurance_app.py
```

---

## 📸 Application Preview

> Add screenshots of your Streamlit application here.

Example:

```
images/
    home.png
    prediction.png
    about_model.png
```

---

## 🧠 Machine Learning Workflow

```
Data Collection
        ↓
Data Cleaning
        ↓
Feature Encoding
        ↓
Train-Test Split
        ↓
Feature Scaling
        ↓
Model Training
        ↓
GridSearchCV
        ↓
Model Evaluation
        ↓
Model Saving
        ↓
Streamlit Deployment
```

---

## 📌 Future Improvements

- Include Region feature in prediction
- Add feature importance visualization
- Deploy on Streamlit Cloud
- Improve UI with charts
- Compare multiple regression algorithms
- Add prediction history

---

## 👨‍💻 Author

**Krish Goel**

Data Science & Machine Learning Enthusiast

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile

---

## ⭐ If you like this project

Give this repository a **Star ⭐** and feel free to fork it for your own learning.

---

## 📜 License

This project is licensed under the MIT License.

---

### Built with ❤️ using Python, Scikit-learn and Streamlit.
