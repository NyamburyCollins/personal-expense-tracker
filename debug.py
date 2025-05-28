# debug.py
from lib.db import session
from lib.models import Transaction
import datetime
import ipdb

# Create a sample transaction (optional)
t = Transaction(description="Debug Test", amount=-100, category="Test", date=datetime.date.today())
session.add(t)
session.commit()

# Start interactive session
ipdb.set_trace()
