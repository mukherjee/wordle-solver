from collections import Counter
import string
import sys
inputs = sys.argv[1].split()
inp_dict = {}
for index in range(0, len(inputs), 2):
    inp_dict[inputs[index]] = inputs[index + 1]
fn = "5-letter-words.txt"
with open(fn) as file:
    words1 = file.readlines()
    words1 = [word.rstrip() for word in words1]
#print(len(words1))

# Iterate through every word and return a new list satisfying green criteria
def green(words, letter, index):
    new_list = []
    for word in words:
        if word[index] == letter:
            new_list.append(word)
    return(new_list)

def yellow(words, letter, index):
    new_list = []
    for word in words:
        if (letter in word) and (word[index] != letter):
            new_list.append(word)
    return(new_list)

def black(words, letter, index):
    new_list = []
    for word in words:
        if letter not in word:
            new_list.append(word)
    return(new_list)

def yellow_fix(words, letters):
    new_list = []
    for word in words:
        if(len(set(letters) & set(word)) == len(letters)):
            new_list.append(word)
            #print(word)
    return(new_list)

def get_suggestions(words):
    joined = ''.join(words)
    counted = Counter(joined)
    suggested_dict = {}
    for word in words:
        sum = 0
        for letter in word:
            res = Counter(word)
            sum = sum + int(counted[letter]/res[letter])
        suggested_dict[word] = sum
    sorted_dict = {k: v for k, v in sorted(suggested_dict.items(), key=lambda item: item[1], reverse=True)}
    print(f'\nRecommended next word: {list(sorted_dict)[0]}')
    if len(list(sorted_dict)) > 1:
        print(f'Backup word: {list(sorted_dict)[1:2]}\n')
    return sorted_dict

def update_word_list(words, guess, result):
    dispatch = {'G': green, 'Y': yellow, 'B': black}
    new_list = words[:]
    for index, letter in enumerate(guess):
        new_list = dispatch[result[index]](new_list[:], letter, index)
    
    # All yellows must appear in the solution at the same time
    y_list = [guess[i] for i, color in enumerate(result) if color == 'Y']
    new_list = yellow_fix(new_list, y_list)
    return new_list

##### Main work starts here
words = words1.copy()
for guess, result in inp_dict.items():
    words = update_word_list(words[:], guess, result)
get_suggestions(words)
