Here's your updated `README.md` content with **virtual environment creation**, **activation**, and **deactivation** steps added:

---

# CloudIt Questions – Project

This repository contains three key modules related to different AI and backend integrations:

---

## 📁 Folder Structure

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

## 🛠️ Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```

* **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Deactivate Virtual Environment

```bash
deactivate
```

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

* All tasks are modular and independent.
* Ensure Python 3.9+ is installed.
* Make sure `.env` files have the correct API keys and configs.
* For Task2 and Task3, I used Groq API instead of OpenAI.

---
