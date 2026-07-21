# 💵 Banknote Authentication Verifier using K-Nearest Neighbors (KNN)

A Machine Learning project that classifies banknotes as **Genuine** or **Forged** using the **K-Nearest Neighbors (KNN)** algorithm. This project includes data preprocessing, model training, evaluation, and an interactive **Streamlit web application** for real-time banknote authentication.

---

## 📌 Project Overview

Counterfeit currency detection is an important application of machine learning. This project uses the **Banknote Authentication Dataset** to build a KNN classifier capable of predicting whether a banknote is genuine or forged based on statistical features extracted from wavelet-transformed images.

---

## 🚀 Features

- 📊 Data preprocessing and cleaning
- 📈 Exploratory Data Analysis (EDA)
- 🔄 Feature scaling using StandardScaler
- 🤖 K-Nearest Neighbors (KNN) classifier
- 🎯 Hyperparameter tuning
- 📉 Model evaluation with multiple metrics
- 💾 Model and scaler serialization using Joblib
- 🌐 Interactive Streamlit web application
- 📋 Prediction confidence and class probabilities

---

## 📂 Dataset

The project uses the **Banknote Authentication Dataset**, which contains four numerical features extracted from wavelet-transformed images of banknotes.

### Input Features

| Feature | Description |
|----------|-------------|
| Variance | Variance of Wavelet Transformed Image |
| Skewness | Skewness of Wavelet Transformed Image |
| Curtosis | Curtosis of Wavelet Transformed Image |
| Entropy | Entropy of Image |

### Target Variable

| Value | Class |
|-------|-------|
| 0 | Genuine |
| 1 | Forged |

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

---

## 📁 Project Structure

```
Banknote-Authentication/
│
├── banknote.ipynb
├── banknote_app.py
├── banknote_model.pkl
├── scaler.pkl
├── evaluation_metrics.pkl
├── data_banknote_authentication.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Machine Learning Workflow

- Load Dataset
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Train-Test Split
- Feature Scaling
- KNN Model Training
- Hyperparameter Tuning
- Model Evaluation
- Save Model and Scaler
- Deploy with Streamlit

---

## 📊 Model Evaluation

The model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

## 💻 Streamlit Application

The application provides:

- Enter banknote feature values
- Predict Genuine or Forged banknotes
- Prediction confidence score
- Class probability table
- Dataset overview
- Model information
- Evaluation metrics
- Feature descriptions

---

## ▶️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Banknote-Authentication.git
```

### Navigate to the project directory

```bash
cd Banknote-Authentication
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run banknote_app.py
```

---

## 📸 Application Preview

### 🏠 Home Page

- Enter banknote features
- Predict authenticity
- View prediction confidence
- Display class probabilities

### ℹ️ About Model

- Dataset overview
- Model information
- Evaluation metrics
- Feature descriptions

---

## 🔮 Future Improvements

- Compare multiple machine learning algorithms
- Deploy on Streamlit Community Cloud
- Batch prediction using CSV upload
- REST API with FastAPI
- Docker containerization
- Improved visualizations and analytics dashboard

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Krish Goel**

Machine Learning • Data Science • Python


---

## ⭐ Support

If you found this project helpful, please consider **starring ⭐ the repository** to support the project and help others discover it.
