def factorial(n):
    if n < 0:
        return "Факторіал визначений тільки для невід'ємних чисел."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

user_input = int(input("Введіть невід'ємне ціле число: "))

result = factorial(user_input)
print(f"Факторіал числа {user_input}: {result}")