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
        pw = str('fw_oem12').strip()                       # 取得密碼

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

    if len(sys.argv) < 3:
        # print 'no argument; Usage: SendMail_attach.py TITLE FILE'
        # sys.exit()
        print "Default Title and Path:"
        subject = "FW5 Weekly Report"
        fullpath = "/Volumes/robert.lo/Data/DOC/Weekly Report/FW5-report-wk%d.docx" %(datetime.datetime.now().isocalendar()[1]+1)
        fullpath_next = "/Volumes/robert.lo/Data/DOC/Weekly Report/FW5-report-wk%d.docx" %(datetime.datetime.now().isocalendar()[1]+2)
        # fullpath = "/Volumes/Jet_drive/FW5-report-wk40.docx"
    else:
        subject = str(sys.argv[1])
        fullpath = str(sys.argv[2])

    print "Title = %s" %(subject)
    print "Full path = %s" %(fullpath)
    print "The current Week Number is : W%d" %(datetime.datetime.now().isocalendar()[1])

    if os.path.isfile(fullpath_next):
        print "%s exist so the report was sent before!!" %(fullpath_next)
        sys.exit()

    fullpath = ~/edid.bin

    if not os.path.isfile(fullpath):
        print "%s doesn't exist" %(fullpath)
        sys.exit()

    sendEmail_attach(subject, fullpath)
