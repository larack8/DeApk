import os
import zipfile

new_dir_path = "E:/apks/test"
# 读取压缩文件
azip = zipfile.ZipFile("E:/apks/test.apk")
# 返回所有文件夹和文件
zip_list = azip.namelist()
# 新dex文件添加的后缀
suffix = 1
for item in zip_list:
    # 获取当前item文件的前缀名。如aa.txt的前缀名为aa，后缀名为.txt
    item_name = os.path.splitext(item)[0]
    # 获取当前item文件的后缀名
    item_suffix = os.path.splitext(item)[1]
    if item_suffix == ".dex":
        # 将当前文件复制粘贴至new_dir_path目录下面
        azip.extract(item, path=new_dir_path)
        # 如果是要批量处理classes.dex文件，那么下面的os.rename()就有意义了
        # 因为每个APK压缩包里面的dex文件均是classes.dex文件
        old_file_path = os.path.join(new_dir_path, item)
        new_item = item_name + "_" + str(suffix) + item_suffix
        new_file_path = os.path.join(new_dir_path, new_item)
        os.renames(old_file_path, new_file_path)
        # 用python语句执行cmd命令
        command = r"E:\MyApps\Android\de_apk\mytools\dex2jar-2.0\d2j-jar2dex.bat -f E:\apks\test\classes_1.dex"
        os.system(command)

# command = r"E:\MyApps\Android\de_apk\mytools\dex2jar-2.0\d2j-jar2dex.bat -f E:\apks\test\classes.dex"
# os.system(command)