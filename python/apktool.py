# coding: utf-8
# Created by yeliang23 on 2018/6/19.
import os

# 2、Python反编译脚本
# 新建一个apktool.py，编写反编译、回编译和签名方法。
# 反编译：apktool d [apkFile] -f -o [outputDir]
# 回编译：apktool b [apkFile] -f -o [outputDir]
# 签名：可以使用jarsigner。
# jarsigner是JDK提供的针对jar包签名的通用工具。
# jarsigner -verbose -keystore [signFile] -signedjar [outputApk] [inputApk] [signAccount]


APK_TOOLS = 'E:/MyApps/Android/de_apk/mytools/apktool-2.4'
JDK = "E:/MyApps/Android/Java/jdk1.8.0_191"
KEYSTORE = 'E:/backup/keystore/larack.jks'


# 初始化
def init(root):
    global root_apktool, jdkroot  # 定义为全局变量
    root_apktool = APK_TOOLS  # 反编译工具apktool根目录
    jdkroot = JDK  # JDK根目录

    global default_signFile, default_account, default_password  # 默认签名信息
    default_signFile = KEYSTORE  # 签名文件路径
    default_account = "larack"  # 秘钥的账号
    default_password = "000000"  # 秘钥的密码


# 反编译
def Dcode(input):
    output = input.split('.')[0] + '-file'
    ResultFile = os.system('java -jar ' + root_apktool + "/apktool_bsf.jar" + ' d -f ' + input + " -o " + output)
    if ResultFile == 0:
        return 'Success'
    else:
        return 'Fail'


# 反编译
def Dcode(input, output):
    ResultFile = os.system('java -jar ' + root_apktool + "/apktool_bsf.jar" + ' d -f ' + input + " -o " + output)
    if ResultFile == 0:
        return 'Success'
    else:
        return 'Fail'


# 回编译
def Code(input):
    ResultFile = os.system('java -jar ' + root_apktool + "/apktool_bsf.jar" + ' b -f ' + input)
    if ResultFile == 0:
        return 'Success'
    else:
        return 'Fail'


# 签名
# 参数：
# jdkroot：JDK所在的位置
# inkeystore：秘钥的路径
# input：需要签名的APK路径
# output：生成的APK路劲
# account和password：秘钥的账号和密码
# 详情：
# jarsigner.exe 为jdk自带的文件，通常在jdk安装目录的bin文件夹下
# 例如：C:\Program Files\Java\jdk1.8.0_162\bin
# -verbose:签名/验证时输出详细信息
# -keystore:密钥的位置
# -storepass:秘钥的密码
def Sign(inkeystore, input, output, account, password):
    order = jdkroot + '/bin/jarsigner -verbose -keystore ' + inkeystore + " -signedjar " + output + " " + input + " " + account + " -storepass " + password
    os.system(order)


def Sign_haveback(input):
    output = input.split('.')[0] + '_sign.apk'
    order = jdkroot + '/bin/jarsigner -verbose -keystore ' + default_signFile + " -signedjar " + output + " " + input + " " + default_account + " -storepass " + default_password
    ResultFile = os.system(order)
    if ResultFile == 0:
        return 'Success'
    else:
        return 'Fail'


def remove_res_apk():
    order = 'del /s /a  C:/Users/xyz/AppData/Local/apktool/framework/1.apk '
    ResultFile = os.system(order)
    if ResultFile == 0:
        return 'Success'
    else:
        return 'Fail'


def test():
    # 反编译输入APK和输出文件夹
    input = "E:/apks/test.apk"
    output = "E:/apks/test"
    # 签名的各个参数
    signFile = default_signFile  # 签名文件路径
    signInput = "E:/apks/test.apk"  # 需要签名的apk
    signOutput = "E:/apks/test_sign.apk"  # 签名完成的apk
    account = default_account  # 秘钥的账号
    password = default_password  # 秘钥的密码
    # 测试
    Dcode(input, output)  # 反编译
    Code(output)  # 回编译
    Sign(signFile, signInput, signOutput, account, password)  # 签名


if '__main__' == __name__:
    init('')
    remove_res_apk()
    test()
    print('apktool')
