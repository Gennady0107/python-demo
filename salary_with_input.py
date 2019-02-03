salary = float(input('Введиете ежемесячную зп '))
print(salary)
print(type(salary))
fee = 0.13
period = 12
salary_total_in_year = salary * (1 - fee) * period
print(salary_total_in_year)
