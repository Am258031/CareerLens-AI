def read_text_file(file_path):
    """
    Reads a text file and returns its content as a string.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def load_resume_and_jd(resume_path, jd_path):
    """
    Loads resume and job description text.
    """
    resume_text = read_text_file(resume_path)
    jd_text = read_text_file(jd_path)

    return resume_text, jd_text
