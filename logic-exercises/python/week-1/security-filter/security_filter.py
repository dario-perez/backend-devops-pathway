# List of daily expenses in KRW
daily_expenses = [5000, 12000, 3500, 7000]

# List of daily expenses in USD
expenses_in_usd = []

# Price of 1 USD in KRW
usd_1 = 1300

# Filter expenses that exceed the security threshold
suspicious_expenses = []

for expense in daily_expenses:
    if expense > 6000:
        suspicious_expenses.append(expense)

if not suspicious_expenses:
    print("No suspicious transactions detected")
else:
    print(f"Suspicious transactions detected: {suspicious_expenses}")


for krw_expense in daily_expenses:
    exchange = krw_expense / usd_1
    expenses_in_usd.append(round(exchange, 2))

if not expenses_in_usd:
    print("No expences")
else:
    print(f"USD expences: {expenses_in_usd}")
