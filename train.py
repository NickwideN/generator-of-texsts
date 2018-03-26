import re

#очистим файл model.txt
model = open('model.txt', 'w')  
model.close()

#ну, приступим
train_text = open('text.txt', 'r', encoding="utf-8")
#объявление переменной, содержащая последнее слово предыдущей строчки
last_word = ''
for line in train_text:
    # вставим в начало строчки последнее слово предыдущей
    # строчки
    line = last_word + ' ' + line 
    # приведем все символы к lowercase
    line = line.lower()
    # оставим только алфавитные символы
    line = re.sub('[^a-zа-я ']', '', line)
    #line = OnlyAlpha(line)
   
    # разделение строки по словам
    line_list = line.split()
    if line_list:
        last_word = line_list[-1]
    
    
    #работа с парами слов
    for i in range(len(line_list) - 1):
        new_pair = line_list[i] + '\t' +  line_list[i + 1]
        #print('\n\nnext pair: ', new_pair)
        model = open('model.txt', 'r+')
        model_line = ' '
        is_new_pair_was = False
        while model_line:
            model_line = model.readline()
            #print('курсор на: ', model.tell(), ' ', model_line)
            pair_model = model_line[:model_line.find(' ')]
            #print('pair_model', pair_model)
            if pair_model == new_pair:
                model.seek(model.tell() - 2)
                number = str(int(model.read(1)) + 1)
                model.seek(model.tell() - 1)
                model.write(number)
                is_new_pair_was = True
                #print('!!break курсор: ', model.tell()) 
                #print(pair_model, '==', new_pair)
                break
        if (not(is_new_pair_was)):    
            model.write(new_pair + ' ' + '1' + '\n')
        model.close()
    #print(line_list)
    
    
print('ok')
train_text.close()





