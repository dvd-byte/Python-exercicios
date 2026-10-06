salary = int(input("Enter your salary: "))
salary_increase = int(input("Enter the percentage of salary increase: "))
new_salary = salary + (salary * (salary_increase / 100))
print(f"Your new salary is: ${new_salary:.2f}")