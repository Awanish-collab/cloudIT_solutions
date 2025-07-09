# CloudIt Questions – Project

This repository contains three key modules related to different AI and backend integrations:

### Folder Structure:

```
CLOudit_Questions/
│
├── fastapi/
│   └── main.py                 # FastAPI-based user CRUD API
│
├── openai_integration/
│   ├── .env                    # Stores OpenAI or Groq API keys
│   └── main.py                 # Integration with OpenAI/Groq LLM
│
├── RAG/
│   ├── chroma_db_storage/     # Persistent Chroma DB vector storage
│   ├── .env                   # API key or config environment file
│   ├── data.json              # Input data for RAG
│   └── main.py                # RAG pipeline using embeddings + LLM
│
├── venv/                      # Python virtual environment
├── requirements.txt           # Python dependencies
└── note                       # Notes or markdowns (if any)
```

---

## 🔧 Setup Instructions

1. **Install required dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**

   * Make sure to populate the `.env` files in each module with the appropriate API keys (e.g., `GROQ_API_KEY`, `OPENAI_API_KEY`).

---

## 🚀 How to Run

### ✅ Task 1: FastAPI CRUD (Located in `fastapi/`)

```bash
cd fastapi
uvicorn main:app --reload
```

### ✅ Task 2: OpenAI Integration (Located in `openai_integration/`)

```bash
cd openai_integration
python main.py
```

### ✅ Task 3: RAG Pipeline (Located in `RAG/`)

```bash
cd RAG
python main.py
```

---

## 📌 Notes

* All tasks are modularized and can be executed independently.
* Ensure Python 3.9+ is used.
* Use virtual environment (`venv/`) for dependency isolation.

---

