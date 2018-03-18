def OnlyAlpha(s):
    Symbols_not_removed = " '"
    i = 0
    while i < len(s):
        if not(s[i].isalpha() or s[i] in Symbols_not_removed):
            if i == len(s):
                s = s[:i]
                i -= 1
            else:
                s = s[:i] + s[i + 1:]
                i -= 1
        i += 1
    return s
    
def OnlyLowercase(s):
    s = ' ' + s
    for i in range(len(s)):
        if s[i].isupper():
            if ((s[i] == 'I') and (s[i - 1] == ' ' and s[i + 1] == ' ')):
                continue
            s = s[:i] + s[i].lower() + s[i + 1:]
    return s
#очистим файл model.txt
model = open('model.txt', 'w')  
model.close()

#ну, приступим
train_text = open('test.txt', 'r')
last_word = ''
for line in train_text:
    line = last_word + ' ' + line
    line = OnlyAlpha(line)
    line = OnlyLowercase(line)
    line_list = line.split()
    last_word = line_list[-1]
    
    
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



























