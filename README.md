# 📄 CareerLens-AI | ATS + NLP Resume Analyzer

> An AI-powered Resume Analysis System that evaluates resumes against job descriptions using **Natural Language Processing (NLP)** and **ATS (Applicant Tracking System)** techniques. The system performs skill extraction, skill gap analysis, semantic similarity computation, ATS scoring, resume maturity evaluation, and generates an automated recruiter-style PDF report.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![NLP](https://img.shields.io/badge/NLP-Resume%20Analysis-green)
![SentenceTransformers](https://img.shields.io/badge/SentenceTransformers-Semantic%20Similarity-orange)
![ReportLab](https://img.shields.io/badge/ReportLab-PDF%20Generation-red)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

# 📌 Overview

Recruiters often receive hundreds of resumes for a single job posting. Manually evaluating every resume is time-consuming and inconsistent.

CareerLens-AI automates this process by analyzing resumes against job descriptions using NLP techniques. It identifies matching skills, missing skills, semantic similarity, ATS compatibility, and generates a recruiter-friendly PDF report with actionable recommendations.

---

# 🚀 Features

✅ Resume Text Preprocessing

✅ Job Description Analysis

✅ Skill Extraction using NLP

✅ Skill Gap Analysis

✅ Semantic Similarity using Sentence Transformers

✅ ATS Compatibility Score

✅ Resume Maturity Assessment

✅ Section-wise Skill Scoring

✅ Personalized Skill Recommendations

✅ Automated Recruiter PDF Report

---

# 🏗️ System Architecture

```text
                Resume + Job Description
                          │
                          ▼
                 Text Preprocessing
                          │
                          ▼
                  Skill Extraction
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
   Skill Gap Analysis             Semantic Similarity
          │                               │
          └───────────────┬───────────────┘
                          ▼
                   ATS Score Engine
                          │
                          ▼
               Resume Maturity Analysis
                          │
                          ▼
              Recommendation Generator
                          │
                          ▼
            Recruiter-style PDF Report
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| spaCy | NLP Text Processing |
| Sentence Transformers | Semantic Similarity |
| scikit-learn | Cosine Similarity |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| ReportLab | PDF Report Generation |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```text
CareerLens-AI/
│
├── data/
│   ├── resumes/
│   └── job_descriptions/
│
├── src/
│   ├── preprocessing.py
│   ├── skill_extraction.py
│   ├── skill_gap.py
│   ├── similarity_engine.py
│   ├── ats_engine.py
│   ├── maturity_scoring.py
│   ├── recommendation_engine.py
│   └── report_generator.py
│
├── app.py
├── ingestion.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Am258031/CareerLens-AI.git

cd CareerLens-AI
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

# ▶️ Usage

Run the application

```bash
python app.py
```

The application automatically:

- Loads Resume & Job Description
- Cleans the text
- Extracts technical skills
- Performs Skill Gap Analysis
- Computes Semantic Similarity
- Calculates ATS Score
- Evaluates Resume Maturity
- Generates Recommendations
- Creates Recruiter PDF Report

---

# 📊 Sample Output

The application generates:

- Resume Skills
- Job Description Skills
- Matched Skills
- Missing Skills
- Extra Skills
- Skill Match Score
- Semantic Similarity Score
- ATS Score
- Resume Maturity Level
- Personalized Recommendations
- Recruiter PDF Report

Example

```text
Matched Skills:
Python
Machine Learning
NLP
MongoDB

Missing Skills:
SQL
TensorFlow

ATS Score:
86%

Resume Maturity:
Industry Ready
```

---

# 📄 Recruiter PDF Report

The generated report contains:

- ATS Score Dashboard
- Semantic Similarity Score
- Resume Maturity Level
- Matched Skills
- Missing Skills
- Extra Skills
- Section-wise Skill Analysis
- Improvement Recommendations

---

# 🎯 Future Improvements

- Resume Ranking among Multiple Candidates

- AI Resume Rewriting Suggestions

- GPT-powered Resume Feedback

- Streamlit Web Dashboard

- Multi-format Resume Parsing (PDF/DOCX)

- LinkedIn Profile Analysis

- Resume Keyword Optimization

- Cloud Deployment

---

# 📷 Screenshots

## Console Output

(Add Screenshot)

---

## ATS Recruiter Report

(Add Screenshot)

---

## Skill Gap Analysis

(Add Screenshot)

---

# 💡 Learning Outcomes

This project helped in understanding:

- Natural Language Processing (NLP)

- Text Preprocessing

- Skill Extraction

- Semantic Similarity

- Sentence Transformers

- ATS Resume Evaluation

- PDF Report Generation

- Modular Python Architecture

- Real-world Recruiter Workflow

---

# 👨‍💻 Author

**Amjad Ali**

B.Tech Information Technology

GitHub: https://github.com/Am258031

LinkedIn: https://www.linkedin.com/in/amjad-ali-475927284/

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
