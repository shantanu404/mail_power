"""
    A helping string that sends emails.
"""

import smtplib
from utils import get_credentials

COUNT = int(input("count: "))
M = smtplib.SMTP('smtp.gmail.com', 587)
USR, PASS_ = get_credentials('./usr_credentials/client.txt')

M.starttls()
M.login(USR, PASS_)
for i in range(COUNT):
    M.sendmail(USR, get_credentials("./credentials/server.txt")[0],
               'Subject:POWER\r\nLIGHT' + str(i+1) + ' ON\n')

M.quit()
