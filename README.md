# generator-of-texsts
train.py 
-----------------------------------------
Создает библиотеку (по-умолчанию model.txt в текущей директории), на основе всех файлов, которые есть в указанной директории (--input-dir) с расширением .txt, кроме файла с названием 'model.txt'.

Parser   |  Description
----------|------------------
--input-dir    | путь к директории, в которой лежит коллекция документов. По умолчанию текст считывается из stdin. В этом случае для завершения ввода текста необходимо 2 раза нажать "Enter"
--model         | путь к файлу, в который сохраняется модель (по-умолчанию model.txt в текущей директории).
--lc            | Приводить тексты к lowercase.
--help 

generate.py 
-------------------------------------------------------
Выводит последовательность слов, основываясь на указанной библиотеке (по-умолчанию model.txt в текущей директории)

Parser   |  Description
----------|------------------
--model | путь к файлу, из которого загружается модель(по-умолчанию model.txt в текущей директории)
--seed | Начальное слово (по-умолчанию случайное слово).
--length | длина генерируемой последовательности (по-умолчанию случайное число от 1 до 100)
--output | Файл, в который будет записан результат (по умолчанию stdout)
--help 

