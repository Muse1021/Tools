# -*- coding: utf-8 -*-
import os,subprocess,time,re,sys
def get_devices():
    logcmd = "adb devices"
    #Poplog = subprocess.Popen(logcmd,stderr=subprocess.PIPE)
    #Poplog = os.popen(logcmd)
    Poplog = subprocess.Popen(logcmd, shell=True, stdout=subprocess.PIPE).stdout
    devices = Poplog.readlines()
    devices_list = []
    model_list ={}
    for i in devices:
        if 'devices' not in i and len(i.split()) > 0:
            #print "i: ",i
            #print "len: ",len(i)
            devices_list.append(i.split()[0])
    device_number = len(devices_list)
    print(devices_list)
    if device_number == 0 :
        print "NO decices !!"      
    else:
        for i in range(device_number):
            print "11111:",devices_list[i]
            de = "adb -s %s shell  getprop ro.product.model" % (devices_list[i])
            Poplog = subprocess.Popen(de, shell=True, stdout=subprocess.PIPE).stdout
            print "test:::::::",Poplog.read().split(": ")[-1]
            print("complete")
            strs = (Poplog.readlines()[0]).strip()
            model_list[strs] = devices_list[i]
    return model_list
if __name__ == "__main__":
    print(get_devices())


