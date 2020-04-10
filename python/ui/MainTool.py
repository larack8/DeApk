import sys

from PyQt5.QtWidgets import QMainWindow, QApplication  # 导入PyQt5相关资源

from ui import decompile_mainUI  # 导入反编译的主界面


def init():
    root = os.getcwd()  # 文件夹根目录


# 主界面UI
class decompile_mainUI_Desiger(QMainWindow, decompile_mainUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(decompile_mainUI_Desiger, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    init()  # 初始化
    app = QApplication(sys.argv)  # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    decompile_main_ui = decompile_mainUI_Desiger()
    decompile_main_ui.show()  # 显示
    sys.exit(app.exec_())  # 程序运行，sys.exit方法确保程序完整退出。
