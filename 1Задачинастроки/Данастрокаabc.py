def modify_string(s):
    if s.startswith('abc'):
        # Если строка начинается на 'abc', заменяем их на 'www'
        s = 'www' + s[3:]
    else:
        # Иначе добавляем 'zzz' в конец строки
        s = s + 'zzz'
    return s

# Пример использования
try:
    input_string = input("Введите строку: ")
    output_string = modify_string(input_string)
    print("Результат:", output_string)

except Exception as e:
    print("Произошла ошибка:", e)
