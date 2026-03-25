# 💸 Smart Chit Analyzer

A full-stack web application that helps users track, analyze, and visualize their expenses with a clean dashboard and real-time insights.

---

## 🚀 Features

* ➕ Add and manage expenses
* 📋 View all expenses in a clean UI
* ❌ Delete expenses instantly
* 📊 Interactive analytics dashboard (Chart.js)
* 🧠 Category-wise spending insights
* 📅 Monthly expense tracking
* ⚡ Real-time updates without page reload

---

## 🧱 Tech Stack

### Frontend

* HTML5
* CSS3 (Modern UI, responsive design)
* JavaScript (Vanilla JS + Fetch API)

### Backend

* Python (Flask)
* Flask-CORS

### Database

* MongoDB (NoSQL, flexible schema)
* PyMongo

### Visualization

* Chart.js

---

## 📸 Screenshots

> Add your screenshots here

* Dashboard View
* Expense List
* Analytics Charts

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Dakshanreddym/smart-chit-analyzer.git
cd smart-chit-analyzer
```

---

### 2️⃣ Setup Backend

```bash
cd backend
python -m venv .venv
```

Activate virtual environment:

**Windows (PowerShell):**

```bash
.venv\Scripts\activate
```

**Windows (CMD):**

```bash
.venv\Scripts\activate.bat
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Flask server:

```bash
python app.py
```

---

### 3️⃣ Setup Frontend

Open `frontend/index.html` in your browser
(or use Live Server in VS Code)

---

## 🌐 API Endpoints

| Method | Endpoint          | Description           |
| ------ | ----------------- | --------------------- |
| POST   | /add              | Add new expense       |
| GET    | /expenses         | Get all expenses      |
| DELETE | /delete/<id>      | Delete expense        |
| GET    | /category-summary | Category-wise totals  |
| GET    | /monthly-summary  | Monthly spending data |

---

## 📊 Analytics (Chart.js)

* Pie Chart → Category-wise spending
* Bar Chart → Monthly spending trend

---

## 🧠 Why MongoDB?

* Handles flexible, semi-structured expense data
* Easy to extend (add tags, notes, receipts)
* No schema migration needed

---

## ⚡ Future Enhancements

* 🔐 User authentication (JWT)
* 🌙 Dark mode UI
* 📤 Export reports (PDF/CSV)
* 🧾 Receipt upload with OCR
* 🤖 AI-based spending insights

---

## 🧑‍💻 Author

**Dakshan Reddy**
GitHub: https://github.com/Dakshanreddym

---

## ⭐ Show Your Support

If you like this project:

* Star ⭐ the repo
* Fork 🍴 it
* Share 🚀 it

---

## 📌 Project Status

✅ Active and continuously improving
