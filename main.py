#Функция ввода пароля
def enter_password():
    password_input = input("Введите пароль: ")
    return password_input


#Функция проверки пароля
def check_password(password_check):
    if password_check == password:
        return False
    else:
        return True


#Основное тело программы
password = "password"
while check_password(enter_password()):
    print("Ошибка! Неверный пароль!")
print("Совершен вход в систему!")