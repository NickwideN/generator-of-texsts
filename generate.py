import numpy as np

def next_word(word_1, Lib):
	#создаем массив из возможных слов-2
	words_2 = []
	words_2_truffic = [] #количество встреч соответствующей пары
	line_model = 'string'
	for row in Lib:
	    if row:
    		if row[0] == word_1:
    			words_2.append(row[1])
    			words_2_truffic.append(int(row[2]))
	sum_traffic = sum(words_2_truffic)
	for i in range(len(words_2_truffic)):
		words_2_truffic[i] /= sum_traffic

	#создали массивы
	if words_2:
		new_word = np.random.choice(words_2, 1, p=words_2_truffic)[0]
	else:
		print("\nI don't know what '", word_1, "' mean", sep='')
		exit(1)
	return new_word


if __name__ == '__main__':
    #импорт библиотеки
	model = open('model.txt', 'r', encoding='utf-8')
	Lib = model.read().split('\n')
	for i in range(len(Lib)):
	    Lib[i] = Lib[i].split()
	#ввод первого слова
	print('input the first word')
	word = input()
	# ввод количества последующих слов
	print('input number of next words')
	size = int(input())
	#вывод последовательности
	print(word, end=' ')
	for i in range(size):
		word = next_word(word, Lib)
		print(word, end=' ')
	print('\n')
	model.close()
