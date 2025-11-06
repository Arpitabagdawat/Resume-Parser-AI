import os
import pytesseract
from pdf2image import convert_from_path
import pandas as pd

# --- Paths Setup ---
# 👇 Replace with your actual paths
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\Users\X-STAR\Downloads\resume_parser_ai\poppler-25.07.0\Library\bin"

RESUME_FOLDER = "raw"  # Folder where resumes are stored
OUTPUT_FILE = "parsed_resumes.xlsx"

# --- Function: Extract text from image PDFs ---
def extract_text_from_image_pdf(pdf_path):
    text = ""
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    for img in images:
        text += pytesseract.image_to_string(img)
    return text

# --- Function: Extract info ---
def extract_info(text):
    import re
    name = ""
    email = ""
    phone = ""
    skills = ""

    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    phone_match = re.search(r'\+?\d[\d\s-]{8,}\d', text)

    if email_match:
        email = email_match.group()
    if phone_match:
        phone = phone_match.group()

    # Basic name extraction (first line often name)
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if len(lines) > 0:
        name = lines[0]

    # Skills keyword check (simple demo)
    skill_keywords = ["Python", "C++", "Power BI", "SQL", "Excel", "Machine Learning", "Data Analysis"]
    found = [skill for skill in skill_keywords if skill.lower() in text.lower()]
    skills = ", ".join(found)

    return {"Name": name, "Email": email, "Phone": phone, "Skills": skills}

# --- Main Function ---
def main():
    data = []
    if not os.path.exists(RESUME_FOLDER):
        print(f"❌ Folder '{RESUME_FOLDER}' not found.")
        return

    for filename in os.listdir(RESUME_FOLDER):
        if filename.endswith(".pdf"):
            print(f"Processing: {filename}")
            file_path = os.path.join(RESUME_FOLDER, filename)
            text = extract_text_from_image_pdf(file_path)
            info = extract_info(text)
            info["FileName"] = filename
            data.append(info)

    df = pd.DataFrame(data)
    df.to_excel(OUTPUT_FILE, index=False)
    print(f"\n✅ Extraction complete! Results saved in '{OUTPUT_FILE}'")

# --- Run Script ---
if __name__ == "__main__":
    main()
