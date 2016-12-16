# -*- coding: utf-8 -*-


from MBPerformanceTest import AdbMethon
class Apk():

    def UnInstallApp(self):
        '''
        卸载应用、删除文件夹
        @return:
        '''
        try:

            # 卸载应用
            AdbMethon.adb("uninstall com.manboker.headportrait")

            # 删除文件夹
            AdbMethon.shell("rm -rf /sdcard/MomentCam")

            print u"卸载完成请稍等"

        except:
            print u"卸载时遇到问题了QAQ"

if __name__ == "__main__":
    Apk().UnInstallApp()