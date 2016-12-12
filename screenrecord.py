# -*- coding:utf-8 -*-

'''
执行ADB命令录制视频
录制视频要求API level > 19
'''

import os

import time
from PublicResour import AdbMethon

PATH = lambda p: os.path.abspath(p)

def Record():
    # 录制视频(存在sdcard中)
    AdbMethon.shell("screenrecord /sdcard/sina/vide2.mp4")
    # 停止录制
    input_key = raw_input("Please press the Enter key to stop recording :\n")
    if input_key == "":
        AdbMethon.adb("kill-server")
    print "Get Video file..."

    # 重启adb server
    AdbMethon.adb("start-server")
    time.sleep(2)

    path = PATH("%s/video" %os.getcwd())
    if not os.path.isdir(path):
        os.makedirs(path)

    # wait()等待子进程结束
    AdbMethon.adb("pull /sdcard/sina/vide2.mp4 %s" % PATH("%s/%s.mp4" % (path, AdbMethon.timestamp()))).wait()

if __name__ == "__main__":
    Record()

