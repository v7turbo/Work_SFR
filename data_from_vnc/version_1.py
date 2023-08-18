import os

dirname = "D:\\vnc"
files = os.listdir(dirname)

with open('fio.txt', 'w') as list:
    for i in files:
        i = i[:-4] + '\n'
        list.write(i)

for filename in files:
    with open(os.path.join(dirname, filename), 'r') as f:
        text = f.readlines()
        text1 = text[1]
        cut = text1[5:19]
        no_space = cut.strip()
        with open('ip.txt', 'a') as list1:
            for no_space in cut:
                list1.write(no_space)