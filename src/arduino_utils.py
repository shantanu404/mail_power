"""
    All arduino serial communication is going on here.
"""

import json
import pyfirmata

from syntax.lexicon import scan
from syntax.parser import parse_sentence, ParserError

mappingfile = open("data/mapping.json")
config_data = json.loads(mappingfile.read())
mappingfile.close()

MAPPING = config_data["items"]
GROUPS = config_data["groups"]
PORT = input("port> ")
BOARD = pyfirmata.Arduino(PORT);

def parse_gmail(msg_body):
    """ Parse the msg body from html to plain """
    if "Content-Type" in msg_body:
        lines = msg_body.split('\n');
        lines = [x.strip('\r\n') for x in lines if x != "" and x[:2] != "--"]
        x = ""
        while "Content-Type" not in x:
            x = lines.pop()
        lines.reverse()
        x = ""
        while "Content-Type" not in x:
            x = lines.pop()
    else:
        lines = msg_body.split('\n');

    lines.reverse()

    return lines

def get_items_actions(sentence):
    """
    Get the items and action for that from the sentence.
    returns a list of tuples
    """
    if sentence["subject"][1] == "computer":
        action = (sentence["verb"][1] == "turn_on")

        for item, pin in MAPPING.items():
            if item == (sentence["object"][1]):
                return [(pin, action)]

        for group, items in GROUPS.items():
            if group == (sentence["object"][1]):
                vals = []
                for item in items:
                    vals.append((MAPPING[item], action))
                return vals

    return [ (None, None) ]


def parse_n_send_command(msg_body):
    """ Parse the command and send to arduino."""
    msgs = parse_gmail(msg_body);
    for msg in msgs:
        if len(msg) == 0:
            continue
        words = scan(msg.lower().strip('\r\n'))
        print(words)
        sentence = {"subject" : None, "verb" : None, "object": None} # set it as a local variable
        try:
            sentence = parse_sentence(words)
        except ParserError as error:
            print(error)
            continue

        for item_id, action in get_items_actions(sentence):
            print(item_id, action)
            BOARD.digital[item_id].write(action)
