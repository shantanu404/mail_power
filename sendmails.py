from utils.get_credential import *
import smtplib

count = int(input("count: "))
M = smtplib.SMTP('smtp.gmail.com', 587)
usr, pass_ = get('./credentials/login2.txt')
M.starttls()
M.login(usr, pass_)
for i in range(count):
    M.sendmail(usr, get("./credentials/login.txt")[0], 'Subject:POWER\r\nLIGHT' + str(i+1) + ' ON\n')

M.quit()
