# -------- Imports --------
from ingestion import load_resume_and_jd
from src.preprocessing import clean_text
from src.skill_extraction import extract_skills
from src.skill_gap import analyze_skill_gap
from src.similarity_engine import compute_similarity
from src.maturity_scoring import compute_maturity
from src.report_generator import generate_pdf_report


from src.ats_engine import (
    compute_ats_score,
    get_ats_verdict,
    section_skill_scores,
    generate_recommendations
)

# -------- Paths --------
resume_path = "data/resumes/resume_1.txt"
jd_path = "data/job_descriptions/jd_1.txt"

# -------- Load --------
resume_text, jd_text = load_resume_and_jd(resume_path, jd_path)

# -------- Preprocess --------
clean_resume = clean_text(resume_text)
clean_jd = clean_text(jd_text)

print("CLEAN RESUME TEXT:\n", clean_resume)
print("\nCLEAN JOB DESCRIPTION TEXT:\n", clean_jd)

# -------- Skill Extraction --------
resume_skills = extract_skills(clean_resume)
jd_skills = extract_skills(clean_jd)

print("\nResume Skills:", resume_skills)
print("JD Skills:", jd_skills)

# -------- Section Scores --------
section_scores = section_skill_scores(resume_skills, jd_skills)

print("\nSection Scores:")
for k, v in section_scores.items():
    print(k, ":", v, "%")

# -------- Skill Gap --------
gap_report = analyze_skill_gap(resume_skills, jd_skills)

print("\nMatched Skills:", gap_report["matched"])
print("Missing Skills:", gap_report["missing"])
print("Extra Skills:", gap_report["extra"])
print("Match Score:", gap_report["score"], "%")

# -------- Recommendations --------
recommendations = generate_recommendations(gap_report["missing"])

print("\nRecommendations:")
for r in recommendations:
    print("-", r)

# -------- Similarity --------
similarity_score = compute_similarity(clean_resume, clean_jd)
print("\nSemantic Similarity:", similarity_score, "%")

# -------- Maturity --------
final_score, maturity_level = compute_maturity(
    gap_report["score"],
    similarity_score,
    len(resume_skills)
)

print("\nMaturity Score:", final_score)
print("Level:", maturity_level)

# -------- ATS Score --------
ats_score, keyword_score = compute_ats_score(
    gap_report["score"],
    similarity_score,
    maturity_level,
    clean_resume
)

verdict = get_ats_verdict(ats_score)

print("\nATS Score:", ats_score)
print("Keyword Score:", keyword_score)
print("Verdict:", verdict)

# -------- PDF --------
generate_pdf_report(
    "report.pdf",
    resume_skills,
    jd_skills,
    gap_report,
    similarity_score,
    maturity_level,
    ats_score,
    verdict,
    recommendations,
    section_scores
)

print("\nPDF Report Generated → report.pdf")
