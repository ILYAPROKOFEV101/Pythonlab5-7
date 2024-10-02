import re


def extract_words(input_string, delimiters):
    # Создаем регулярное выражение, которое использует любые символы из delimiters как разделители
    pattern = f"[{re.escape(delimiters)}]+"

    # Разбиваем строку по разделителям
    words = re.split(pattern, input_string)

    # Возвращаем все слова (убираем пустые строки, если они есть)
    return [word for word in words if word]


# Пример использования
input_string = input("Введите строку со словами: ")
delimiters = input("Введите символы-разделители: ")
words = extract_words(input_string, delimiters)

print("Слова в строке:", words)
