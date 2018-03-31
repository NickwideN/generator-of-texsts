import numpy as np
import ast
def next_word(word_1, Lib):
    if word_1 in Lib:
        words_2_dict = Lib[word_1]
        words_2 = list(words_2_dict.keys())
        words_2_traffic = list(words_2_dict.values()) #количество встреч соответствующей пары
        sum_traffic = sum(words_2_dict.values())
        for i in range(len(words_2_traffic)):
            words_2_traffic[i] /= sum_traffic
        new_word = np.random.choice(words_2, 1, p=words_2_traffic)[0]
    else:
        print("\nI don't know what '", word_1, "' mean", sep='')
        exit(1)
    return new_word


if __name__ == '__main__':
    #импорт библиотеки
	model = open('model.txt', 'r', encoding='utf-8')
	Lib = ast.literal_eval(model.read())
	#ввод первого слова
	print('input the first word')
	word = input()
	# ввод количества последующих слов
	print('input number of next words')
	size = int(input())
	# вывод последовательности
	print(word, end=' ')
	for i in range(size):
		word = next_word(word, Lib)
		print(word, end=' ')
	print('\n')
	model.close()
