import os

dirname = "D:\\vnc"            
files = os.listdir(dirname)

with open('fio.txt', 'w') as list:
    for i in files:
        i = i[:-4] + '\n'
        list.write(i)
list.close()

target_list = []
for filename in files:
    with open(os.path.join(dirname, filename), 'r') as f:
        text = f.readlines()
        text1 = text[1]
        cut = text1[5:19]
        target_list.append(cut)

with open('ip.txt', 'w') as list1:
    for line in target_list:
        list1.write(line)
list1.close()