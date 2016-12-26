# -*- coding:utf-8 -*-
# file: pysmtp.py
#
import smtplib
import sys

def sendEmail(VER):                                      # 按鈕事件
    try:                                        # 例外處理
        host = 'smtp.gmail.com'                      # 取得伺服器位址
        port = 587            # 取得通訊埠
        user = str('ee3amt@gmail.com').strip()                     # 取得使用者名稱
        pw = str('xxx').strip()                       # 取得密碼
        fromaddr = 'ee3amt@gmail.com'                     # 取得發件人
        toaddr = 'atttrobert@gmail.com'                     # 取得收件人
        subject = 'Email sending Test'                      # 取得主旨
        text = 'This is an email from Robert ' + VER + ' is available now'                 # 取得信件內容
        msg = ("From: %s\nTo: %s\nSubject: %s\n\n"              # 產生信件頭
            % (fromaddr, toaddr, subject))
        msg = msg + text
        smtp = smtplib.SMTP(host,port)                      # 連線伺服器
        # smtp.set_debuglevel(1)                          # 設定除錯等級
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        print "Connected to Gmail"
        try:
            smtp.login(user,pw)                         # 登入伺服器
            print "login ok"
        except:     
            print "login Gmail fail"


        smtp.sendmail(fromaddr, toaddr, msg)                    # 傳送信件
        smtp.quit()                             # 中斷伺服器
    except :
        print "Email sending error !!"

#----------------------------------------------------------------------
if __name__ == "__main__":

    reload(sys)
    sys.setdefaultencoding('utf-8')

    sendEmail('V1.0.2.7')