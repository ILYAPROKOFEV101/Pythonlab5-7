def count_digits(s):
    # Функция подсчитывает количество цифр в строке
    return sum(char.isdigit() for char in s)

def sort_by_digit_count(strings):
    # Сортируем массив строк по количеству цифр в строке

    return sorted(strings, key = count_digits)

# Пример использования
strings = ["abc123", "a1b2", "4567", "no digits", "123abc456"]
sorted_strings = sort_by_digit_count(strings)

print("Упорядоченный массив строк:", sorted_strings)
