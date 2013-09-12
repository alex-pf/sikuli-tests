from sikuli import *
# -*- coding: utf-8 -*-
import os
import sys
import shutil

def deleteFileOrFolder(directory):
    if os.path.exists(directory):
        try:
            if os.path.isdir(directory):
                # delete folder
                shutil.rmtree(directory)
            else:
                # delete file
                os.remove(directory)
        except:
            print "Ecxeption ",str(sys.exc_info())
    else:
        print "not found ",directory


def clearData():
    batPath = os.environ.get("GIT_HOME") + "sikuli-tests\\baseFunction.sikuli\clear.bat"
    try:
        os.system(batPath)
        print (u"Папка NavstatExpress удалена")
        return 1
    except:
        print (u"Папка NavstatExpress не удалена!")
        return 0
        

def startNavstat(userName = u"admin", password = u"admin"):
    click("1376484163733.png")
    wait("1376485054733.png",10)
    type(Pattern("VnO1Tb3OBBT1.png").targetOffset(42,2), userName.encode("UTF-8"))
    type(Key.TAB)
    type(password.encode("UTF-8"))
    click("OK.png")
    try:
        wait(Pattern("NAVSTAT-1.png").similar(0.80), 300)
    except:
        print (u"Навстат не запустился")
        exit()


def firstStartNavstat(userName = u"admin", password = u"admin"):
    startNavstat(userName, password)
    try:
        click(Pattern("Vlcropvmvrsm.png").targetOffset(64,-1))
        print (u"Первичный запуск Навстат")
    except:
        print (u"Это не первичный запуск Навстат")
        exit()

# аналог wait принимает на вход список картинок и время ожидания в секундах, возвращает номер найденной картинки
# если не дождались возвращаем "-1"
def waitList(imgList, timer):
    start = time.time() + timer
    while start > time.time():
        print " --- ", start, " - ", time.time(), " = ", start-time.time()
        i=0
        while i < len(imgList):
            print "Find ", i
            try:
                find(imgList[i])
                return i
            except:
                print("Don't find ")
            i+=1
    return -1
# Установка периода для отчётов и истории -----------------------------------------------------------------
import time
import datetime
def setInterval(day1,day2):
    # Навстат должен быть запущен и открыта панель с датапикером
    doubleClick(Pattern("3GlpHOJ1BDBM.png").targetOffset(-39,-4))
    paste(day1.strftime("%d.%m.%Y "))
    doubleClick(Pattern("3GlpHOJ1BDBM.png").targetOffset(-37,23))
    paste(day2.strftime("%d.%m.%Y "))
# ---------------------------------------------------------------------------------------------------------
