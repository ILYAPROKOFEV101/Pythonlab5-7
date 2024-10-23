def replace_elements(lst, old_value, new_value):
    # Заменяем old_value на new_value в каждом элементе списка
    for i in range(len(lst)):
        lst[i] = lst[i].replace(old_value, new_value)
    return lst



try:
#Ввод данных
    input_list = input("Введите элементы списка, разделенные запятыми: ")
    old_value = input("Введите значение, которое нужно заменить: ")
    new_value = input("Введите новое значение: ")

    # Преобразуем ввод в список
    lst = [elem.strip() for elem in input_list.split(',')]

    if not lst:
        raise ValueError("Список не должен быть пустым.")

    # Замена значений
    modified_list = replace_elements(lst, old_value, new_value)
    print("Измененный список:", modified_list)

except ValueError as ve:
    print("Ошибка:", ve)
except Exception as e:
    print("Произошла ошибка:", e)
