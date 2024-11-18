salary = 5000 # Ежемесячная зарплата
spend = 6000 # Траты за первый месяц
months = 10 # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03 # Ежемесячный рост цен

safety_cushion = 0
current_spend = spend

for month in range(months):
  if month > 0:
    current_spend *= (1 + increase)
  safety_cushion += max(0, current_spend - salary)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {int(safety_cushion)}")