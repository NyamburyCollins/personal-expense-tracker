from lib.db import session
from lib.models import Transaction
import datetime

# Sample data
transactions = [
    Transaction(description="Lunch at Java", amount=-450, category="Food", date=datetime.date(2024, 5, 1)),
    Transaction(description="Freelance payment", amount=5000, category="Income", date=datetime.date(2024, 5, 3)),
    Transaction(description="Groceries", amount=-1200, category="Food", date=datetime.date(2024, 5, 4)),
    Transaction(description="Transport to town", amount=-300, category="Transport", date=datetime.date(2024, 5, 5)),
    Transaction(description="Bought a book", amount=-700, category="Shopping", date=datetime.date(2024, 5, 6)),
    Transaction(description="Allowance from parents", amount=3000, category="Income", date=datetime.date(2024, 5, 7)),

    Transaction(description="January Rent", amount=-10000, category="Rent", date=datetime.date(2025, 1, 5)),
    Transaction(description="Weekly Groceries", amount=-3200, category="Food", date=datetime.date(2025, 1, 6)),
    Transaction(description="Electricity Bill", amount=-2400, category="Utilities", date=datetime.date(2025, 1, 7)),

]

# Add to session and commit
session.add_all(transactions)
session.commit()
print("✅ Seed data inserted.")
