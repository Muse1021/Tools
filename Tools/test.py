#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os,subprocess,time,re,sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
def test():
    screenshot = "adb shell /system/bin/screencap -p /sdcard/screenshot.png"
    pic_name = str(int(time.time()))+".png"
    screenshot_pull = "adb pull /sdcard/screenshot.png E:/screenshot/%s"%pic_name
    subprocess.Popen(screenshot,shell=True, stdout=subprocess.PIPE).stdout
    if  os.path.exists("E:/screenshot"):
        pass
    else:
        os.mkdir("E:/screenshot")
    Poplog = subprocess.Popen(screenshot_pull, shell=True, stdout=subprocess.PIPE).stdout
    Poplog.readlines()
a = "sssss"
b = "bbbbb"
print "%s1%s2"%(a,b)

