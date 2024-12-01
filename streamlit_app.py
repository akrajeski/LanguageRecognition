import streamlit as st
import spacy
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load German SpaCy model
nlp = spacy.load("de_core_news_sm")

# Load the pre-trained model and vectorizer
model_path = "logistic_regression_model.pkl"  # Pre-saved model
vectorizer_path = "tfidf_vectorizer.pkl"      # Pre-saved vectorizer
cefr_model = joblib.load(model_path)
tfidf_vectorizer = joblib.load(vectorizer_path)

# Function for text cleaning
def clean_text(text, apply_lemmatization=True):
    if not isinstance(text, str):
        return text 

    # Lowercase the text
    text = text.lower()

    # Remove special characters, numbers, and extra spaces
    text = re.sub(r'[^a-zäöüß\s]', '', text)  # Retain only letters and German-specific characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace

    # Process the text using SpaCy
    doc = nlp(text)

    # Tokenize, remove stopwords, and optionally lemmatize
    tokens = [
        token.lemma_ if apply_lemmatization else token.text
        for token in doc if not token.is_stop
    ]

    # Join tokens back into a single string
    return ' '.join(tokens)

# Streamlit application
def main():
    st.title("German Sentence Fluency Level Estimator")
    st.write("Input a German sentence, and this application will estimate its fluency level (A1, A2, B1, B2, C1, C2).")

    # User input
    user_input = st.text_area("Enter a German sentence:", "")

    if st.button("Estimate Fluency Level"):
        if user_input.strip():
            # Clean and preprocess the user input
            cleaned_input = clean_text(user_input)

            # Transform the input using the trained TF-IDF vectorizer
            input_vector = tfidf_vectorizer.transform([cleaned_input])

            # Predict fluency level using the trained model
            prediction = cefr_model.predict(input_vector)
            predicted_level = prediction[0]

            st.success(f"Estimated Fluency Level: {predicted_level}")
        else:
            st.warning("Please enter a valid German sentence.")

if __name__ == "__main__":
    main()
