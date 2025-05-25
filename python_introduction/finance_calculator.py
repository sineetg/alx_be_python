income = input("Enter your monthly income: ")
expenses = input("Enter your total monthly expenses: ")

savings = int(income) - int(expenses)
interest = 0.05
projected_savings = (savings * 12) + (savings * 12 * interest)

print(f"Your monthly savings are {savings}.")
print(f"Projected savings after one year, with interest, is {projected_savings}.")