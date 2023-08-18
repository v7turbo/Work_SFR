#!/bin/bash

#search_by_uid

read -p "Введите имя файла: " find_var       # присваиваем значение переменной find_var (имя файла МОЖЕТ быть не полным и содержать пробелы)
sudo smbstatus -L | grep -i "${find_var}"    # поиск по значению find_var
read -p "Введите UID: " find_uid             # присваиваем значение переменной find_uid
poisk_name=$(id $find_uid)                   # новая переменная
echo                                         # пустая строка
echo ${poisk_name%%gid=*}                    # вывод переменной poisk_name, до значения gid=