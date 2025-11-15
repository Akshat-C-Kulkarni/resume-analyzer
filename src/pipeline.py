from src.extraction import extract_text_from_pdf
from src.predict import predict_category

def predict_from_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    category = predict_category(text)
    return category

if __name__ == "__main__":
    sample_pdf = "data/sample_resume.pdf"  # Change if needed
    print("Predicted:", predict_from_pdf(sample_pdf))
