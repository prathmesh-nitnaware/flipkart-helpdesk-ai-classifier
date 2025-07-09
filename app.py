# app.py

import streamlit as st
import joblib

# Load model, vectorizer, and label encoder
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Set page config
st.set_page_config(page_title="Flipkart Support Classifier", page_icon="📦", layout="centered")

# Title
st.title("📦 Flipkart Customer Support Query Classifier")
st.write("This app predicts whether a customer query is **Return/Refund related** or **Other**.")

# Input box
user_input = st.text_area("📝 Enter a customer support message:")

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Transform input
        X_input = vectorizer.transform([user_input])
        prediction = model.predict(X_input)[0]
        label = label_encoder.inverse_transform([prediction])[0]

        # Display result
        if label == 1:
            st.success("🔁 This query is **Return/Refund Related**.")
        else:
            st.info("📩 This query is **Other** (e.g., order, feedback, offers).")
