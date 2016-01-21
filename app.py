from utils.get_credential import *
from imaplib import IMAP4_SSL

def main():
    M = IMAP4_SSL('imap.gmail.com')
    usr, pass_ = get('./credentials/login.txt')
    rc, data = M.login(usr, pass_)
    print( data )
    M.logout()
    return

if __name__ == '__main__':
    main()
