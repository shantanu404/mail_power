"""
    All arduino serial communication is going on here.
"""

import json
import pyfirmata

from syntax.lexicon import scan
from syntax.parser import parse_sentence, ParserError

mappingfile = open("mapping.json")
config_data = json.loads(mappingfile.read())
mappingfile.close()

MAPPING = config_data["items"]
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

    return lines

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

        if sentence["subject"][1] == "computer":
            action = (sentence["verb"][1] == "turn_on")
            item = (sentence["object"][1])
            items = [x[0] for x in MAPPING.items()]
            found = item in items
            if not found:
                print(item)
            else:
                item = MAPPING[item]

            print(item, action)
            BOARD.digital[item].write(action)

    return
