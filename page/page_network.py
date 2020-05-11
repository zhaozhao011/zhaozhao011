#fileName:page_network.py
import os, sys
sys.path.append(os.getcwd()) #解决bug：找不到导入的base模块
from base.page_base import PageBase #导入自定义的PageBase类

from selenium.webdriver.common.by import By

#页面类
class PageNetwork(PageBase):#继承基类页面类PageBase
    #抽取这几个元素的元素定位特征(另外，通过XPATH定位的元素可简化XPATH)
    # “更多”按钮
    more_button = By.XPATH, "text,More"
    # “移动网络”按钮
    network_button = By.XPATH,"text,Cellular networks"
    # “首选网络类型”按钮
    first_network_button = By.XPATH,"text,Preferred network type"
    # “2G”按钮
    network_2g_button = By.XPATH,"text,2G"
    # “3G”按钮
    network_3g_button = By.XPATH,"text,3G"

    def __init__(self, driver):
        PageBase.__init__(self, driver)

    #函数功能：找到并点击“更多”按钮
    def click_more(self):
        self.click(self.more_button)

    #函数功能：找到并点击“移动网络”
    def click_yidonwanluo(self):
        self.click(self.network_button)

    #函数功能：找到并点击“首选网络类型”
    def click_PreNetworkType(self):
        self.click(self.first_network_button)

    #函数功能：找到并点击“2G”
    def click_2G(self):
        self.click(self.network_2g_button)

    #函数功能：找到并点击“3G”
    def click_3G(self):
        self.click(self.network_3g_button)