import sqlite3
from login_player import *


def add_text(user):
    base = sqlite3.connect(user + '.db')
    cur = base.cursor()
    r = cur.execute('SELECT * FROM akk').fetchall()     # считываем все данные с файла sqlite
    my_file = open("my_akk_data.txt", "w+")
    total = 0
    for row in r:   # отображение данных в меню
        my_file.write("Имя аккаунта: " + row[0] + "\n")
        my_file.write("Логин: " + row[1] + "\n")
        my_file.write("Пароль: " + row[2] + "\n")
        my_file.write("_______________\n")
        total += 1
    my_file.write("Всего аккаунтов: " + str(total))
    my_file.close()
    print("Данные успешно выведены!")