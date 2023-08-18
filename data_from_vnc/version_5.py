import os
from prettytable import PrettyTable

dirname = 'D:\\vnc'
files = os.listdir(dirname)
x = PrettyTable()                                      # создать пустую таблицу
x.field_names = ["fio", "ip"]                          # задать имена полей
                                                       # кол-во полей = кол-ву столбцов
for filename in files:
    with open(os.path.join(dirname, filename), 'r') as f:
        text = f.readlines()
        text1 = text[1]
        without_space = text1[5:19]		               # срез до ip адреса
        x.add_row([filename[:-4]] + [without_space])   # добавить строки в таблицу
d = open("ip.txt", 'w')
d.write(str(x))
