def calcilate_yearly_income(monthly_salary, fee):
    total = monthly_salary * (1 - fee) * 12
    return total


print(calcilate_yearly_income(50_000, 0.13))
print(calcilate_yearly_income(60_000, 0.13))
print(calcilate_yearly_income(70_000, 0.13))
print(calcilate_yearly_income(80_000, 0.13))