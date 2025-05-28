# main.py
from lib.db import session
from lib.models import Transaction
import datetime

def show_menu():
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Exit")

def add_transaction(is_income=False):
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ")

    if not date_str:
        date = datetime.date.today()
    else:
        from lib.utils import parse_date, format_currency

        date = parse_date(date_str)


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
        print(f"{t.date} | {t.category:10} | {t.description:20} | {'Ksh ' + str(t.amount):>8}")

def view_balance():
    total = session.query(Transaction).with_entities(Transaction.amount).all()
    balance = sum([t[0] for t in total])
    print(f"\n💰 Current Balance: Ksh {balance:.2f}")

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
            print("Goodbye! 💸")
            break
        else:
            print("Invalid option. Try again.")
