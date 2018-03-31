import re
if __name__ == '__main__':
    train_text = open('text.txt', 'r', encoding="utf-8")
    last_word = ''  #содержит последнее слово предыдущей строчки
    Lib = {}        #библиотека пар слов
    for line in train_text:
        # вставим в начало строчки последнее слово предыдущей строчки
        line = last_word + ' ' + line 
        # приведем все символы к lowercase
        line = line.lower()
        # оставим только алфавитные символы
        line = re.sub("[^a-zа-я' ]", '', line)
        # разделение строки по словам
        line_list = line.split()
        #зафиксируем последнее слово строчки
        if line_list:
            last_word = line_list[-1]
        #ввод пар строк в библиотеку
        for i in range(len(line_list) - 1):
            if line_list[i] in Lib:
                if line_list[i + 1] in Lib[line_list[i]]:
                    Lib[line_list[i]][line_list[i + 1]] += 1
                else:
                    Lib[line_list[i]][line_list[i + 1]] = 1
            else:
                Lib[line_list[i]] = {line_list[i + 1]: 1}
    
    #вывод быблиотеки в файл model.txt
    model = open('model.txt', 'w')
    model.write(str(Lib))
    model.close()
     
    train_text.close()
    print('ok')
