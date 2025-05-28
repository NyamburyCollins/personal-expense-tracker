import datetime

def parse_date(date_str):
    """
    Parses a string into a date object.
    If empty or invalid, returns today's date.
    """
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return datetime.date.today()

def format_currency(amount):
    """
    Formats a float value as Ksh currency.
    """
    return f"Ksh {amount:,.2f}"

def sanitize_string(text):
    """
    Strips leading/trailing spaces and ensures consistent formatting.
    """
    return text.strip().capitalize()
