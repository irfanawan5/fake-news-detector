# 📰 Fake News Detection Project

## 📌 Project Overview
This project focuses on detecting fake news articles using Natural Language Processing (NLP) and Machine Learning techniques. It leverages labeled datasets to build predictive models that classify news as **real** or **fake**.

## 🎯 Goal & Problem Statement
- **Goal:** Build a classifier that accurately identifies fake news.
- **Problem:** Fake news is a major challenge, especially on social media, misleading people and distorting public opinion.

## 🛠️ Solution Approach
- Load and explore datasets.
- Clean and preprocess text data.
- Convert text to numerical features using **TF-IDF**.
- Train multiple machine learning models.
- Evaluate and select the best performing model.

## 📚 Libraries Used
- **pandas:** Data manipulation
- **numpy:** Numerical operations
- **matplotlib & seaborn:** Data visualization
- **scikit-learn:** Preprocessing, vectorization, model training, evaluation
- **nltk:** Text preprocessing tasks (stopwords removal, stemming)

## 📊 Dataset Details
- **fake.csv:** 23,481 articles (~52.3%)
- **true.csv:** 21,417 articles (~47.7%)
- **Combined dataset:** 44,898 articles, 5 features (including label)

## 🛤️ Step-by-Step Code Workflow
- Data Loading (pandas)
- Data Cleaning (removing nulls, irrelevant characters)
- Text Preprocessing (lowercasing, stopwords removal, stemming)
- TF-IDF Vectorization
- Model Training (Logistic Regression, PassiveAggressiveClassifier)
- Model Evaluation (Accuracy, Precision, Recall, F1-score, Confusion Matrix)

## 📈 Data Insights and Visualizations
- Distribution of real vs. fake articles
- Word clouds for real and fake news
- Histogram of article text lengths

## 🧠 Model Training & Evaluation
- **Best Model:** PassiveAggressiveClassifier
- **Accuracy Achieved:** ~98.76%

## 🚀 Web Application Deployment
- Built using **Streamlit** for a user-friendly web interface.
- Users can input news text and instantly predict whether it is **Fake** or **Real**.
- Technologies used: Python, Streamlit, scikit-learn, joblib, TF-IDF Vectorizer.

## 🏆 Outcome
- App tested successfully with multiple news samples.
- Predictions are fast and accurate.
- No issues found after optimization.

## ✅ Conclusion
This project demonstrates how machine learning can effectively tackle fake news detection through proper text preprocessing, model selection, and real-world deployment.

---

✍️ **Author:** Irfan Omer Awan  
📅 **Date:** 21-04-2025  

---

# 🙏 Thank You!
Thank you for reviewing this project. I hope you find it insightful and helpful!
