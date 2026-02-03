# 🔐 Flask Authentication System (Oracle SQL)

A complete **Sign In & Sign Up web application** built using  
**Python (Flask)**, **Oracle SQL**, **HTML**, **CSS**, and **JavaScript**.

This project demonstrates backend authentication, database connectivity with Oracle, and a modern UI authentication portal.

# Demo

![Screen Recording 2026-02-03 104248 (1)](https://github.com/user-attachments/assets/b836a975-3eea-4921-a022-a34cec1ad9c2)
---

## 📌 Features

- ✅ User Registration (Sign Up)
- ✅ User Login (Sign In)
- ✅ Password hashing (secure authentication)
- ✅ Oracle SQL database integration
- ✅ Flask backend with REST APIs
- ✅ Modern responsive UI (Dark Theme)
- ✅ Session-based authentication
- ✅ Error handling & validation

---

## 🛠️ Technologies Used

| Layer | Technology |
|----|----|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python (Flask) |
| Database | Oracle SQL (XE / XEPDB1) |
| DB Driver | `oracledb` (Thin mode) |
| Version Control | Git & GitHub |

---



## 📂 Project Structure
flask-oracle-auth/


├── app.py            
├── db_config.py      
├── requirements.txt  
├── README.md 


├── templates/


│ └── index.html 




---

## 🗄️ Oracle Database Schema

```sql
CREATE TABLE users (
    user_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR2(50) NOT NULL,
    email VARCHAR2(100) UNIQUE NOT NULL,
    password VARCHAR2(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


⚙️ Setup Instructions (Local)
1️⃣ Install Python Dependencies
pip install -r requirements.txt

2️⃣ Update Database Credentials

Edit db_config.py:

oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost/XEPDB1"
)

3️⃣ Run the Application
python app.py


Open browser:

http://127.0.0.1:5000

🧪 Test Credentials Flow

Sign Up → create new user

Sign In → login using same credentials









