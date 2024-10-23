from collections import Counter


def most_common_value(lst):
    if not lst:
        return None  # Если список пустой, возвращаем None

    frequency = {}

    # Подсчитываем количество вхождений каждого элемента
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1

    # Находим значение с максимальным количеством вхождений
    most_common = max(frequency.items(), key=lambda x: x[1], default=None)

    return most_common


# Пример использования
input_list = input("Введите элементы списка, разделенные запятыми: ")
lst = [elem.strip() for elem in input_list.split(',')]

# Находим наиболее часто встречающееся значение
common_value = most_common_value(lst)

if common_value:
    value, frequency = common_value
    print(f"Наиболее часто встречающееся значение: '{value}' с количеством: {frequency}")
else:
    print("Нет данных для анализа.")
