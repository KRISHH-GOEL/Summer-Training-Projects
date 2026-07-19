# ❤️ Heart Disease Prediction using Machine Learning

A professional Machine Learning project that predicts the likelihood of heart disease based on a patient's clinical information. The project includes complete data preprocessing, model training, hyperparameter tuning, evaluation, model serialization, and a beautiful interactive Streamlit web application.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help healthcare professionals identify high-risk patients and assist in timely medical intervention.

This project uses a **Random Forest Classifier** trained on a heart disease dataset to predict whether a patient has heart disease based on multiple clinical attributes.

The project demonstrates a complete end-to-end Machine Learning workflow including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- Model Serialization
- Streamlit Deployment

---

## 🚀 Features

- Interactive Streamlit Web Application
- Real-time Heart Disease Prediction
- Prediction Confidence Score
- Model Performance Dashboard
- Hyperparameter Display
- Clean and Professional UI
- Pre-trained Machine Learning Model
- Label Encoding Support

---

## 📂 Project Structure

```
Heart-Disease-Prediction/
│
├── heart_app.py                 # Streamlit Application
├── heart_disease.ipynb          # Complete ML Notebook
├── Heart_Disease_Prediction.csv # Dataset
│
├── heart_disease_model.pkl      # Trained Random Forest Model
├── label_encoder.pkl            # Label Encoder
├── metrics.pkl                  # Model Evaluation Metrics
├── best_params.pkl              # Best Hyperparameters
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Features

The model uses the following patient attributes:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope of ST Segment
- Number of Major Vessels
- Thallium Scan Result

---

## 🤖 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis
4. Label Encoding
5. Train-Test Split
6. Model Training
7. Hyperparameter Tuning using GridSearchCV
8. Model Evaluation
9. Save Trained Model
10. Deploy using Streamlit

---

## 🧠 Model Used

- Random Forest Classifier

### Why Random Forest?

- High Accuracy
- Handles Non-linear Relationships
- Less Overfitting
- Robust Performance
- Excellent Classification Results

---

## 📈 Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

## 💻 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Heart-Disease-Prediction.git
```

Move into the project directory

```bash
cd Heart-Disease-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run heart_app.py
```

---

## 📸 Application Screens

The application includes:

- 🏠 Home Page
- ❤️ Prediction Page
- 📊 Model Performance Dashboard
- 🏆 Best Hyperparameters
- 🎯 Prediction Probability
- 📈 Confidence Score

---

## Example Prediction

Input:

```
Age: 45
Sex: Male
Chest Pain Type: 3
Blood Pressure: 120
Cholesterol: 200
Maximum Heart Rate: 150
```

Output:

```
Prediction:
Heart Disease Absent

Confidence:
96.42%
```

---

## 📚 Learning Outcomes

This project helped in understanding:

- Data Preprocessing
- Classification Algorithms
- Feature Engineering
- Hyperparameter Tuning
- Model Evaluation
- Model Serialization
- Streamlit Development
- End-to-End Machine Learning Pipeline

---

## 🔮 Future Improvements

- Add more ML algorithms for comparison
- Explain predictions using SHAP
- Feature Importance Visualization
- Cloud Deployment (Render/Streamlit Cloud)
- User Authentication
- PDF Prediction Reports
- Database Integration
- REST API using FastAPI

---

## 🤝 Contributing

Contributions are welcome!

If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Krish Goel**

B.Tech CSE Student | Machine Learning Enthusiast | Python Developer

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

## ⭐ If you like this project

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps support the project and motivates further development.

---

### ❤️ Built with Python, Scikit-learn & Streamlit
