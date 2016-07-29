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

def parse_n_send_command(msg_body):
    """ Parse the command and send to arduino."""
    words = scan((msg_body).lower())
    sentence = {"subject" : None, "verb" : None, "object": None} # set it as a local variable
    try:
        sentence = parse_sentence(words)
    except ParserError as error:
        print(error)

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
