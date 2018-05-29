# Import required python libraries
import os
import time
import datetime
import glob
import shutil
import urllib
import json
import sys
import re
import urllib.request
# MySQL database details to which backup to be done. Make sure below user having enough privileges to take databases backup.
# To take multiple databases backup, create any file like /backup/dbnames.txt and put databses names one on each line and assignd to DB_NAME variable.

DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = 'root123'
DB_PORT = '3308'
DB_NAME = 'E:/python/backup/dbnames.txt'
#DB_NAME = 'vding_prod_online'
#window version path
BACKUP_PATH = 'E:/python/backup/'
#linux version path
#BACKUP_PATH = '/backup/dbbackup/'
toMobile = '15986845591'


# Getting current datetime to create seprate backup folder like "12012013-071334".
DATETIME = time.strftime('%Y%m%d')

TODAYBACKUPPATH = BACKUP_PATH + DATETIME
DB_FILES_PATH = BACKUP_PATH + '*'


def backupDB():
    # Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
    print ("checking for databases names file.")
    if os.path.exists(DB_NAME):
        file1 = open(DB_NAME)
        multi = 1
        print ("Databases file found...")
        print ("Starting backup of all dbs listed in file " + DB_NAME)
    else:
        print ("Databases file not found...")
        print ("Starting backup of database " + DB_NAME)
        multi = 0
    # Starting actual database backup process.
    if multi:
        in_file = open(DB_NAME,"r")
        flength = len(in_file.readlines())
        in_file.close()
        p = 1
        dbfile = open(DB_NAME,"r")
        while p <= flength:
            db = dbfile.readline()   # reading database name from file
            db=db.strip('\n')     #去掉换行符
            print (db)
            dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " -P" + DB_PORT + " --master-data=2 " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"

            if(os.system(dumpcmd) == 0):
               message = "数据库:%s---备份成功!" % db
               sendMsgToDD(message,toMobile)
               #print ("Your backups has been created in '" + TODAYBACKUPPATH + "' directory")
            else:
               message = "数据库:%s---备份失败!" % db
               sendMsgToDD(message,toMobile)
            p = p + 1

        dbfile.close()
    else:
        db = DB_NAME
        dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " -P" + DB_PORT + " --master-data=2 " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
        if (os.system(dumpcmd) == 0):
            message = "数据库:%s---备份成功!" % DB_NAME
            sendMsgToDD(message,toMobile)
            #print ("Your backups has been created in '" + TODAYBACKUPPATH + "' directory")
        else:
            message = "数据库:%s---备份失败!" % DB_NAME
            sendMsgToDD(message,toMobile)


def removeAddBackFiles():
    # Checking if backup folder already exists or not. If not exists will create it.
    print ("del folder three days ago")
    folders = glob.glob(DB_FILES_PATH)
    today = datetime.datetime.now()
    for item in folders:
        try:
            foldername = os.path.split(item)[1]
            day = datetime.datetime.strptime(foldername, "%Y%m%d")
            diff = today - day
            if diff.days >= 3:
                shutil.rmtree(item)
        except:
            pass
    print ("creating backup folder")
    if not os.path.exists(TODAYBACKUPPATH):
        os.makedirs(TODAYBACKUPPATH)



def sendMsgToDD(ddmsg,moblie):
    headers = {'Content-Type': 'application/json'}
    test_data = {
    'msgtype':"text",
    "text":{
        'content':"%s" % ddmsg
    },
    "at":{
        "atMobiles":[
            "%s" % moblie
        ],
        "isAtAll":False
    }
    }
    requrl = "https://oapi.dingtalk.com/robot/send?access_token=b17eb64223cf39738a404acd375e88ce21d1a6d2c97e448a5f809d7761b94fe2"
    req = urllib.request.Request(url = requrl,headers = headers,data = json.dumps(test_data).encode(encoding='utf-8'))
    response = urllib.request.urlopen(req)

def main():
    removeAddBackFiles()
    backupDB()
    sendMsgToDD("#####执行完成######",toMobile)

main()
