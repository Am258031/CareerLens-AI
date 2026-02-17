def compute_ats_score(gap_score, similarity_score, maturity_level, resume_text):
    
    # ----- maturity weight -----
    maturity_map = {
        "Beginner": 40,
        "Intermediate": 70,
        "Industry Ready": 90
    }

    maturity_score = maturity_map.get(maturity_level, 50)

    # ----- keyword density -----
    important_keywords = [
        "project", "experience", "skills",
        "machine learning", "nlp",
        "react", "node", "mongodb"
    ]

    keyword_hits = sum(1 for k in important_keywords if k in resume_text.lower())
    keyword_score = (keyword_hits / len(important_keywords)) * 100

    # ----- weighted ATS score -----
    ats = (
        gap_score * 0.4 +
        similarity_score * 0.3 +
        maturity_score * 0.2 +
        keyword_score * 0.1
    )

    return round(ats, 2), keyword_score
def get_ats_verdict(score):

    if score >= 80:
        return "Strong Match — Recruiter Ready"
    elif score >= 65:
        return "Moderate Match — Needs Minor Skill Boost"
    else:
        return "Low Match — Major Skill Gaps"

def section_skill_scores(resume_skills, jd_skills):

    categories = {
        "languages": {"python", "java", "c++", "javascript", "sql"},
        "frameworks": {"react", "node", "express"},
        "databases": {"mongodb", "mysql"},
        "ai": {"machine learning", "nlp", "pandas", "numpy"}
    }

    section_scores = {}

    for section, skill_set in categories.items():

        jd_sec = jd_skills & skill_set
        res_sec = resume_skills & skill_set

        if len(jd_sec) == 0:
            score = 100   # nothing required → full score
        else:
            score = (len(res_sec & jd_sec) / len(jd_sec)) * 100

        section_scores[section] = round(score, 1)

    return section_scores

def generate_recommendations(missing_skills):

    RECOMMEND_DB = {
        "python": "Learn Python for ML, backend APIs, and automation.",
        "sql": "Practice SQL queries, joins, and indexing.",
        "mongodb": "Build CRUD apps using MongoDB.",
        "react": "Create frontend dashboards using React.",
        "node": "Learn Node.js REST API development.",
        "express": "Understand Express routing & middleware.",
        "machine learning": "Build ML models using scikit-learn.",
        "nlp": "Practice text processing and NLP pipelines.",
        "pandas": "Use Pandas for data cleaning & analysis.",
        "numpy": "Learn NumPy arrays & vector operations."
    }

    recs = []

    for skill in missing_skills:
        if skill in RECOMMEND_DB:
            recs.append(RECOMMEND_DB[skill])

    if not recs:
        recs.append("Profile looks strong. Focus on advanced projects.")

    return recs
