# 🌞 Daylight & Ventilation Analyzer

An AI-powered tool that analyzes architectural floor plans or text descriptions to provide feedback on daylight exposure and natural ventilation potential. Built using **LangChain**, **Streamlit**, and **Tesseract OCR**.

---

## 🚀 Features

- 🖼 Upload floor plan images (PNG, JPG, JPEG) for OCR-based text extraction.
- ✍️ Enter text descriptions directly to get instant feedback.
- 🧠 Uses OpenAI (via LangChain) to provide architectural insight based on uploaded content.
- 📄 Outputs useful recommendations on daylight and ventilation optimization.

---

## 📂 Project Structure

daylight_analyzer/
│
├── app.py # Streamlit app entry point
├── analyze.py # Core LangChain-based logic
├── prompt_template.txt # Prompt used by the LLM
├── requirements.txt # Python dependencies
├── .gitignore # Ignore virtual env & unnecessary files

yaml
Copy
Edit

---

## ⚙️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/your-username/daylight_analyzer.git
cd daylight_analyzer
Create virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Install Tesseract OCR and add it to your system PATH

🔑 API Key Setup
Make sure you have your OpenAI API key ready. Set it as an environment variable:

bash
Copy
Edit
$env:OPENAI_API_KEY="your-api-key-here"   # PowerShell (Windows)
export OPENAI_API_KEY="your-api-key-here" # Mac/Linux
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
📷 Screenshot

🛠 Built With
LangChain

Streamlit

Pytesseract

OpenAI GPT-4

🙌 Contribute
Feel free to fork the repo, make enhancements, and open a PR! Contributions are welcome.

📜 License
MIT License © [Your Name]

yaml
Copy
Edit
