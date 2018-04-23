import numpy as np
import ast
import argparse
import sys
import random
import pickle
parser = argparse.ArgumentParser(description='Ganerate sequence of words, based on model, which created by train.txt')

parser.add_argument('--model','-m', type=argparse.FileType('rb'), default=open('model.pickle', 'rb'), help='Way to file for reading model')

parser.add_argument('--seed', '-s', default=None, help='The first word of the sequence. (default: random word')

parser.add_argument('--length', '-l', type=int, help='Length of the sequence. (default: random(max = 100))', default=None)

parser.add_argument('--output', '-o', help='Way to write the sequence', default=sys.stdout)
args = parser.parse_args()


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


def main():
    #импорт библиотеки
	Lib = pickle.load(args.model)
	#ввод первого слова
	word = args.seed
	if not(word): word = random.choice(list(Lib.keys()))
	# ввод количества последующих слов
	size = args.length
	if not(size): size = random.randint(1, 100)
	# вывод последовательности
	args.output.write(word + ' ')
	for i in range(size):
		word = next_word(word, Lib)
		args.output.write(word + ' ')
	args.output.write('\n')
    
    
if __name__ == '__main__':
    main()
