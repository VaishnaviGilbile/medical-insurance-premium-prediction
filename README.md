# 📊 Medical Insurance Premium Prediction

A full-stack Machine Learning project that predicts **medical insurance premiums** using health, lifestyle, and demographic data, with a deployed **Flask web application** for real-time predictions.

---

## 🚀 Project Overview

This project builds a regression model using **HistGradientBoostingRegressor** to estimate insurance charges. It also includes a **Flask-based web interface** where users can input their details and get instant predictions.

---

## 🎯 Objective

To develop an end-to-end system that:
- Trains a machine learning model on insurance data  
- Predicts medical insurance premiums  
- Provides a user-friendly web interface for real-time predictions  

---

## 📁 Dataset Features

The dataset includes:

- `age` – Age of the individual  
- `gender` – Male / Female  
- `bmi` – Body Mass Index  
- `children` – Number of dependents  
- `smoker` – Smoking status  
- `region` – Residential region  
- `medical_history` – Existing conditions  
- `family_medical_history` – Family health background  
- `exercise_frequency` – Physical activity level  
- `charges` – Insurance cost (target variable)  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:**
  - Pandas  
  - NumPy  
  - Matplotlib  
  - Seaborn  
  - Scikit-learn  
- **Model:** HistGradientBoostingRegressor  
- **Backend:** Flask  
- **Serialization:** Pickle  

---

## ⚙️ Workflow

### 1. Data Preprocessing
- Encoding categorical variables:
  - Gender, Smoker, Region  
  - Medical history & family history  
  - Exercise frequency  

### 2. Model Training
- Train-test split (80/20)  
- Model used: **HistGradientBoostingRegressor**  
- Evaluation metrics:
  - R² Score  

### 3. Model Saving
- Trained model saved using `pickle` → `train.pkl`

### 4. Web Application
- Built using Flask  
- Takes user input via HTML form  
- Converts inputs into encoded format  
- Predicts insurance premium in real-time  

