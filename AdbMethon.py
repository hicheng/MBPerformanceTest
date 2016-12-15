# -*- coding: utf-8 -*-

'''
用来调用adb shell
'''

import os
import subprocess
import sys
import time


devices_num = ""
'''
#判断是否设置了环境变量ANDROID_HOME
if "ANDROID_HOME" in os.environ:
    command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "abd.exe")
else:
    #执行了raise语句， raise后面的语句将不再执行
    raise EnvironmentError(
        "Adb not found in Android_Home path: %s." %os.environ["ANDROID_HOME"]
    )
'''
# 得到当前连接设备的信息
def get_device_list():
    devices = []
    # 启动进程
    result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    result.reverse()
    for line in result[1:]:
        if "attached" not in line.strip():
            devices.append(line.split()[0])
        else:
            break
    return devices

# adb命令
def adb(args):
    global devices_num
    if devices_num == "":
        devices = get_device_list()
        if len(devices) == 1:
            devices_num = devices[0]
        else:
            print u"没有连接设备"
    # 当已经有多个设备连接到主机时，可以使用-s参数进行选择
    cmd = "adb %s" % (str(args))
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# adb shell命令
def shell(args):
    global devices_num
    if devices_num == "":
        devices = get_device_list()
        if len(devices) == 1:
            devices_num = devices[0]
        else:
            print u"没有连接设备"
    # 当已经有多个设备连接到主机时，可以使用-s参数进行选择
    cmd = "adb shell %s" % (str(args))
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 时间戳
def timestamp():

    # 返回当前时间时间戳
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
