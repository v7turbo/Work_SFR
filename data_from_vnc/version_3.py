import os

dirname = "D:\\vnc"            
files = os.listdir(dirname)

target_list = [] 					       	
for filename in files:					       	
    with open(os.path.join(dirname, filename), 'r') as f:      
        text = f.readlines()				        
        text1 = text[1]
        without_space = text1[5:19]			                             # срез до ip адреса
        target_list.append({'fio': filename[:-4], 'ip': without_space})  #

with open('ip.txt', 'w') as list1:
    for line in target_list:
        list1.write(line['fio'] + ' -------------- ' + line['ip'])
list1.close()