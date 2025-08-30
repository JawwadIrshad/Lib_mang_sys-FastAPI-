# 📚 Library Management System API

A secure, role-based backend system for managing books, borrow records, and users (librarians and students) using **FastAPI**, **JWT Authentication**, and **SQLite**.

---

## 🚀 Features

- **Authentication & Authorization**
  - JWT-based login/register
  - Role-based access control (Librarian / Student)

- **Librarian Capabilities**
  - Add, update, delete, and view books
  - View all borrow records

- **Student Capabilities**
  - View available books
  - Borrow/Return books
  - View own borrow history

- **Borrowing Logic**
  - Prevent over-borrowing (max 3 books per student)
  - Prevent borrowing when quantity is 0
  - Auto-update book quantity and due dates

---

## 📦 Technologies Used

- Python 3.10+
- FastAPI
- SQLModel / SQLAlchemy
- Pydantic
- JWT (python-jose)
- Passlib (Password hashing)
- SQLite
- Uvicorn (ASGI server)

---

## 🔧 Installation

```bash
git clone https://github.com/JawwadIrshad/Lib_mang_sys-FastAPI-.git
cd Lib_Mnag_sys(FastAPI)
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Unix/macOS

pip install -r requirements.txt
```

```bash
pip install -r requirements.txt
```

## 🧪 Run the Project

```bash
uvicorn main:app --reload
```

API will be available at:  
👉 http://127.0.0.1:8000  
Docs: http://127.0.0.1:8000/docs
