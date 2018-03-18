import numpy as np
def next_word(word_1):
    model = open('model.txt', 'r')
    #создаем массив из возможных слов-2
    words_2 = []
    words_2_truffic = []
    line_model = 'string'
    while line_model and line_model not in '  ':
        line_model = model.readline()
        if not(line_model): break
        line_model_arr = line_model.split()
        if line_model_arr[0] == word_1:
            words_2.append(line_model_arr[1])
            words_2_truffic.append(int(line_model_arr[2]))
    sum_traffic = sum(words_2_truffic)
    for i in range(len(words_2_truffic)):
        words_2_truffic[i] /= sum_traffic
        
    #print('words_2', words_2)
    #print('words_2_truffic', words_2_truffic)
    #print(sum(words_2_truffic))
    #создали массивы
    if words_2:
        new_word = np.random.choice(words_2, 1, p=words_2_truffic)[0]
    else:
        print("\nI don't know what '", word_1,"' mean", sep = '')
        exit(1)
    
    model.close()
    return new_word

print('input the first word')
word = input()
print('input number of next words')
size = int(input())
print(word, end = ' ')
for i in range(size):
    word = next_word(word)
    print(word, end = ' ') 
print('\n')

