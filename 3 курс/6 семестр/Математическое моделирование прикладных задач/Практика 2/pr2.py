Q = float(input("Введите сумму кредита: "))
n = int(input("Введите количество лет: "))
p = float(input("Введите годовую процентную ставку (%): "))

months = int(n) * 12
month_percentage = p / 12 / 100  # Переводим процентную ставку в доли

if month_percentage > 0:
    payment = (Q * month_percentage) / (1 - (1 + month_percentage) ** -months)
else:
    payment = Q / months

print(f"{'Период':<10}{'Задолженность на начало периода':<30}{'Ежемесячный платеж':<20}{'Остаток по задолженности':<30}")

for i in range(1, months + 1):
    interest_for_month = Q * month_percentage
    principal_payment = payment - interest_for_month
    Q -= principal_payment

    # В последний месяц корректируем платеж, чтобы остаток был равен нулю
    # if i == months:
    #    payment = Q + interest_for_month
    #    Q = 0
    if Q + principal_payment < payment:
        payment = Q + principal_payment
        Q = 0

    print(f"{i:<10}{Q + principal_payment:<30.2f}{payment:<20.2f}{Q:<30.2f}")
