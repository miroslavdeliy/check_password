#Функция ввода пароля
def input_password():
    passw = input("Введите пароль: ")
    return passw


#Функция проверки пароля
def check_password(pas):
    if pas == password:
        return False
    else:
        return True


#Основное тело программы
password = "password"
while check_password(input_password()):
    print("Ошибка! Неверный пароль!")
    print("Введите пароль еще раз!")
print("Совершен вход в систему!")