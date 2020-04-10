# coding: utf-8
# Created by yeliang23 on 2018/6/19.

import sys
import os
import threading
import time
from base import apktool
from PyQt5.QtWidgets import QMainWindow, QApplication  # 导入PyQt5相关资源
from ui import decompile_mainUI  # 导入反编译的主界面
from ui import tipsUI  # 导入提示界面


def init():
    root = os.getcwd()  # 文件夹根目录
    apktool.init(root)


# 提示语
def tipsUItxt(result, Success, Fail, Unknown):
    if result == 'Success':
        tips.setText(Success)
    elif result == 'Fail':
        tips.setText(Fail)
    else:
        tips.setText(Unknown)


# 反编译
def decompiles(address):
    result = apktool.Dcode_haveback(address)
    tipsUItxt(result, '反编译成功', '反编译失败', '遇到未知错误')


# 回编译
def compiles(address):
    result = apktool.Code_haveback(address)
    tipsUItxt(result, '回编译成功', '回编译失败', '遇到未知错误')


# 签名
def sign(address):
    result = apktool.Sign_haveback(address)
    tipsUItxt(result, '签名成功', '签名失败', '遇到未知错误')


# 提示界面
class tipsUI_Desiger(QMainWindow, tipsUI.Ui_Form):
    def __init__(self, parent=None):
        super(tipsUI_Desiger, self).__init__(parent)
        self.setupUi(self)

    def setText(self, txt):
        self.progress_tips_text.setText(txt)


# 主界面
class decompile_mainUI_Desiger(QMainWindow, decompile_mainUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(decompile_mainUI_Desiger, self).__init__(parent)
        self.setupUi(self)

        self.Decompile_Button.clicked.connect(self.decompileBut)  # 监听点击事件（反编译）
        self.Compile_Button.clicked.connect(self.compileBut)  # 回编译
        self.Sign_Button.clicked.connect(self.signBut)  # 签名

    def decompileBut(self):  # 点击事件（反编译）
        address = self.Decompile_Edit.toPlainText()  # 获取输入框内容
        if '///' in address:  # 拖拉进来的文件都带有“file:///”，要把它去掉
            address = address.split('///')[1]
        tips.setText('  请稍等......')  # 设置提示语
        tips.show()  # 弹出提示
        decompilesThread = threading.Thread(target=decompiles, args=(address,))
        decompilesThread.start()  # 新开一个线程 调用反编译方法
        # decompilesThread.join() #等待反编译结束

    def compileBut(self):  # 回编译
        address = self.Compile_Edit.toPlainText()
        if '///' in address:
            address = address.split('///')[1]
        tips.setText('  请稍等......')
        tips.show()
        CompilesThread = threading.Thread(target=compiles, args=(address,))
        CompilesThread.start()
        # decompilesThread.join()

    def signBut(self):  # 签名
        signfile_address = self.SignFile_Edit.toPlainText()
        if len(signfile_address) == 0:
            address = self.Sign_Edit.toPlainText()
            if '///' in address:
                address = address.split('///')[1]
            tips.setText('  请稍等......')
            tips.show()
            SignThread = threading.Thread(target=sign, args=(address,))
            SignThread.start()
            # decompilesThread.join()
        else:
            tips.setText('暂不支持更换签名')
            tips.show()


if __name__ == "__main__":
    init()  # 初始化
    app = QApplication(sys.argv)  # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    decompile_main_ui = decompile_mainUI_Desiger()
    tips = tipsUI_Desiger()
    decompile_main_ui.show()
    sys.exit(app.exec_())  # 程序运行，sys.exit方法确保程序完整退出。
