# 🚲 Bike Sharing Demand Prediction

A Machine Learning project that predicts the **daily number of bike rentals** based on weather conditions and calendar-related features. The model is deployed as an interactive **Streamlit web application**, allowing users to estimate bike demand by providing environmental and seasonal inputs.

---

## 📌 Project Overview

This project demonstrates an end-to-end Machine Learning workflow, including:

- Data Collection
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Model Deployment using Streamlit

The application predicts the estimated number of bike rentals using multiple weather and date-related features.

---

## 📂 Project Structure

```
Bike-Demand-Prediction/
│
├── Bike_Demand.ipynb          # Jupyter notebook for model training
├── bike_app.py                # Streamlit web application
├── bike_demand_model.pkl      # Trained Random Forest model
├── day.csv                    # Dataset
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## 🚀 Features

- Predict daily bike rental demand
- User-friendly Streamlit interface
- Weather and calendar-based predictions
- Random Forest Regression model
- Real-time prediction
- Clean and responsive UI

---

## 📊 Dataset

The project uses the **Bike Sharing Dataset**, which contains daily bike rental records along with weather and seasonal information.

### Input Features

- Season
- Year
- Month
- Holiday
- Weekday
- Working Day
- Weather Situation
- Temperature
- Humidity
- Wind Speed

### Target

- **Bike Rental Count**

---

## 🤖 Machine Learning Model

**Random Forest Regressor**

### Model Performance

- **R² Score: 0.88**

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Streamlit
- Joblib

---

## 📈 Machine Learning Workflow

1. Import Libraries
2. Load Dataset
3. Data Exploration
4. Data Cleaning
5. Exploratory Data Analysis (EDA)
6. Correlation Analysis
7. Feature Selection
8. Train-Test Split
9. Model Training
10. Model Evaluation
11. Save Model
12. Deploy with Streamlit

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Bike-Demand-Prediction.git
```

Navigate to the project directory

```bash
cd Bike-Demand-Prediction
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run bike_app.py
```

---

## 🎯 How to Use

1. Launch the Streamlit application.
2. Select:
   - Season
   - Year
   - Month
   - Holiday
   - Working Day
   - Weather Condition
3. Adjust:
   - Temperature
   - Humidity
   - Wind Speed
4. Click **Predict Bike Demand**.
5. View the estimated number of bike rentals.

---

## 📷 Application Preview

Add screenshots of your application here.

```
assets/
│
├── home.png
├── prediction.png
└── result.png
```

---

## 📦 Requirements

```
Python 3.10+
pandas
numpy
matplotlib
scikit-learn
streamlit
joblib
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🌱 Future Improvements

- Hyperparameter tuning
- Compare multiple regression models
- Add feature importance visualization
- Deploy on Streamlit Community Cloud
- Improve UI/UX
- Add historical demand graphs
- Predict hourly bike demand

---

## 📚 Learning Outcomes

This project helped in understanding:

- Data preprocessing
- Feature engineering
- Regression algorithms
- Random Forest Regression
- Model serialization using Joblib
- Streamlit deployment
- End-to-end Machine Learning workflow

---

## 👨‍💻 Author

**Krish Goel**

B.Tech Computer Science Student

Machine Learning | Data Science | Python

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub. It helps others discover the project and motivates future improvements.

---
