def invest(amount, years, rate):
    for i in range(years):
        print(f"year {i}: ${amount}")
        amount = round(amount * (1+rate), 2)

amount = int(input("Enter the initial amount of investment: "))
years = int(input("Enter the amount of years to calculate: "))
rate = float(input("Enter the interest rate(not in percentage): "))

invest(amount, years, rate)