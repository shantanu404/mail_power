from utils.get_credential import *
from imaplib import IMAP4_SSL
import time

global client

client = get('./credentials/login2.txt')[0]

def get_recent_mails(M, client):
    rc, res = M.search(None, '(UNSEEN) (SUBJECT POWER) (FROM "' + client + '")')
    ids = res[0].decode().split(' ')
    return ids

def main():
    M = IMAP4_SSL('imap.gmail.com')
    usr, pass_ = get('./credentials/login.txt')
    rc, data = M.login(usr, pass_)
    if (rc == 'OK'):
        try:
            while True:
                M.select('Inbox') # select the inbox
                mails = get_recent_mails(M, client)
                if mails != ['']:
                    for mail in mails:
                        print(M.fetch(mail.encode(), '(UID BODY[TEXT])'))
                time.sleep(5)
        except KeyboardInterrupt as e:
            pass

        M.close()
        M.logout()
    else:
        pass
    return

if __name__ == '__main__':
    main()
