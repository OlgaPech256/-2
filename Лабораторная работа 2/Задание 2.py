money_capital = 20000 # Подушка безопасности
salary = 5000 # Ежемесячная зарплата
spend = 6000 # Траты за первый месяц
increase = 0.05 # Ежемесячный рост цен

months = 0
current_capital = money_capital
current_spend = spend

while current_capital >= 0:
  if salary >= current_spend:
    current_capital += salary - current_spend
  else:
    needed = current_spend - salary
    if current_capital >= needed:
      current_capital -= needed
    else:
      break #денег не хватает

  months += 1
  current_spend *= (1 + increase)


print("Количество месяцев, которое можно протянуть без долгов:", months)
