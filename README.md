<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 200" width="900" height="200">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d1117"/>
      <stop offset="100%" style="stop-color:#1a1a2e"/>
    </linearGradient>
    <linearGradient id="acc2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#a78bfa"/>
      <stop offset="100%" style="stop-color:#f472b6"/>
    </linearGradient>
  </defs>
  <rect width="900" height="200" fill="url(#bg2)" rx="12"/>
  <!-- Document shapes -->
  <rect x="680" y="30" width="70" height="90" rx="4" fill="#ffffff08" stroke="#a78bfa30" stroke-width="1"/>
  <rect x="688" y="45" width="54" height="4" rx="2" fill="#a78bfa40"/>
  <rect x="688" y="56" width="40" height="3" rx="2" fill="#a78bfa30"/>
  <rect x="688" y="65" width="48" height="3" rx="2" fill="#a78bfa25"/>
  <rect x="688" y="74" width="35" height="3" rx="2" fill="#a78bfa20"/>
  <rect x="688" y="83" width="50" height="3" rx="2" fill="#a78bfa30"/>
  <rect x="688" y="92" width="42" height="3" rx="2" fill="#a78bfa20"/>
  <rect x="688" y="101" width="30" height="3" rx="2" fill="#a78bfa15"/>
  <!-- Scan line effect -->
  <rect x="680" y="70" width="70" height="2" fill="#a78bfa" opacity="0.4"/>
  <!-- AI nodes -->
  <circle cx="800" cy="60" r="8" fill="#a78bfa30" stroke="#a78bfa" stroke-width="1.5"/>
  <circle cx="840" cy="90" r="6" fill="#f472b630" stroke="#f472b6" stroke-width="1.5"/>
  <circle cx="800" cy="120" r="8" fill="#a78bfa30" stroke="#a78bfa" stroke-width="1.5"/>
  <circle cx="856" cy="140" r="5" fill="#f472b630" stroke="#f472b6" stroke-width="1"/>
  <line x1="800" y1="60" x2="840" y2="90" stroke="#a78bfa50" stroke-width="1"/>
  <line x1="840" y1="90" x2="800" y2="120" stroke="#a78bfa50" stroke-width="1"/>
  <line x1="840" y1="90" x2="856" y2="140" stroke="#f472b650" stroke-width="1"/>
  <!-- Title -->
  <text x="50" y="90" font-family="Georgia, serif" font-size="36" font-weight="bold" fill="url(#acc2)">Resume Analyzer</text>
  <text x="50" y="130" font-family="Georgia, serif" font-size="18" fill="#c084fc" opacity="0.8">AI-Powered</text>
  <text x="50" y="162" font-family="monospace" font-size="12" fill="#6b7280">NLP · LLM · ATS Scoring · Skill Gap Analysis</text>
</svg>

# Resume Analyzer

> **AI-Powered Resume Analyzer — Intelligent parsing, scoring, and career insights using NLP and LLMs**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org)
[![NLP](https://img.shields.io/badge/NLP-spaCy%20%7C%20NLTK-09A3D5?style=flat-square)](https://spacy.io)
[![LLM](https://img.shields.io/badge/LLM-Powered-7C3AED?style=flat-square&logo=openai&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Complete-22c55e?style=flat-square)]()

</div>

---

## Overview

**Resume Analyzer** is an AI-powered tool that intelligently parses, evaluates, and provides actionable feedback on resumes. Leveraging natural language processing and large language model capabilities, it bridges the gap between a candidate's resume and what recruiters and ATS systems actually look for.

Whether you're a student entering the job market or a professional pivoting careers, this system provides data-driven, role-specific guidance to maximize your chances of getting shortlisted.

---

## Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                        Resume Analyzer                         │
│                                                                │
│   ┌──────────────┐    ┌───────────────┐     ┌───────────────┐  │
│   │  PDF / Text  │───▶│  NLP Parsing  │───▶│  Entity       │  │
│   │  Resume Input│    │  (spaCy/NLTK) │     │  Extraction   │  │
│   └──────────────┘    └───────────────┘     └──────┬────────┘  │
│                                                    │           │
│   ┌──────────────┐    ┌───────────────┐     ┌──────▼────────┐  │
│   │  Report &    │◀───│  ATS Score +  │◀───│  Skill Gap &  │  │
│   │  Suggestions │    │  Role Match   │     │  Keyword Scan │  │
│   └──────────────┘    └───────────────┘     └───────────────┘  │
│                                                                │
│   Pipeline: Resume → Parse → Analyze → Score → Recommend       │
└────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Resume Parsing** — Extracts skills, experience, education, and certifications from PDF/text resumes
- **ATS Compatibility Scoring** — Rates how well a resume will perform through Applicant Tracking Systems
- **Keyword Gap Analysis** — Compares resume content against target job descriptions
- **Skill Recommendations** — Suggests missing skills and courses based on career trajectory
- **Role-Fit Percentage** — AI-driven match score between resume and job role
- **Personalized Feedback** — Actionable, role-specific improvement suggestions

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.9+ |
| NLP | spaCy, NLTK, Transformers |
| PDF Processing | PyPDF2, pdfminer |
| AI/LLM | OpenAI API / Gemini |
| Notebook | Jupyter |
| Visualization | Matplotlib, WordCloud |

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/Akshat-C-Kulkarni/resume-analyzer.git
cd resume-analyzer

# Install dependencies
pip install -r requirements.txt

# Set up API key (if using LLM features)
export OPENAI_API_KEY=your_key_here

# Launch the notebook
jupyter notebook
```

---

## Project Structure

```
resume-analyzer/
├── data/                  # Sample resumes and job descriptions
├── notebooks/             # Main analysis notebook
├── src/
│   ├── parser.py          # Resume parsing logic
│   ├── scorer.py          # ATS & role-fit scoring
│   └── recommender.py     # Skill gap & recommendations
├── requirements.txt
└── README.md
```

---

## Sample Output

```
Resume Analysis Report
────────────────────────────────────────
Candidate       : Akshat C. Kulkarni
Role Target     : Data Scientist
ATS Score       : 82 / 100
Role Match      : 76%

Top Skills Found : Python, ML, SQL, Pandas
Missing Keywords : Docker, Spark, A/B Testing

Recommendations:
  → Add quantified project metrics
  → Include "feature engineering" keyword
  → Mention cloud platform experience (AWS/GCP)
────────────────────────────────────────
```

---

## Author

**Akshat C. Kulkarni**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/akshatckulkarni)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat-square&logo=github)](https://github.com/Akshat-C-Kulkarni)

---

<div align="center"><sub>Built with Python · NLP · LLM APIs · Jupyter</sub></div>
