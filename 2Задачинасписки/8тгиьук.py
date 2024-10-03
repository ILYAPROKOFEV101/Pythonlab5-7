import random

# Ввод количества строк (N) и столбцов (M) с преобразованием в целые числа
N = int(input("Введите число столбцов: "))
M = int(input("Введите число строк: "))

# Создаем двумерный список (матрицу) с элементами в диапазоне от 10 до 40
matrix = [[random.randint(10, 40) for _ in range(M)] for _ in range(N)]

# Выводим матрицу
print("Матрица:")
for row in matrix:
    print(row)

# Определяем строки, в которых есть хотя бы один элемент, делящийся на 5
rows_with_multiple_of_5 = [index for index, row in enumerate(matrix) if any(elem % 5 == 0 for elem in row)]

# Вывод результата
print("\nСтроки, содержащие хотя бы один элемент, который делится на 5:")
if rows_with_multiple_of_5:
    print(rows_with_multiple_of_5)
else:
    print("Таких строк нет")

