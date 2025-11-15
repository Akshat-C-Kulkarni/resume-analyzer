import joblib
import numpy as np
import re
import nltk

# Load stopwords & tokenizer
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

# -----------------------------
# Load trained model components
# -----------------------------
MODEL_PATH = "./model/resume_classifier_model.joblib"
VECTORIZER_PATH = "./model/vectorizer.joblib"
LABELS_PATH = "./model/label_classes.joblib"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
label_classes = joblib.load(LABELS_PATH)

stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

# ----------------------------------
# Preprocess text (same as training)
# ----------------------------------
def preprocess_text(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stop_words]
    tokens = [stemmer.stem(w) for w in tokens]
    return " ".join(tokens)

# ----------------------------------
# Prediction function
# ----------------------------------
def predict_category(raw_text):
    cleaned = preprocess_text(raw_text)
    vectorized = vectorizer.transform([cleaned])
    pred_index = model.predict(vectorized)[0]
    return pred_index

# For quick testing
if __name__ == "__main__":
    sample = """
Machine learning engineer skilled in python, data preprocessing, model training, 
tensorflow, scikit-learn, and building classification models.
"""
    print("Predicted Category:", predict_category(sample))
