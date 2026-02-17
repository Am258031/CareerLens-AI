def compute_maturity(match_score, similarity_score, resume_skill_count):
    """
    Computes resume maturity level using
    weighted scoring model.
    """

    # -------- Weighted Score --------
    final_score = (
        0.5 * match_score +
        0.3 * similarity_score +
        0.2 * min(resume_skill_count * 5, 100)
    )

    final_score = round(final_score, 2)

    # -------- Level Mapping --------
    if final_score >= 75:
        level = "Industry Ready"
    elif final_score >= 50:
        level = "Developing"
    else:
        level = "Beginner"

    return final_score, level
