# -*- coding:utf-8 -*-
# file: pysmtp.py
#

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import os
import datetime
import shutil

#----------------------------------------------------------------------
def sendEmail_attach(subject, fullpath):
    try:                                        # 例外處理
        sender = 'robert.lo@amtran.com.tw'
        recipients = ['atttrobert@gmail.com']
        emaillist = [elem.strip().split(',') for elem in recipients]
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['Reply-to'] = sender
        user = str('ee3amt@gmail.com').strip()                     # 取得使用者名稱
        pw = str('fw_oem13').strip()                       # 取得密碼

        msg.preamble = 'Multipart massage.\n'

        part = MIMEText("Hi  \n\n The attached file is EDID table in file from HDMI DDC \n\n Thanks!")
        msg.attach(part)

        part = MIMEApplication(open(fullpath,"rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(fullpath))
        msg.attach(part)


        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(user, pw)

        server.sendmail(msg['From'], emaillist , msg.as_string())
        server.quit()                             # 中斷伺服器
        print "Email sending ok !!"

    except :
        print "Email sending error !!"

#----------------------------------------------------------------------
if __name__ == "__main__":

    reload(sys)
    sys.setdefaultencoding('utf-8')

    subject = "HDMI I2C EDID table"
    fullpath = "/home/pi/edid.bin"

    if not os.path.isfile(fullpath):
        print "%s doesn't exist" %(fullpath)
        sys.exit()

    sendEmail_attach(subject, fullpath)
