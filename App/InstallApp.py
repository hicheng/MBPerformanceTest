# -*- coding:utf-8 -*-
'''
从本地电脑安装App到手机
'''
import os
import re

from MBPerformanceTest import AdbMethon
class Apk():

    def InstallApp(self):
        '''
        安装应用, 覆盖安装-r
        @return:
        '''
        apkname = raw_input(u"请输入要安装的Apk名: \n")

        # 卸载应用
        AdbMethon.adb("uninstall com.manboker.headportrait")

        # 删除文件夹
        AdbMethon.shell("rm -rf /sdcard/MomentCam")

        # 安装应用
        AdbMethon.adb("install C:\log\%s.apk" %apkname )

        '''
        # 使用正则， 传入的是正则地址
        try:
            res = re.compile(r'.*')
            pagename = os.path.join(" C:\log", "%s" %res) + ".apk"
            print pagename
            AdbMethon.adb("install %s" %pagename)
            print "b"
        except:
            pass
            '''
if __name__ == "__main__":
    Apk().InstallApp()
