def month_to_season(numbers):
    if 1 <= numbers <= 2:
        return "Зима"
    elif 3 <= numbers <= 5:
        return "Весна"
    elif 6 <= numbers <= 8:
        return "Лето"
    elif 9 <= numbers <= 11:
        return "Осень"
    elif numbers == 12:
        return "Зима"
    else:
        return "Неверный номер месяца"


try:
    numbers = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(numbers))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
