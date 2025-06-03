# 🎓 Student Performance Prediction in Mathematics

This project uses machine learning to predict students' final math grades based on various demographic, academic, and social features. It aims to help educators and stakeholders identify students at academic risk and intervene early to improve outcomes.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Objectives](#objectives)
- [Technologies Used](#technologies-used)
- [Data Preprocessing](#data-preprocessing)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Results](#results)
- [How to Run](#how-to-run)
- [Future Work](#future-work)
- [License](#license)

---

## 📖 Overview

The goal of this project is to predict students' final math performance (`G3`) using machine learning models. Insights from this model can help teachers and school administrations provide timely support for students.

---

## 📊 Dataset

- **Source**: UCI Machine Learning Repository  
- **Link**: [Student Performance Data Set](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Size**: 395 student records with 33 features
- **Target Variable**: `G3` (Final Math Grade)

**Key Features:**
- Demographic: `age`, `sex`, `address`
- Social: `famsize`, `guardian`, `romantic`
- Academic: `G1`, `G2`, `studytime`, `failures`, `absences`

---

## 🎯 Objectives

- Perform Exploratory Data Analysis (EDA)
- Preprocess the data for modeling
- Train and compare multiple machine learning models
- Evaluate model performance using regression metrics
- Visualize insights and predictions

---

## 🛠️ Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook

---

## ⚙️ Data Preprocessing

- Checked for missing values
- Encoded categorical variables using Label Encoding
- Standardized numeric features
- Split data into training and test sets (80/20)

---

## 🤖 Modeling

Machine Learning Models Used:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Regressor

---

## 📈 Evaluation

**Metrics Used:**
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

| Model              | MAE   | MSE   | R² Score |
|-------------------|-------|-------|----------|
| Linear Regression | 2.35  | 8.92  | 0.82     |
| Random Forest     | 1.75  | 6.42  | 0.89     |

---

## 🧠 Results

- The **Random Forest Regressor** outperformed other models.
- Prior grades (`G1`, `G2`) were the strongest predictors.
- Socio-demographic features had moderate impact.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git  https://github.com/AbishekMishra183/MiniProject.git
   cd  MiniProject
