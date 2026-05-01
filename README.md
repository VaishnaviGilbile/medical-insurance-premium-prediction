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

## Project structure

- `app.py` - Flask application that serves the UI and uses the trained model to predict premiums.
- `train.py` - Script to train the regression model and save it as `train.pkl`.
- `train.pkl` - Pickled trained model (created by `train.py`).
- `insurance.csv` - Dataset used for training.
- `templates/` - HTML templates (`index.html`, `after.html`).
- `static/` - Static files (CSS).

## Prerequisites

- Python 3.8+ (this project was developed and tested with Python 3.9)
- pip
- A virtual environment is recommended

## Recommended packages

You can install required packages with pip. Example packages used in this project:

- flask
- pandas
- scikit-learn
- numpy

(If you want I can generate a `requirements.txt` automatically.)

## Setup

1. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install packages:

```bash
pip install flask pandas scikit-learn numpy
```

Training the model

If you wish to re-train the model (regenerates `train.pkl`):

```bash
python3 train.py
```

This script reads `insurance.csv`, encodes categorical columns (`gender`, `smoker`, `region`), trains a HistGradientBoostingRegressor and writes `train.pkl` in the project folder.

Important: `train.py` expects `insurance.csv` to have columns: `age, sex, bmi, children, smoker, region, charges`.

How the data is encoded

- gender: male -> 0, female -> 1
- smoker: yes -> 0, no -> 1
- region: southeast -> 0, southwest -> 1, northeast -> 2, northwest -> 3

The model is trained using these features (in this order):
- age, gender, bmi, children, smoker, region

Running the web app

1. Ensure `train.pkl` exists in the project root. If not, re-run `python3 train.py`.
2. Start the Flask app:

```bash
python3 app.py
```

3. Open your browser and navigate to http://127.0.0.1:5000


## UI:
<img width="1468" height="756" alt="image" src="https://github.com/user-attachments/assets/def0c090-5c41-43ca-bb0a-0f61f93bbde1" />


