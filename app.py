import streamlit as st
import pickle
import numpy as np

# Load the model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Streamlit Interface
st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("📰 Fake News Detector")
st.subheader("Enter a news article below to check if it's Real or Fake:")

# User input
news_input = st.text_area("News Article", height=300)

# Prediction
if st.button("Check"):
    if news_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Preprocess and vectorize
        input_vector = vectorizer.transform([news_input])
        prediction = model.predict(input_vector)[0]
        probability = model.predict_proba(input_vector)[0]

        # Output result
        if prediction == 1:
            st.success("✅ This news appears to be **REAL**.")
        else:
            st.error("🚨 This news appears to be **FAKE**.")

        st.write(f"Confidence: {np.max(probability) * 100:.2f}%")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Scikit-learn")
