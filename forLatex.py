# -*- coding: utf-8 -*-

import winreg
import time


class LatexLicense(object):
    def __init__(self):
        """
        类的构造函数，一般将类的成员变量在此处写出来，并赋予初始值
        """
        self.interval = 1
        self.keyNames = {"WinEdt": False, "WinEdt 7": False}

    def run(self):
        """
        实际运行函数
        包含计时器和Delete操作
        """
        while True:
            self.del_redundant_keys()
            time.sleep(self.interval)

    def del_redundant_keys(self):
        """
        打开注册表，删除多余的键值
        """
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software")
        size = winreg.QueryInfoKey(key)
        for i in range(size[0]):
            for name in self.keyNames.keys():
                if winreg.EnumKey(key, i) == name:
                    self.keyNames[name] = True

        for name in self.keyNames.keys():
            if self.keyNames[name]:
                winreg.DeleteKey(key, name)
                self.keyNames[name] = False

        winreg.CloseKey(key)

test = LatexLicense()
test.run()