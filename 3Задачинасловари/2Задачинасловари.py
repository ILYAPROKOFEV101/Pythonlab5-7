import hashlib

# Словарь с банковскими ячейками и кодовыми словами
bank_cells = {
    101: "карта",
    102: "лес",
    103: "дом",
    104: "ноутбук",
    105: "стол"
}


# Функция для поиска ячейки по кодовому слову
def find_bank_cell_by_codeword(codeword):
    # Поиск номера ячейки по кодовому слову
    for cell_number, word in bank_cells.items():
        if word == codeword:
            # Хеширование кодового слова с помощью MD5
            md5_hash = hashlib.md5(codeword.encode()).hexdigest()
            return cell_number, md5_hash

    return None, None  # Если кодовое слово не найдено


# Пример использования
codeword_input = input("Введите кодовое слово: ")
cell_number, md5_hash = find_bank_cell_by_codeword(codeword_input)

if cell_number:
    print(f"Номер ячейки: {cell_number}")
    print(f"MD5-хеш кодового слова: {md5_hash}")
else:
    print("Кодовое слово не найдено.")

