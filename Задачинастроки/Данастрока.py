def rearrange_string():
    input_string = input("Введите строку из 10 символов: ")
    even_digits = []
    letters = []

    # Разделяем цифры и буквы
    for char in input_string:
        if char.isdigit() and int(char) % 2 == 0:
            even_digits.append(char)
        elif char.isalpha():
            letters.append(char)

    # Проверяем, что достаточно символов для соблюдения условий
    if len(even_digits) < 5 or len(letters) < 5:
        return "Недостаточно символов для создания строки!"

    result = []

    # Расставляем буквы на нечетные позиции и цифры на четные
    for i in range(10):
        if i % 2 == 0:
            result.append(letters.pop(0))
        else:
            result.append(even_digits.pop(0))

    return ''.join(result)



output_string = rearrange_string()
print(output_string)
