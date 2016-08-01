#!/usr/bin/env python3

"""Clean up mails"""

import imaplib
from utils import get_credentials as get

def main():
    """ Entry point """
    usr, pass_ = get("./credentials/server.txt")
    server = imaplib.IMAP4_SSL('imap.gmail.com')
    server.login(usr, pass_)
    server.select()
    stat, res = server.search(None,\
    "(SUBJECT POWER) (SEEN)")
    mails = res[0].decode().split(" ")
    if stat == 'OK' and mails != ['']:
        print(mails)
        for num in res[0].decode().split(" "):
            stat, data = server.store(num.encode(), '+FLAGS', '\\Deleted')
            print(stat, data)
        server.expunge()
    else:
        print("No mails found!")

if __name__ == '__main__':
    main()
