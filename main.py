from lib.db import session
from lib.models import Transaction, Budget
import datetime
from sqlalchemy import func
from lib.utils import parse_date, format_currency

def show_menu():
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Generate Summary Report")
    print("6. Set Monthly Budget")
    print("7. View Budget Report")
    print("8. Exit")

def add_transaction(is_income=False):
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ")

    date = parse_date(date_str) if date_str else datetime.date.today()

    if not is_income:
        amount = -abs(amount)  # Store expenses as negative

    transaction = Transaction(description=description, amount=amount, category=category, date=date)
    session.add(transaction)
    session.commit()

    print("✅ Transaction saved!")

def view_transactions():
    transactions = session.query(Transaction).order_by(Transaction.date.desc()).all()
    print("\n--- Transactions ---")
    for t in transactions:
        print(f"{t.date} | {t.category:10} | {t.description:20} | {format_currency(t.amount)}")

def view_balance():
    total = session.query(Transaction).with_entities(Transaction.amount).all()
    balance = sum([t[0] for t in total])
    print(f"\n💰 Current Balance: {format_currency(balance)}")

def generate_summary():
    print("\n📊 Expense Summary by Category")
    
    results = session.query(
        Transaction.category,
        func.sum(Transaction.amount)
    ).group_by(Transaction.category).all()

    if not results:
        print("No transactions found.")
        return

    for category, total in results:
        print(f"{category:15} : {format_currency(total)}")

    overall = session.query(func.sum(Transaction.amount)).scalar()
    print("\n💰 Total Balance:", format_currency(overall))

def set_budget():
    category = input("Enter category: ").strip()
    amount = float(input("Enter monthly budget amount: "))
    month = input("Enter month (YYYY-MM): ")

    existing = session.query(Budget).filter_by(category=category, month=month).first()
    if existing:
        existing.amount = amount
        print("🔄 Budget updated.")
    else:
        session.add(Budget(category=category, amount=amount, month=month))
        print("✅ Budget set.")
    session.commit()

def check_budget():
    month = input("Enter month to check (YYYY-MM): ")

    budgets = session.query(Budget).filter_by(month=month).all()

    if not budgets:
        print("⚠️ No budgets found for this month.")
        return

    print(f"\n Budget Report for {month}")
    for budget in budgets:
        spent = session.query(func.sum(Transaction.amount)).filter(
            Transaction.category == budget.category,
            Transaction.date.like(f"{month}-%")
        ).scalar() or 0.0

        print(f"{budget.category:15} Budget: Ksh {budget.amount:.2f} | Spent: Ksh {abs(spent):.2f}")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(is_income=False)
        elif choice == "2":
            add_transaction(is_income=True)
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            view_balance()
        elif choice == "5":
            generate_summary()
        elif choice == "6":
            set_budget()
        elif choice == "7":
            check_budget()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
