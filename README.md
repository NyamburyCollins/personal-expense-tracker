# 💸 Personal Expense Tracker

A cross-platform, open-source web app to track income and expenses, manage monthly budgets, and gain control of your finances.

---

## 🎯 Project Aim

Build a simple but powerful personal finance tracker where users can:
- Log income and expenses
- Set monthly budgets by category
- View summaries of spending habits
- Access their data from any device
- Customize and extend the app to fit their needs

---

## ✅ MVP Features

| Feature | Description |
|--------|-------------|
| 🧾 Track Income & Expenses | Users can input transactions (amount, category, description, date) |
| 🗂️ Categorization | Transactions are organized under custom categories like `Food`, `Rent`, `Transport`, etc. |
| 📅 Set Monthly Budgets | Define monthly budgets per category and compare them to real spending |
| 🌐 Accessible Anywhere | Cross-platform web interface using React (frontend) + FastAPI (backend) |
| 🛠️ Customizable & Open Source | Designed to be extended: add features like recurring bills, reminders, or currency conversion |

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Python + FastAPI |
| Frontend | React + Tailwind CSS |
| Database | SQLite (development), PostgreSQL (production-ready) |
| ORM | SQLAlchemy |
| Hosting | Render / Railway / Vercel |
| Optional | Docker, Chart.js, Auth (Post-MVP) |

---

## 🗂️ Folder Structure (Backend - Python)

```
personal-expense-tracker/
├── lib/
│   ├── models.py        # SQLAlchemy models
│   ├── db.py            # DB setup (engine, session)
│   ├── seed.py          # Sample transactions
├── main.py              # CLI for testing and adding transactions
├── debug.py             # Interactive shell using ipdb
├── expenses.db          # SQLite DB (auto-generated)
├── README.md            # You're reading it
```

---

## 🚀 Getting Started

### 1. Clone the project
```bash
git clone <repo-url>
cd personal-expense-tracker
```

### 2. Set up environment
```bash
pipenv install
pipenv shell
```

### 3. Seed the database
```bash
python lib/seed.py
```

### 4. Run CLI
```bash
python main.py
```

### 5. (Optional) Debug session
```bash
python debug.py
```

---

## 🔮 Future Features

- Recurring transactions
- Expense notifications
- Charts & analytics (by month/category)
- Export to PDF/CSV
- Mobile PWA version

---

## 👨‍💻 Author

**Collins Otieno Nyambury**  
📧 nyamburycollins@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/collins-nyambury-35a5a7239/) | [GitHub](https://github.com/NyamburyCollins?tab=repositories)

---

## 📝 License

MIT License
