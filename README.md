# 🏠 House Price Prediction Using Machine Learning

## 📌 Project Overview

The real estate market is influenced by several factors such as property area, number of bedrooms, bathrooms, parking availability, property age, location rating, and distance from the city center. Estimating the selling price of a house manually can often be inaccurate and inconsistent.

This project implements a **House Price Prediction System** using **Linear Regression**, enabling users to estimate house prices based on key property features. The objective is to provide a data-driven solution that assists buyers, sellers, and real-estate agencies in making informed decisions. :contentReference[oaicite:0]{index=0}

---

## 🎯 Problem Statement

Develop a machine learning model capable of predicting house prices using property-related features such as:

- Area (Square Feet)
- Number of Bedrooms
- Number of Bathrooms
- Parking Spaces
- Property Age
- Location Rating
- Distance from City Center

The model should learn the relationship between these features and house prices and provide accurate predictions for new properties. :contentReference[oaicite:1]{index=1}

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Streamlit

---

## 📊 Dataset Features

| Feature | Description |
|----------|------------|
| Area_sqft | Total area of the property |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Parking | Number of parking spaces |
| Property_Age | Age of the property |
| Location_Rating | Location score/rating |
| Distance_from_City | Distance from city center |
| Price | Target variable |

---

## 🔄 Project Workflow

### 1. Data Collection
Collected housing data containing property features and corresponding prices.

### 2. Data Preprocessing
- Loaded dataset using Pandas
- Checked dataset shape and structure
- Verified column information
- Prepared features and target variables

### 3. Exploratory Data Analysis
- Analyzed dataset statistics
- Identified feature relationships
- Visualized important patterns

### 4. Model Training
Implemented **Linear Regression** using Scikit-Learn.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

### 5. Model Evaluation
Evaluated model performance using:

- R² Score
- Prediction Comparison
- Error Analysis

### 6. Deployment
Built a simple **Streamlit Application** that allows users to enter house details and receive predicted prices instantly.

---

## 📁 Project Structure

```text
House-Price-Prediction-ML
│
├── app.py
├── house_price_dataset.csv
├── House_Price_Prediction_Report.pdf
└── README.md
```

---

## 🚀 Key Learning Outcomes

Through this project, I gained practical experience in:

- Data Preprocessing
- Feature Selection
- Linear Regression
- Model Evaluation
- Machine Learning Workflow
- Streamlit Application Development
- End-to-End ML Project Development

---

## 💡 Future Improvements

- Add advanced regression models
- Improve dataset size and quality
- Deploy the application online
- Implement feature engineering techniques
- Compare multiple machine learning algorithms

---

## 👨‍💻 Author

**Sai Deva Harsha**

B.Tech CSE | Machine Learning Enthusiast | DSA Learner

GitHub: saidevaharsha07-art
