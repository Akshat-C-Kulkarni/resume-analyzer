import streamlit as st
from pathlib import Path
import tempfile
import sys

# ----------------------------------
# Add project root to Python path
# ----------------------------------
root_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(root_dir))

# Now import the pipeline
from src.pipeline import predict_from_pdf

# ----------------------------------
# Streamlit UI
# ----------------------------------
st.set_page_config(page_title="AI-Powered Resume Analyzer")

st.title("📄 AI-Powered Resume Analyzer")
st.write("Upload your resume in PDF format to predict your job category.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.info("Extracting text and analyzing your resume...")

    try:
        prediction = predict_from_pdf(temp_path)
        st.success(f"🔍 **Predicted Category:** {prediction}")
    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
