#!/usr/bin/env python

import itertools
from itertools import product, permutations
import pandas as pd

word_results = []

def permutations_result(chars):
   result = [''.join(element) for element in  list(permutations(chars))]
   return result


#file = open('words.txt', 'w')
test_word = "ball"
max_length = (len(test_word) + 1)
possible_words = []

word_characters = ""
for letter in test_word:
    word_characters = word_characters + letter
    if(len(word_characters) > 1):
        words = permutations_result(word_characters)

        possible_words.extend(words)

print(possible_words)
# for thing in possible_words:
#     print(thing)

# for word in distinct_list:
#     file.write('\n'.join(word))

