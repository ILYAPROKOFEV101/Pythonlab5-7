def rearrange_string():
    input_string = input("Введите строку из 10 символов: ")

    # Проверка длины строки
    if len(input_string) != 10:
        raise ValueError("Строка должна содержать ровно 10 символов!")

    even_digits = []
    letters = []

    # Разделяем четные цифры и буквы
    for char in input_string:
        if char.isdigit() and int(char) % 2 == 0:
            even_digits.append(char)
        elif char.isalpha():
            letters.append(char)

    # Проверяем, что достаточно символов для соблюдения условий
    if len(even_digits) < 5 or len(letters) < 5:
        raise ValueError("Недостаточно четных цифр или букв для создания строки! "
                         "Необходимо минимум 5 четных цифр и 5 букв.")

    result = []

    # Расставляем четные цифры на четные позиции и буквы на нечетные
    for i in range(10):
        if i % 2 == 0:  # четные позиции
            result.append(even_digits.pop(0))
        else:  # нечетные позиции
            result.append(letters.pop(0))

    return ''.join(result)


try:
    output_string = rearrange_string()
    print("Сформированная строка:", output_string)
except ValueError as e:
    print(e)
