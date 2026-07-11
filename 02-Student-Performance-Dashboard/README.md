# 🎓 Student Performance Dashboard | Power BI

An interactive **Power BI dashboard** developed to analyze student academic performance and identify the factors that influence final grades. This project transforms raw student data into meaningful insights through interactive visualizations, KPIs, slicers, and DAX measures.

---
![Power BI](https://img.shields.io/badge/Power%20BI-Data%20Visualization-F2C811?logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-Analytics-blue)
![Power Query](https://img.shields.io/badge/Power%20Query-ETL-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Portfolio](https://img.shields.io/badge/Portfolio-Project-blueviolet)
![GitHub](https://img.shields.io/badge/GitHub-Open%20Source-black?logo=github)
## 📌 Project Overview

The objective of this project is to analyze students' academic performance and understand how various factors such as study time, previous failures, internet access, parental education, and career aspirations impact their final grades.

The dashboard provides an intuitive and interactive interface that enables users to filter data and explore different aspects of student performance with ease.

---

## 🚀 Dashboard Preview

> **Main Dashboard**

![Dashboard Preview](dashboard.png)

---

## 🎯 Objectives

- Analyze overall student performance.
- Identify the relationship between study habits and academic results.
- Examine the effect of previous failures on final grades.
- Explore demographic and family-related factors influencing performance.
- Build an interactive dashboard using Power BI.

---

## 📊 Dashboard Features

### KPI Cards
- 👨‍🎓 Total Students
- 📈 Average Final Grade (G3)
- ✅ Pass Rate
- ❌ Total Failures
- 📚 Average Study Time

### Interactive Slicers
- School
- Gender
- Age

### Visualizations
- 📈 Average Final Grade by Age
- 📊 Average Grade by Study Time
- 📉 Average Grade by Number of Failures
- 🎯 Study Time vs Final Grade (Scatter Plot)
- 🌳 Students by Guardian (Treemap)
- 🍩 Students Planning Higher Education
- 🍩 Students with Internet Access
- 📋 Matrix showing Average G1, G2 and G3 by School and Gender
- 🌲 Decomposition Tree for Grade Analysis

---

## 📈 Key Insights

Some interesting findings from the analysis include:

- Students with **higher study time generally achieve better final grades.**
- Previous academic failures show a **negative relationship** with final performance.
- A large majority of students aspire to pursue **higher education.**
- Most students have access to the internet.
- Mothers are the primary guardians for a significant proportion of students.

---

## 🛠️ Tools & Technologies

- Microsoft Power BI
- Power Query
- DAX (Data Analysis Expressions)
- Data Modeling
- Interactive Visualizations

---

## 📂 Dataset

This dashboard is built using the **Student Performance Dataset**, which contains demographic, academic, social, and family-related information about students.

Example attributes include:

- Age
- Gender
- Study Time
- Failures
- Guardian
- Internet Access
- Higher Education
- Final Grades (G1, G2, G3)

---

## 📐 Data Preparation

The following preprocessing steps were performed:

- Imported dataset into Power BI.
- Cleaned and transformed data using Power Query.
- Created calculated measures using DAX.
- Built relationships where required.
- Added slicers for interactive filtering.

---

## 📊 DAX Measures Used

Some of the key DAX measures include:

```DAX
Total Students = COUNTROWS(Student)

Average G3 = AVERAGE(Student[G3])

Average Study Time = AVERAGE(Student[studytime])

Total Failures = SUM(Student[failures])

Pass Rate =
DIVIDE(
    COUNTROWS(FILTER(Student, Student[G3] >= 10)),
    COUNTROWS(Student)
)
```

---

## 📁 Repository Structure

```
Student-Performance-Dashboard/
│
├── Dashboard.pbix
├── dataset.csv
├── dashboard.png
├── README.md
└── assets/
```

---

## 💡 Skills Demonstrated

- Data Cleaning
- Data Transformation
- Data Modeling
- DAX Calculations
- KPI Design
- Dashboard Design
- Interactive Filtering
- Business Intelligence
- Data Visualization
- Analytical Thinking

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

- Building professional Power BI dashboards
- Designing interactive reports
- Writing DAX measures
- Creating business-focused KPIs
- Visual storytelling using data
- Dashboard layout and UI design

---

## 📸 Dashboard Snapshot

<img src="dashboard.png" width="1000">

---

## 🔮 Future Improvements

Some possible enhancements include:

- Additional report pages with detailed analysis
- Predictive analytics using Machine Learning
- Drill-through reports
- Custom tooltips
- Dynamic report titles
- Mobile-optimized dashboard

---

## 👨‍💻 Author

**Krish Goel**

B.Tech Student | Aspiring Data Analyst | Power BI | Python | SQL

📌 GitHub: https://github.com/YourUsername

📌 LinkedIn: https://linkedin.com/in/YourProfile

---

## ⭐ If you found this project useful, consider giving it a star!
