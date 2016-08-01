"""
    A module to make sentences.

    Originally by Zed A. Shaw
    Modified by Mohammad Shantanu Rahman
"""

class ParserError(Exception):
    """ Do nothing really, just yell """
    pass

def peek(word_list):
    """ Get the first word """
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    """ See if the next word matches and return it"""
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    """ Skip word of certain types """
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    """ Parse verb of a sentence """
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    """ Parse the object of a sentence """
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    """ We need some subjects """
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'computer') # imperative the thing we want.
    else:
        raise ParserError("Expected a verb next")

def parse_sentence(word_list):
    """ Parse each sentence to make a Sentence ie object """
    sub = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return {"subject" : sub, "verb" : verb, "object": obj}
