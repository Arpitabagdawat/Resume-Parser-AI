# Resume-Parser-AI

An AI-powered Resume Parser that automatically extracts key details such as **Name, Email, Phone Number, and Skills** from PDF resumes — including **image-based resumes** using OCR (Tesseract).  
This project simplifies resume screening and can be extended for **ATS systems or job-matching applications**.

---

## 🚀 Features
- ✅ Extracts text from **PDF and image-based resumes**
- ✅ Automatically identifies **Name, Email, Phone, and Skills**
- ✅ Supports **multiple resumes** at once
- ✅ Saves all parsed results in an **Excel file (`parsed_resumes.xlsx`)**
- ✅ Easy to expand with **Streamlit UI** or **Job Matching AI**

---

## 🗂️ Project Structure
```
resume_parser_ai/
│
├── raw/                     # Folder containing resumes (PDF/Image)

├── main.py                  # Main script

└── parsed_resumes.xlsx      # Output file
```

---

## ⚙️ Tech Stack
- **Python 3**
- **PyPDF2** – for text-based PDF extraction  
- **pytesseract** – for image-to-text conversion  
- **pdf2image** – for converting PDF pages to images  
- **spaCy** – for keyword and NLP processing  
- **pandas**, **openpyxl** – for Excel output


### 3️⃣ Install Tesseract OCR
- Download and install from: [Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki)
- Note the installation path, e.g.  
  `C:\Program Files\Tesseract-OCR\tesseract.exe`

### 4️⃣ Install Poppler for PDF to Image Conversion
- Download from: [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases)
- Extract and copy the **bin** folder path  
  Example:  
  `C:\Users\<YourName>\Downloads\poppler-xx\bin`

### 5️⃣ Run the Project
```bash
python main.py
```

---

## 📊 Output Example
| Name | Email | Phone | Skills | FileName |
|------|--------|--------|---------|----------|
| John Doe | john@email.com | +91-9876543210 | Python, SQL | Resume1.pdf |

✅ Output saved in: **`parsed_resumes.xlsx`**

---

## 🌟 Future Enhancements
- Add **Streamlit Web Interface** for uploading resumes  
- Integrate **Job Description Matching** (Match Score %)  
- Store results in **Database / Dashboard (Power BI or Tableau)**  
- Deploy using **Streamlit Cloud or Render**

---

## 👩‍💻 Author
**Arpita Bagdawat**  
🎓 B.Tech (AI & Data Science) | Mahakal Institute of Technology, Ujjain  
💼 Aspiring Data Analyst & Data Scientist  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/arpita-b-66a996292)

---

## 💬 Contribute
Feel free to **fork** this repository and open a pull request if you'd like to improve the project.  
If you find this project useful, don't forget to ⭐ the repo!

