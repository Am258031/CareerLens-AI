def analyze_skill_gap(resume_skills, jd_skills):

    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills
    extra = resume_skills - jd_skills

    if len(jd_skills) == 0:
        score = 0
    else:
        score = (len(matched) / len(jd_skills)) * 100

    return {
        "matched": matched,
        "missing": missing,
        "extra": extra,
        "score": round(score, 2)
    }
