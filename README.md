# Multiple-disease-prediction

# Multiple Disease Prediction — Streamlit

## Overview

A Streamlit application for predicting multiple diseases — currently **Heart Disease** and **Diabetes** — using pre-trained machine learning models. Users can input clinical features to receive instant predictions along with probabilities. The app demonstrates end-to-end ML deployment, from data preprocessing to a clean, interactive web interface.

## Features

* Predicts **Heart Disease** & **Diabetes**
* Simple, user-friendly UI with sidebar inputs
* CSV batch prediction & export
* Displays prediction results and probabilities
* Modular design for adding more diseases and models

## Tech Stack

* Python, Streamlit
* scikit-learn, pandas, NumPy
* joblib for model loading
* matplotlib/plotly for optional visualizations

## Setup

1. Clone the repository:

```bash
git clone https://github.com/<username>/multiple-disease-prediction.git
cd multiple-disease-prediction
```

2. Create and activate a virtual environment (optional but recommended).
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

## Input Examples

**Heart Disease:** age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal

**Diabetes:** Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age

> Ensure the app's input fields match the features used when training each model.

## Deployment

* Deploy easily on Streamlit Cloud by linking your GitHub repo.
* Alternative options: Docker, Render, Heroku, AWS.

## Disclaimer

This application is for educational purposes only and should not be used as a substitute for professional medical diagnosis.

## Contact

**Avikal Bhatt** — [avikalbhatt123@gmail.com](mailto:avikalbhatt123@gmail.com)

