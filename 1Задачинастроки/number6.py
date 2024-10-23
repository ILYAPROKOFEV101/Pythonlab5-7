import re  # Импортируем модуль re для работы с регулярными выражениями


def extract_words(input_string, delimiters):
    # Создаем регулярное выражение, которое использует любые символы из delimiters как разделители
    pattern = f"[{re.escape(delimiters)}]+"

    # Разбиваем строку по разделителям
    words = re.split(pattern, input_string)

    # Возвращаем все слова (убираем пустые строки, если они есть)
    return [word for word in words if word]


# Пример использования
try:
    input_string = input("Введите строку со словами: ")
    delimiters = input("Введите символы-разделители: ")

    # Проверка, что строка не пустая
    if not input_string or not delimiters:
        raise ValueError("Строка со словами и разделители не должны быть пустыми.")

    words = extract_words(input_string, delimiters)

    print("Слова в строке:", words)

except ValueError as ve:
    print("Ошибка:", ve)
except Exception as e:
    print("Произошла ошибка:", e)
