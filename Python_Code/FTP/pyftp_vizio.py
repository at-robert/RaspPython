# -*- coding:utf-8 -*-
# file: pyftp.py
#
import os
import FtpUploadTracker
from ftplib import FTP_TLS
from ftplib import FTP                          # 從ftplib模組中匯入FTP

import sys
import smtplib
import time

def sendEmail(VER):                                      # 按鈕事件
    try:                                        # 例外處理
        host = 'smtp.gmail.com'                      # 取得伺服器位址
        port = 587            # 取得通訊埠
        user = str('ee3amt@gmail.com').strip()                     # 取得使用者名稱
        pw = str('fw_oem12').strip()                       # 取得密碼
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

bufsize = 1024                                  # 設定緩沖區大小
def Get(filename):                              # 下載檔案
    command = 'RETR ' + filename
    ftp.retrbinary(command, open(filename,'wb').write, bufsize)
    print('下載成功')
def Put(filename):                              # 上傳檔案
    command = 'STOR ' + filename
    filehandler = open(filename,'rb')
    ftp.storbinary(command,filehandler,bufsize)
    filehandler.close()
    print('上傳成功')
def PWD():                                  # 取得目前目錄
    print(ftp.pwd())
def Size(filename):                             # 取得檔案大小
    print(ftp.size(filename))
def Help():                                 # 輸出幫助
    print('''
    ==================================
        Simple Python FTP 
    ==================================
    cd      進入資料夾
    delete      移除檔案
    dir     取得目前檔案清單
    get     下載檔案
    help        幫助
    mkdir       建立資料夾
    put     上傳檔案
    pwd     取得目前目錄
    rename      更名檔案
    rmdir       移除資料夾
    size        取得檔案大小
    ''')
# server = raw_input('請輸入FTP伺服器位址:')                    # 取得伺服器位址
# ftp = FTP(server)                             # 連線到伺服器位址
# username = raw_input('請輸入使用者名稱:')                     # 取得使用者名稱
# password = raw_input('請輸入密碼:')                        # 取得字典

if len(sys.argv) < 2:
    print("用法：python pyftp_vizio.py <<VER>>")
    exit(1)  

VER = sys.argv[1]
print "VER = %s" %(VER)

#Rake FTP
server = '54.68.189.167'                    # 取得伺服器位址
# ftp = FTP()
ftp = FTP_TLS()

ftp.connect(server, 990)
username = 'Amtran_SX7'
password = 'E~S3f0QsQoxoz:q'

ftp.login(username,password)                                # 登入FTP
print(ftp.getwelcome())                         # 取得歡迎訊息
actions  = {'dir':ftp.dir, 'pwd': PWD, 'cd':ftp.cwd, 'get':Get,         # 指令與對應的函數字典
        'put':Put, 'help':Help, 'rmdir': ftp.rmd, 
        'mkdir': ftp.mkd, 'delete':ftp.delete,
        'size':Size, 'rename':ftp.rename}

# ftp.cwd('SB/MTK')
# ftp.dir()


''' To upload a file to the FTP site
pwd = os.path.expanduser('~') + '/'
filefullname = pwd + '/Downloads/dolby.m2ts'

totalSize = os.path.getsize(filefullname)
print('Total file size : ' + str(round(totalSize / 1024/1024  ,1)) + ' Mb')

filename = os.path.basename(filefullname)
fp = open(filefullname, 'rb')
uploadTracker = FtpUploadTracker.FtpUploadTracker(int(totalSize))
'''

count = 0
# VER = 'V1.0.2.9'
# tgz_str = '/AMTRAN_C4A/' + VER + '/' + VER + '_rel.tgz'

while True:
    try:
        ftp.connect(server, 990)
        ftp.login(username,password)
        print(ftp.getwelcome()) 

        Size_str = '/AMTRAN_C4A/' + VER + '/' + VER + '.utv'
        # tgz_str = '/AMTRAN_C4A/' + VER + '/' + VER + '_rel.tgz'
        print "%s exist on the Vizio FTP site, size is = %d" %(VER, (ftp.size(Size_str)))

        sendEmail(VER)
        ftp.quit()
        break
    except:
        print "%s doesn't exist" %(VER)
        ftp.quit()

        time.sleep(1800)
        count = count + 1

        if(count >= 5):
            VER = 'V1.0.3.1' 


# try:
#     print "%s exist on the Vizio FTP site, size is = %d" %(VER + '_tgz', (ftp.size(tgz_str)))
# except:
#     print "%s doesn't exist" %(VER + '_tgz')




# while True:                                   # 指令循環
#   print('pyftp>', )                           # 輸出提示符
#   cmds = raw_input()                          # 取得輸入
#   cmd = str.split(cmds)                       # 將輸入按空格分割
#   try:                                    # 例外處理
#       if len(cmd) == 1:                       # 判斷指令是否有參數
#           if str.lower(cmd[0]) == 'quit':         # 若果指令為quit則離開循環
#               break
#           elif str.lower(cmd[0]) == 'upload':
#               print "STOR %s" %(filename)
#               ftp.storbinary('STOR %s' %(filename) , fp, 1024, uploadTracker.handle)
#           else:
#               actions[str.lower(cmd[0])]()            # 呼叫與指令對應的函數
#       elif len(cmd) == 2:                     # 處理指令有一個參數的情況
#           actions[str.lower(cmd[0])](cmd[1])          # 呼叫與指令對應的函數
#       elif len(cmd) == 3:                     # 處理指令有兩個參數的情況
#           actions[str.lower(cmd[0])](cmd[1],cmd[2])       # 呼叫與指令對應的函數
#       else:
#           print('輸入錯誤')
#   except:
#       print('指令出錯')
# ftp.quit()                                  # 通訊埠連線
