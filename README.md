# ⚖️ Lexora AI

<p align="center">
  <img src="assets/logo.png" alt="Lexora AI Logo" width="140"/>
</p>

<h2 align="center">AI-Powered Legal Document Intelligence Platform</h2>

<p align="center">
Analyze legal agreements, detect legal risks, generate AI-powered summaries, translate documents, and interact with contracts using Google Gemini.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_AI-orange)
![License](https://img.shields.io/badge/License-Educational-green)

</p>

---

# 🚀 Overview

Lexora AI is an AI-powered legal document intelligence platform developed using **Python**, **Streamlit**, and **Google Gemini AI**.

The application simplifies complex legal agreements by automatically extracting text, generating executive summaries, detecting important legal clauses, assessing document risks, translating summaries into multiple languages, and allowing users to interact with legal documents through an AI-powered chatbot.

---

# ✨ Features

- 📄 Upload and analyze legal PDF documents
- 🤖 AI-generated executive summaries
- ⚠️ Legal risk assessment with interactive risk gauge
- 📑 Automatic clause detection
- 🌍 Multilingual translation
- 💬 AI-powered Legal Assistant
- 📥 Professional PDF report generation
- 📊 Interactive dashboard
- 🎨 Modern responsive Streamlit interface

---

# 📸 Application Preview

## 🏠 Home

![Home](docs/screenshots/01_home.png)

---

## 📊 Analysis Dashboard

![Dashboard](docs/screenshots/02_dashboard.png)

---

## 📝 AI Executive Summary

![Summary](docs/screenshots/03_summary.png)

---

## 🌍 Multilingual Translation

![Translation](docs/screenshots/04_translation.png)

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Frontend | Streamlit |
| AI Model | Google Gemini |
| PDF Processing | pdfplumber, PyMuPDF |
| Data Visualization | Plotly |
| Report Generation | ReportLab |
| Translation | Google Translate |
| Environment Variables | python-dotenv |

---

# 📂 Project Structure

```text
Project Root/
│
├── assets/
│   ├── logo.png
│   └── favicon.png
│
├── backend/
│   ├── chatbot.py
│   ├── clause_detector.py
│   ├── gemini_client.py
│   ├── pdf_utils.py
│   ├── report_generator.py
│   ├── risk_detector.py
│   ├── summarizer.py
│   └── translator.py
│
├── docs/
│   └── screenshots/
│
├── sample_documents/
├── uploads/
├── reports/
│
├── app.py
├── requirements.txt
├── README.md
└── .env.example
```

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Likitha116/lexora-ai-legal-document-analyzer.git
cd lexora-ai-legal-document-analyzer
```

---

### Create a virtual environment

```bash
python -m venv venv
```

---

### Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Generate your API key from **Google AI Studio**.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start at:

```
http://localhost:8501
```

---

# 📄 Sample Document

A sample employment agreement is included inside:

```text
sample_documents/
```

Upload it to quickly explore the application's features.

---

# 🎯 Future Enhancements

- 🎙 Voice-enabled AI Assistant
- 📄 OCR support for scanned legal documents
- ⚖️ Contract comparison
- ☁️ Cloud deployment
- 👤 User authentication
- 📊 Advanced analytics dashboard
- 📱 Mobile-friendly interface

---

# 👩‍💻 Author

**Likitha A**

Computer Science Engineering Student

- 🌐 GitHub: https://github.com/Likitha116
- 💼 LinkedIn: https://www.linkedin.com/in/likithaashok/

---

# 📜 License

This project is developed for **educational, research, and portfolio purposes**.

Feel free to explore, learn from, and build upon the project with appropriate attribution.

---

<p align="center">

### ⭐ If you found this project helpful, consider giving it a Star!

Made with ❤️ by **Likitha A**

</p>