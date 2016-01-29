"""
    The main entry point
"""

import time
from imaplib import IMAP4_SSL

import utils

def get_recent_mails(server, client_name):
    """ Gets the recent mails from client"""
    res = server.search(None, '(UNSEEN) (SUBJECT POWER) (FROM "' + client_name + '")')[1]
    ids = res[0].decode().split(' ')
    return ids

def main():
    """ The entry point """

    client = input("client name : ")

    server = IMAP4_SSL('imap.gmail.com')
    usr, pass_ = utils.get_credentials('./credentials/server.txt')
    stat = server.login(usr, pass_)[0]
    if stat == 'OK':
        print("Listening for mails......")
        try:
            while True:
                server.select('Inbox') # select the inbox
                mails = get_recent_mails(server, client)
                if mails != ['']:
                    for mail in mails:
                        print(server.fetch(mail.encode(), '(UID BODY[TEXT])'))
                time.sleep(5)
        except KeyboardInterrupt:
            print("Done Listening...")

        server.close()
        server.logout()
    else:
        pass
    return

if __name__ == '__main__':
    main()
