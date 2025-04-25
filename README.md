```markdown
# Bookly API

A simple FastAPI project demonstrating CRUD operations on an in-memory “books” collection.

---

## 🚀 Prerequisites

- **Windows 10+**  
- **Python 3.8+** installed and on your `PATH`
- **Git** (to clone the repo)  
- **(Optional but recommended)** a virtual environment

---

## 📥 Setup

1. **Clone the repository**  
   ```powershell
   git clone https://github.com/KarthikSajwan/bookly-basics.git
   cd bookly-basics
   ```

2. **Create & activate a virtual environment**  
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate
   ```

3. **Install dependencies**  
   If you have a `requirements.txt`:
   ```powershell
   pip install -r requirements.txt
   ```
   Or directly:
   ```powershell
   pip install fastapi uvicorn
   ```

---

## ▶️ Running the Server

From the project root, run:

```powershell
uvicorn src.main:app --reload
```

- `src.main:app` tells Uvicorn to look for the `app` instance in `src/main.py`.  
- `--reload` makes the server automatically restart whenever you change code.

By default, it will start on **http://127.0.0.1:8000**.

---

## 📖 API Endpoints

All routes are prefixed with `/api/v1/books`:

| Method | Path                             | Description                       |
|--------|----------------------------------|-----------------------------------|
| GET    | `/api/v1/books/`                 | List **all** books                |
| POST   | `/api/v1/books/`                 | Create a **new** book             |
| GET    | `/api/v1/books/{id}`             | Get a **single** book by its `id` |
| PATCH  | `/api/v1/books/{id}`             | **Partially** update a book       |
| DELETE | `/api/v1/books/{id}`             | **Delete** a book by its `id`     |

### Example Requests

- **List all books**  
  ```
  GET http://127.0.0.1:8000/api/v1/books/
  ```

- **Create a book**  
  ```
  POST http://127.0.0.1:8000/api/v1/books/
  Content-Type: application/json

  {
    "id": 11,
    "title": "Comedy of Errors",
    "author": "Your Name",
    "publisher": "Funny Press",
    "published_date": "2025-04-25",
    "page_count": 123,
    "language": "English"
  }
  ```

- **Get a book by ID**  
  ```
  GET http://127.0.0.1:8000/api/v1/books/11
  ```

- **Partial update (PATCH)**  
  ```
  PATCH http://127.0.0.1:8000/api/v1/books/11
  Content-Type: application/json

  {
    "title": "Comedy of (Very) Serious Errors"
  }
  ```

- **Delete a book**  
  ```
  DELETE http://127.0.0.1:8000/api/v1/books/11
  ```

---
