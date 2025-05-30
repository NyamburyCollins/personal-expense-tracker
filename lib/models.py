from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base
import datetime

# Create a base class for our models
Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)  # Negative for expenses, positive for income
    category = Column(String, nullable=False)
    date = Column(Date, default=datetime.date.today)

    def __repr__(self):
        return (
            f"<Transaction(description='{self.description}', "
            f"amount={self.amount}, category='{self.category}', date={self.date})>"
        )
class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    month = Column(String, nullable=False)  # e.g. "2024-06"

    def __repr__(self):
        return f"<Budget(category='{self.category}', amount={self.amount}, month='{self.month}')>"

