# CloudIt Questions – Project

This repository contains three key modules related to different AI and backend integrations:

---

## 📦 Project Structure

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
├── venv/                      # Python virtual environment (optional)
├── requirements.txt           # Python dependencies
└── note                       # Notes or markdowns (if any)
```

---

## 🔄 Step-by-Step Instructions to Run

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/your-username/CLOudit_Questions.git
cd CLOudit_Questions
```

> Replace `your-username` with the actual GitHub username.

---

### ✅ 2. Create and Activate Virtual Environment

#### Create:

```bash
python -m venv venv
```

#### Activate:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```

* **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

---

### ✅ 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

### ✅ 4. Run Tasks

#### ▶ Task 1: FastAPI CRUD (in `fastapi/`)

```bash
cd fastapi
uvicorn main:app --reload
```

#### ▶ Task 2: OpenAI Integration (in `openai_integration/`)

```bash
cd openai_integration
python main.py
```

#### ▶ Task 3: RAG Pipeline (in `RAG/`)

```bash
cd RAG
python main.py
```

---

### ✅ 5. Deactivate Virtual Environment (After Use)

```bash
deactivate
```

---

## ⚠️ Notes

* Ensure Python **3.9+** is installed.
* Update `.env` files in each folder with your API keys (like `OPENAI_API_KEY`, `GROQ_API_KEY`, etc.).
* Each task is modular and runs independently.
* For Task2 and Task3, I used Groq API instead of OpenAI.

---
