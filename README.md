# AI Compliance Intelligence System

An AI-driven Policy and Compliance Intelligence System developed using Python, NLP, Sentence Transformers, and Streamlit to automate the analysis of policy documents and identify compliance risks with explainable insights.

---

# 📌 Project Overview

Organizations in industries such as healthcare, finance, insurance, and legal services deal with large volumes of policy and regulatory documents. Manual review of these documents is time-consuming and error-prone.

This project automates policy analysis by:
- Extracting text from PDF policy documents
- Preprocessing and segmenting text into clauses/sentences
- Generating semantic embeddings
- Performing AI-assisted compliance risk assessment
- Providing explainable risk insights through an interactive Streamlit application

---

# 🚀 Features

- 📄 PDF Policy Upload
- 🧠 NLP-based Text Processing
- 🔍 Semantic Embedding Generation
- ⚠️ Compliance Risk Classification
- 💡 Explainable AI Insights
- 🎨 Interactive Streamlit Dashboard
- 📊 Risk-Level Filtering

---

# 🛠️ Technologies Used

- Python
- Streamlit
- pdfplumber
- NLTK
- SentenceTransformers
- scikit-learn
- spaCy

---

# 📂 Project Structure

```text
AI-Compliance-System/
│
├── app.py
├── requirements.txt
├── README.md
├── preprocessing.ipynb
│
├── data/
│   ├── raw/
│   │   └── policy.pdf
│   │
│   └── processed/
│       ├── cleaned_data.json
│       └── final_output.json
│
├── screenshots/
│   └── app_output.png
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Compliance-System.git
cd AI-Compliance-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Run the Streamlit application:

```bash
py -m streamlit run app.py
```

If your file is inside an `app/` folder:

```bash
py -m streamlit run app/app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

# 🧠 Risk Classification Logic

| Risk Level | Description |
|------------|-------------|
| 🔴 High | Restrictions, penalties, violations |
| 🟡 Medium | Obligations and compliance requirements |
| 🟢 Low | General informational statements |

---

# 📊 Workflow

1. Upload PDF document
2. Extract text using pdfplumber
3. Clean and preprocess text
4. Split text into sentences
5. Generate semantic embeddings
6. Assign compliance risk level
7. Display explainable insights in Streamlit UI

---

# 📸 Sample Output

The application displays:
- Sentence/Clause
- Risk Level
- Explainable Reason
- Risk-based color highlighting

---

# 🔮 Future Enhancements

- Transformer-based legal NLP models
- Semantic similarity search
- Vector database integration (FAISS / ChromaDB)
- OCR support for scanned PDFs
- Cloud deployment
- Chatbot-based compliance querying

---

# 📚 References

- Streamlit Documentation  
- NLTK Documentation  
- SentenceTransformers Documentation  
- pdfplumber GitHub Repository  
- scikit-learn Documentation  

---

# 👨‍💻 Author

John Daniel

Industry Project – AI-Driven Policy & Compliance Intelligence System
