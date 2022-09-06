'''
ДЗ 9:
Напишите функцию, которая будет генерировать случайный пароль. В пароле должно быть от 7 до 10 символов, при этом каждый символ должен
быть случайным образом выбран из диапазона от 33 до 126 в таблице
ASCII. Ваша функция не должна принимать на вход параметры, а возвращать будет сгенерированный пароль. В основной программе вы должны
просто вывести созданный случайным образом пароль. Программа должна запускаться только в том случае, если она не импортирована в виде
модуля в другой файл.

ДОП:
Добавте файлы ДЗ в github репозиторий, и отправьте мне ссылку

'''
import random

def password():
    newlist = []
    for i in range(33,127):
        newlist.append(chr(i))

    password = ''

    for n in range(10):
        password += random.choice(newlist)

    return password

newpassword = password()

print('Случайно сгенерированный пароль: ', newpassword)



