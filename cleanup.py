import imaplib
from utils.get_credential import *

usr, pass_ = get("./credentials/login.txt")
M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login(usr, pass_)
M.select()
rc , res = M.search(None, "(SUBJECT POWER) (FROM '" + (get('./credentials/login2.txt')[0]) + "') (SEEN)")
mails = res[0].decode().split(" ")
if rc == 'OK' and mails != ['']:
    print(mails)
    for num in res[0].decode().split(" "):
        rc, data = M.store(num.encode(), '+FLAGS', '\\Deleted')
        print(rc, data)
    M.expunge()
else:
    print("No mails found!")
