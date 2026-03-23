from resume_parser import extract_text
SKILLS = [

"python",
"java",
"sql",
"machine learning",
"deep learning",
"tensorflow",
"data analysis",
"fastapi"

]

def extract_skills(text):

    found = []

    for skill in SKILLS:

        if skill in text:

            found.append(skill)

    return found
