# Step1:- set Skill Dictionary --------

SKILLS = {
    # Languages
    "python", "java", "c++", "javascript", "sql",

    # Web / MERN
    "react", "node", "express", "mongodb", "html", "css",

    # AI/ML/NLP
    "machine learning", "deep learning", "nlp",
    "pandas", "numpy", "scikit", "tensorflow", "pytorch",

    # Backend / DB
    "mysql", "api", "rest", "flask", "django",

    # Tools
    "git", "github", "docker", "excel", "power bi",

    # Concepts
    "dsa", "oop", "dbms", "os", "computer networks"
}


#Step 2:-> Skill Extraction Function --------

def extract_skills(text):
    text = text.lower()
    found = set()

    # check multi-word skills first
    for skill in SKILLS:
        if " " in skill:                 # multi-word skill
            if skill in text:
                found.add(skill)

    # single word matching
    words = set(text.split())

    for skill in SKILLS:
        if " " not in skill:
            if skill in words:
                found.add(skill)

    return found
