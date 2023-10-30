def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count

user_input = input("Введіть рядок: ")

result = count_vowels(user_input)
print(f"Кількість голосних у рядку: {result}")