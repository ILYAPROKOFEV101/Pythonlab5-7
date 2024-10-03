from collections import Counter

def most_frequent_value(lst):
    if not lst:  # Проверка на пустой список
        return None
    count = Counter(lst)
    most_common = count.most_common(1)  # Получаем самый частый элемент
    return most_common[0][0]  # Возвращаем значение

# Пример использования
my_list = ['a' , 'b', 'c', 'a', 'c', 'g', 'c', 'a', 'a']
result = most_frequent_value(my_list)
print(f"Наиболее часто встречающееся значение: {result}")
