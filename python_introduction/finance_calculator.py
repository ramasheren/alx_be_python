monthly_income_str = input("Enter your monthly income: ")
monthly_income =  int(monthly_income_str)

monthly_expenses_str = input("Enter your total monthly expenses: ")
monthly_expenses =  int(monthly_expenses_str)

monthly_savings= monthly_income - monthly_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
