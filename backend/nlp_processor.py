import spacy
from resume_parser import extract_text
nlp = spacy.load("en_core_web_sm")

def process_text(text):
    doc = nlp(text)

    tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]

    return " ".join(tokens)

if __name__ == "__main__":

    path = r"C:\Users\Harnoor Singh\Downloads\Resume_Harnoor_Wipro.pdf"

    resume_text = extract_text(path)   # text comes from first file

    result = process_text(resume_text)

    print(result)
