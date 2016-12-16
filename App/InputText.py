# -*- coding:utf-8 -*-
'''
用adb shell input text string 向手机屏幕输入字符串
'''
import os


class InputText():
    def inputText(self):

        try:
            # 输入字符串
            for n in range(0,100):
                input = raw_input(u"写出你要输入的字符串（仅支持英文和数字）： \n")
                os.popen("adb shell input text %s" % input)
        except:
            print u"输入出问题啦~~QAQQQ"


if __name__ == "__main__":
    InputText().inputText()