#coding: utf-8
#Created by yeliang23 on 2018/6/19.

import sys
import os
from base import handle_file
from base import apktool

# 然后再写MainTool.py作为主入口调用各种py脚本，虽然现在只有一个反编译的脚本。
# 通过 from base import apktool 导入base文件夹下的apktool.py。如果是同文件夹下的就只要import就可以了。

def init():
    root = os.getcwd() #文件夹根目录
    apktool.init(root)

#测试各个模块
def moduletest(root):
    handle_file.test(root) #文件读写测试
    apktool.test() #反编译、回编译与签名测试

if '__main__' == __name__:
    print("========Python Start========")
    init() #初始化
    in_temp=input("请输入指令：（F：反编译，H：回编译+签名，Q：签名）\n")
    if in_temp == "F":
        print("===正在执行反编译===")
        in_apk=input("请输入需要反编译的APK：\n")
        apktool.Dcode(in_apk)
    elif in_temp == "H":
        print("===正在执行回编译===")
        in_file=input("请输入需要回编译的文件夹：\n")
        apktool.Code(in_file)
        for file in os.listdir(in_file+'/dist'):
            apkname=file
        print('apkname='+apkname)
        apktool.Sign(in_file+'/dist/'+apkname)
    elif in_temp == "Q":
        print("===正在执行签名===")
        in_apk=input("请输入需要签名的apk：\n")
        apktool.Sign(in_apk)
    else:
        print("===请输入对应的指令===")
    print("========Python End========")
    input("=按任意键关闭=")