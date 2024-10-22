import pulp

# Створення проблеми лінійного програмування для максимізації
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні: кількість виробленого лимонаду (x1) і фруктового соку (x2)
x1 = pulp.LpVariable("Lemonade", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Continuous')

# Цільова функція: максимізувати загальну кількість продуктів
model += x1 + x2, "Total_Products"

# Обмеження ресурсів
model += 2 * x1 + x2 <= 100, "Water_Constraint"         # Обмеження на воду
model += x1 <= 50, "Sugar_Constraint"                   # Обмеження на цукор
model += x1 <= 30, "Lemon_Juice_Constraint"             # Обмеження на лимонний сік
# Обмеження на фруктове пюре
model += 2 * x2 <= 40, "Fruit_Puree_Constraint"

# Розв'язання моделі
model.solve()

# Виведення результатів
print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Кількість лимонаду для виробництва: {x1.varValue}")
print(f"Кількість фруктового соку для виробництва: {x2.varValue}")
print(f"Загальна кількість вироблених продуктів: {
      pulp.value(model.objective)}")
