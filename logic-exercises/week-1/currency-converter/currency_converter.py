# User introduces KRW amount
krw_amount = int(input("Introduce amount: "))


# Function converts KRW to USD
def converter(krw):
    usd = (krw / 1000) * 0.75
    return usd


# Convertion is applied to KRW amount
converted_amount = converter(krw_amount)

print(f"Your amount in USD = {converted_amount}")

if converted_amount < 100:
    print(f"2% Fee applied. Total amount: {round(converted_amount * 0.98, 2)}")
else:
    print(f"1% Fee applied. Total amount: {round(converted_amount * 0.99, 2)}")
