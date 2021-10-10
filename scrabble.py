#!/usr/bin/env python

from itertools import product, permutations
import json
import datetime
import requests
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)

        # place button at (0,0)
        exitButton.place(x=0, y=0)

    def clickExitButton(self):
        exit()

word_results = []

def permutations_result(chars):
    result = [''.join(element) for element in  list(permutations(chars))]
    return result

def api_request(api_key, potential_word):
    word_date = ""

    api_url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key={}".format(potential_word, api_key)
    response = requests.get(api_url)

    result = response.json()
    if len(result) > 0:
        number_1 = result[0]
        result_test = isinstance(number_1, str)
        if(result_test != True):
            if("date" in number_1):
                word_date = number_1['date']
            short_def = number_1['shortdef']
            print("{}: {} - {}.\n".format(potential_word, word_date, short_def))
    
def Get_potential_words(theWord):
    possible_words = []
    word_characters = ""
    for letter in theWord:
        word_characters = word_characters + letter
        if(len(word_characters) > 1):
            words = permutations_result(word_characters)
            possible_words.extend(words)
    
    return possible_words

def main():
    #file = open('words.txt', 'w')
    input_word = input()
    max_length = (len(input_word) + 1)
    real_words = []
    words_today = 0

    today = datetime.datetime.now()

    with open("/home/lyleolsen/projects/totally_random/scrabble_points/stats.json", "r") as stats:
        statsfile = json.load(stats)

    api_key = statsfile["API_KEY"]
    words_processed = statsfile["words_processed"]
    date_last_processed = statsfile["last_run_date"]

    format = '%m/%d/%Y'
    last_run_date = datetime.datetime.strptime(date_last_processed, format)

    difference = today-last_run_date
    day_difference = difference.days

    if(day_difference > 0):
        words_processed = 0


    possible_words = Get_potential_words(input_word)


    for the_word in possible_words:
        if words_processed < 995:
            api_request(api_key, the_word)
            words_processed += 1


    statsfile["words_processed"] = words_processed
    updated_date = datetime.datetime.now().strftime('%m/%d/%Y')
    statsfile["last_run_date"] = updated_date
    updated_data = json.dumps(statsfile)

    with open("/home/lyleolsen/projects/totally_random/scrabble_points/stats.json", "w") as outfile:
        outfile.write(updated_data)

# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("Tkinter window")

# show window
root.mainloop()

#main()
