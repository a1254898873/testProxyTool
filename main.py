# -*- coding: utf-8 -*-
import requests
import threading
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
import sys
from log import error, info, success

# 代理列表
lines = []

# 可用代理
proxy_alive = []


# 代理测试
def test_proxy(self, index, thread_num, timeout, length):
    url = "http://icanhazip.com"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'
    }
    while index < length:
        # mutex.acquire()
        global lines
        line = lines[index]
        # mutex.release()
        index = index + thread_num
        proxy = {'http': "http://{a}".format(a=line), 'https': "https://{a}".format(a=line)}
        try:
            r = requests.get(url, headers=headers, proxies=proxy, timeout=timeout)
            if r.status_code == requests.codes.ok:
                success(line + "  " + "代理可用")
                # mutex.acquire()
                self.ui.list_alive.appendPlainText(line)
                # mutex.release()
        except Exception as e:
            error(line + "  " + "代理不可用")




# 多线程测试代理
def test_proxy_multithreading(self, text, thread_num, timeout):
    n = int(thread_num)
    t = int(timeout)
    global lines
    lines = text.split("\n")
    l = len(lines)
    for i in range(0, n):
        t = threading.Thread(target=test_proxy, args=(self, i, n, t, l))
        t.start()


# 窗体函数
class MainWidget(QWidget):

    def __init__(self):
        # 调用父类的初始化方法
        super().__init__()
        # 完成对本widget的初始化操作
        self.__init_ui()

    def __init_ui(self):
        self.ui = uic.loadUi("./window.ui")
        self.ui.button_import.clicked.connect(self.import_proxy)
        self.ui.button_start.clicked.connect(self.start_test)
        # 显示在屏幕上
        self.ui.show()

    def import_proxy(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择你要上传的图片",  # 标题
            r"./",  # 起始目录
            "(*.txt)"  # 选择类型过滤项，过滤内容在括号中
        )
        with open(filePath, "r") as f:
            text_proxy = f.read()
            self.ui.list_proxy.setPlainText(text_proxy)

    def start_test(self):
        thread_num = self.ui.text_thread.toPlainText()
        timeout = self.ui.text_timeout.toPlainText()
        if thread_num is None or thread_num == "":
            error("请输入线程数")
            return
        if timeout is None or timeout == "":
            error("请输入延迟时间")
            return
        text = self.ui.list_proxy.toPlainText()
        info("开始测试代理")
        test_proxy_multithreading(self, text, thread_num, timeout)


if __name__ == "__main__":
    mutex = threading.Lock()  # 创建锁
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = MainWidget()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplicat
