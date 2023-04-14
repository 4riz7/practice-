A = int(input("Введите размер стипендии: "))
B = int(input("Введите расходы на проживание: "))
total_expenses = 0

for i in range(10):
    total_expenses += B
    B *= 1.03

required_money = total_expenses - 10*A

print("Требуемая сумма денег для проживания учебного года: ", required_money)
