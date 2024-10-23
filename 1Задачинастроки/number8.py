def count_digits(s):
    # Функция подсчитывает количество цифр в строке
    return sum(char.isdigit() for char in s)


def sort_by_digit_count(strings):
    # Сортируем массив строк по количеству цифр в строке
    return sorted(strings, key=count_digits)


# Пример использования
try:
    # Ввод массива строк от пользователя
    input_strings = input("Введите строки, разделенные запятыми: ")
    strings = [s.strip() for s in input_strings.split(',')]  # Разделяем строки и убираем лишние пробелы

    if not strings:
        raise ValueError("Вы не ввели ни одной строки.")

    sorted_strings = sort_by_digit_count(strings)

    print("Упорядоченный массив строк:", sorted_strings)

except ValueError as ve:
    print("Ошибка:", ve)
except Exception as e:
    print("Произошла ошибка:", e)
