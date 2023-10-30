def is_even(number):
    return number % 2 == 0

user_input = input("Введіть число для перевірки: ")

try:
    number_to_check = int(user_input)
    result = is_even(number_to_check)

    if result:
        print(f"{number_to_check} є парним числом.")
    else:
        print(f"{number_to_check} є непарним числом.")

except ValueError:
    print("Введено некоректне число. Будь ласка, введіть ціле число.")