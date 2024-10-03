import hashlib
import random
import string


# Функция для генерации случайного пароля
import random
import string

# Функция для генерации пароля, состоящего только из букв и цифр
def generate_password(length=8):
    all_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password



# Функция для проверки, соответствует ли пароль требованиям безопасности
def is_secure_password(password):
    if len(password) < 6:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    return has_upper and has_lower and has_digit and has_special


# Функция для шифрования пароля с помощью SHA-256
def hash_password(password):
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature


# Основная функция
def process_password():
    choice = input("Вы хотите сгенерировать пароль (1) или ввести свой (2)? Введите 1 или 2: ")

    if choice == '1':
        password = generate_password()
        print(f"Ваш сгенерированный пароль: {password}")

    elif choice == '2':
        password = input("Введите ваш пароль: ")
        while len(password) < 6:
            print("Пароль должен содержать не менее 6 символов.")
            password = input("Введите другой пароль: ")

        if is_secure_password(password):
            hashed_password = hash_password(password)
            print(f"Ваш зашифрованный пароль (SHA-256): {hashed_password}")
        else:
            print("Пароль не соответствует требованиям безопасности. Пароль не был зашифрован.")
    else:
        print("Неверный выбор!")


# Вызов функции
process_password()
