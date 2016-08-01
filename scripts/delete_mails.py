#!/usr/bin/env python3

"""Clean up mails"""

import imaplib

# TODO: Think DRY :)
def get(filepath):
    """Gets the user credentials from a file"""
    with open(filepath) as credentials:
        content = credentials.read()
        info = content.split('|')
        return ((info[0]).strip('\r\n'), (info[1]).strip('\r\n'))

def main():
    """ Entry point """
    usr, pass_ = get("data/credentials.dat")
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
