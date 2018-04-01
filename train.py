import re
import argparse
import sys
import os
import ast
parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', default=None, dest='input_dir', help='Way to collection of train_files, only .txt files exept model')

parser.add_argument('--model', type=argparse.FileType('w'), default=open('model.txt', 'w'), help='Way to file for saving model')

parser.add_argument('--lc', action='store_true', help='To produce lowacase train files')
args = parser.parse_args()

def get_Lib(train_text, Lib):
    last_word = ''  #содержит последнее слово предыдущей строчки
    for line in train_text:
        # вставим в начало строчки последнее слово предыдущей строчки
        line = last_word + ' ' + line 
        # приведем все символы к lowercase
        if (args.lc):
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
    return Lib
    
def main():
    if args.input_dir:
        Lib = {}       #библиотека пар слов
        pattern = re.compile(r'.*\.txt')
        exept_pattern = re.compile(args.model.name)
        train_list = [_file for _file in os.listdir(args.input_dir) if pattern.match(_file) and not(exept_pattern.match(_file))]
        print(train_list)
        for _file in train_list:
            train_text = open(args.input_dir + _file, 'r', encoding="utf-8")
            Lib = get_Lib(train_text, Lib)
            train_text.close()
        args.model.write(str(Lib))
        print('ok')
    
    
if __name__ == '__main__':
    main()
