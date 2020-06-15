import json
from difflib import get_close_matches

data = json.load(open("json.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mead %s instead " % get_close_matches(word, data.keys())[0])
        decide = input("Press 'y' for yes and 'n' for no\n")
        if decide == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == 'n':
            return "You steps on a wrong keys"
        else:
            return "You Entered a wrong word"
    else:
        print("You steps on a wrong keys")


Answer = 'y'
while Answer == 'y':
    w = input("Type a word to translate\n")
    output = translate(w)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    Answer = input("Do you Want to Translate another word\n")





