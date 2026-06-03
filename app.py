import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction App")
st.write("Enter house details below to predict the house price.")

df = pd.read_csv("house_price_dataset.csv")

X = df.drop("Price", axis=1)
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

area = st.number_input("Area (sq ft)", min_value=500, max_value=5000, value=1500)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
parking = st.number_input("Parking Spaces", min_value=0, max_value=5, value=1)
house_age = st.number_input("House Age", min_value=0, max_value=50, value=5)
location_rating = st.number_input("Location Rating", min_value=1, max_value=10, value=7)
distance = st.number_input("Distance from City Center (km)", min_value=1, max_value=50, value=10)

if st.button("Predict House Price"):
    new_house = pd.DataFrame(
        [[area, bedrooms, bathrooms, parking, house_age, location_rating, distance]],
        columns=X.columns
    )

    prediction = model.predict(new_house)

    st.success(f"🏡 Predicted House Price: ₹ {prediction[0]:,.2f}")