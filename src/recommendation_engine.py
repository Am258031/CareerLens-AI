# -------- Skill → Recommendation Map --------

RECOMMEND_DB = {

    "python": [
        "Learn Python for Data Science (Coursera / YouTube)",
        "Practice Python on LeetCode + Kaggle",
        "Build 2 ML mini projects"
    ],

    "machine learning": [
        "Complete ML course by Andrew Ng",
        "Implement 5 ML algorithms from scratch",
        "Do one end-to-end ML project"
    ],

    "nlp": [
        "Learn spaCy and NLTK basics",
        "Build a text classification project",
        "Practice preprocessing + embeddings"
    ],

    "mongodb": [
        "Learn MongoDB CRUD operations",
        "Build a Node + Mongo mini app",
        "Practice aggregation queries"
    ],

    "react": [
        "Build 3 React mini projects",
        "Learn hooks + state management",
        "Create one dashboard UI"
    ],

    "rest": [
        "Learn REST API design",
        "Build Express REST APIs",
        "Practice Postman testing"
    ],

        "pandas": [
        "Learn Pandas data manipulation (DataFrames, groupby, merge)",
        "Practice data cleaning on Kaggle datasets",
        "Build one data analysis mini project"
    ],

    "numpy": [
        "Learn NumPy arrays and vector operations",
        "Practice matrix and numerical computations",
        "Use NumPy inside ML preprocessing pipeline"
    ],

    "sql": [
        "Practice SQL queries (JOIN, GROUP BY, subqueries)",
        "Solve SQL problems on LeetCode / HackerRank",
        "Build a small DB-backed app"
    ],

    "node": [
        "Build REST APIs using Node.js",
        "Create one backend project with Express",
        "Learn middleware and routing"
    ],

    "express": [
        "Learn Express routing and middleware",
        "Build CRUD API with Express + MongoDB",
        "Practice API error handling"
    ],

}


# -------- Recommendation Function --------

def generate_recommendations(missing_skills):

    recs = {}

    for skill in missing_skills:
        if skill in RECOMMEND_DB:
            recs[skill] = RECOMMEND_DB[skill]
        else:
            recs[skill] = [
                f"Study fundamentals of {skill}",
                f"Build one project using {skill}"
            ]

    return recs
