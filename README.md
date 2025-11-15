# 📄 AI-Powered Resume Analyzer
## Week 2 Project – 4 Week / 4 Project Challenge

A simple NLP-powered web app that analyzes resumes and predicts the most suitable job field using machine learning.


## ⭐ Overview

This project allows users to upload their resume in PDF format, extracts text from the document, preprocesses it, and predicts the job domain that best matches the resume content.
It uses classical NLP + ML techniques and provides a clean Streamlit interface for easy interaction.


## 🚀 Features

- 📤 Upload resume (PDF)
- 📄 Automatic text extraction using pdfplumber
- 🔧 NLP preprocessing (tokenization, stopwords, stemming)
- 🤖 Job field prediction using a trained Random Forest model
- 🌐 Streamlit web application


## 🧠 Tech Stack

- Python 3
- pdfplumber (PDF text extraction)
- NLTK (tokenization & stopwords)
- Scikit-learn (ML model)
- Streamlit (web app)
- Joblib (model saving)


## 📁 Project Structure

Resume_Analyzer/
│
├── app/
│   └── app.py                    # Streamlit frontend
│
├── src/
│   ├── extraction.py             # PDF → Text extraction
│   ├── predict.py                # Preprocessing + prediction
│   ├── pipeline.py               # Full PDF → Prediction pipeline
│   └── __init__.py
│
├── model/
│   ├── resume_classifier_model.joblib
│   ├── vectorizer.joblib
│   └── label_classes.joblib
│
├── data/                          # Local dataset (ignored in Git)
│
├── requirements.txt
└── README.md


## ⚙️ Installation & Setup

### 1️⃣ Install dependencies
- pip install -r requirements.txt

### 2️⃣ Run the Streamlit app
- streamlit run app/app.py


## 🔍 Model Details

This project uses a Random Forest Classifier trained on the public
Resume Dataset by Snehaan Bhawal (Kaggle).
The model learns to classify resumes into categories like:
- Data Science
- Java Developer
- Python Developer
- HR
- Sales
- DevOps
- Web Designer
- …and many more.


🎯 Project Goals Achieved

- Built working resume PDF ingestion
- Extracted and cleaned resume text
- Created a trained ML classifier
- Integrated prediction into a Streamlit app
- Delivered a functional job-field recommendation tool


🔮 Possible Future Enhancements

- Extract structured information (Skills, Education, Experience)
- Provide AI-based resume improvement suggestions
- Support DOCX file format
- Add TF-IDF + Linear SVM for improved accuracy
- Match resumes against job descriptions


🙏 Acknowledgements

- Dataset: Resume Dataset – Snehaan Bhawal (Kaggle)
- Part of my 4 Week – 4 Project Challenge