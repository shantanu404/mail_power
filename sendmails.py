"""
    A helping string that sends emails.
"""

import smtplib
from utils import get_credentials

MSG = input("msg> ")
M = smtplib.SMTP('smtp.gmail.com', 587)
USR, PASS_ = get_credentials('./usr_credentials/client.txt')

M.starttls()
M.login(USR, PASS_)
M.sendmail(USR, get_credentials("./credentials/server.txt")[0],
           'Subject:POWER\r\n%s\n' %(MSG))

M.quit()
