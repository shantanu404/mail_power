"""
    A dictionary to parse words.

    Originally by Zed A. Shaw
    Modified by Mohammad Shantanu Rahman
"""

WORDS = {
    'verb' : ['turn_on', 'turn_off'],
    'noun' : ['light1', 'light2', 'light3', 'fan', 'lights'], #TODO: get this data from mapping.json
    'stop' : ['the', 'in', 'of', 'to']
}

def scan_word(word):
    """ See what a word is """
    for (type_, data) in WORDS.items():
        for single_word in data:
            if word == single_word:
                return (type_, word)

    return ('error', word)

def scan(line):
    """ Scan a sentence or line and parse every words """
    res = []
    for word in line.split(" "):
        try:
            res.append(('number', int(word)))
        except ValueError:
            res.append(scan_word(word))
    return res
