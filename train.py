import re

train_text = open('text.txt', 'r', encoding="utf-8")
last_word = ''  #содержит последнее слово предыдущей строчки
Lib = []        #библиотека пар слов
for line in train_text:
    # вставим в начало строчки последнее слово предыдущей строчки
    line = last_word + ' ' + line 
    # приведем все символы к lowercase
    line = line.lower()
    # оставим только алфавитные символы
    line = re.sub('[^a-zа-я ]', '', line)
    # разделение строки по словам
    line_list = line.split()
    #зафиксируем последнее слово строчки
    if line_list:
        last_word = line_list[-1]
    #ввод пар строк в библиотеку
    for i in range(len(line_list) - 1):
        new_pair = line_list[i] + '\t' +  line_list[i + 1]
        new_pair_is_in_Lib = False
        for row in Lib:
            if row[0] == new_pair:
                row[1] += 1 
                new_pair_is_in_Lib = True
                break
        if new_pair_is_in_Lib == False:
            Lib.append([new_pair, 1])
#вывод быблиотеки в файл model.txt
model = open('model.txt', 'w')
for row in Lib:
    model.write(row[0] + ' ' + str(row[1]) + '\n')
model.close()
 
train_text.close()
print('ok')





