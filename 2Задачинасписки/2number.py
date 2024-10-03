def is_valid_extension(filename, allowed_extensions):
    # Получаем расширение файла
    file_extension = filename.split('.')[-1].lower()  # Преобразуем расширение в нижний регистр
    # Проверяем, входит ли расширение в список допустимых
    return file_extension in allowed_extensions

# Пример использования
filename = input("Введите имя файла: ")
allowed_extensions = ['jpg', 'png', 'gif', 'txt', 'pdf', 'py', "kt", 'cpp']  # Список допустимых расширений

if is_valid_extension(filename, allowed_extensions):
    print("Расширение файла допустимо.")
else:
    print("Недопустимое расширение файла.")
