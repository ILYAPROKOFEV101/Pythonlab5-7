def modify_string(s):
    if s.startswith('abc'):
        # Если строка начинается на 'abc', заменяем их на 'www'
        s = 'www' + s[3:]
    else:
        # Иначе добавляем 'zzz' в конец строки
        s = s + 'zzz'
    return s

# Пример использования
input_string = input("Введите строку: ")
output_string = modify_string(input_string)
print(output_string)
