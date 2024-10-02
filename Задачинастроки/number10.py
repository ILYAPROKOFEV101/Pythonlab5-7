import random
import string


def generate_password(user_input=None, length=12):
    # Проверяем, что длина не меньше 6 символов
    if length < 6:
        raise ValueError("Длина пароля должна быть не менее 6 символов")

    # Определяем набор символов для генерации пароля
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()-_+="

    # Объединяем все символы для рандомной генерации
    all_chars = lowercase + uppercase + digits + special_chars

    # Генерируем базовый рандомный пароль, состоящий из обязательных частей
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]


# Пример использования
try:
    user_input = input("Введите часть пароля (если хотите добавить свои символы) или оставьте пустым: ")
    length = int(input("Введите длину пароля (минимум 6): "))

    generated_password = generate_password(user_input=user_input, length=length)
    print("Сгенерированный пароль:", generated_password)

except ValueError as e:
    print(e)
