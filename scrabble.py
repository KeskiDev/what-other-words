#!/usr/bin/env python

import itertools
from itertools import product, permutations
import pandas as pd

word_results = []

def permutations_result(chars):
   result = [''.join(element) for element in  list(permutations(chars))]
   return result


#file = open('words.txt', 'w')
test_word = "test"
max_length = (len(test_word) + 1)


words = permutations_result(test_word)
print(words)


# for word in distinct_list:
#     file.write('\n'.join(word))

