#fileName:test_network.py
import os, sys
#print(os.getcwd());#输出"D:\PyCharm_WK\py3_project01"
sys.path.append(os.getcwd()) #把当前工作目录"D:\PyCharm_WK\py3_project01"添加进系统环境变量PATH中，用于解决：pytest找不到模块问题！

from base.base_driver import init_driver
from page.page_network import PageNetwork #导入页面类PageNetwork类
from appium import webdriver

class TestNetwork:
    def setup(self):
        self.driver = init_driver()
        self.page_network = PageNetwork(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_mobile_network_2g(self):
        #步骤1：点击“更多”
        self.page_network.click_more();
        #步骤2：点击“移动网络”
        self.page_network.click_yidonwanluo();
        #步骤3：点击“首选网络类型”
        self.page_network.click_PreNetworkType();
        #步骤4：点击"2G"
        self.page_network.click_2G();


    def test_mobile_network_3g(self):
        # 步骤1：点击“更多”
        self.page_network.click_more();
        # 步骤2：点击“移动网络”
        self.page_network.click_yidonwanluo();
        # 步骤3：点击“首选网络类型”
        self.page_network.click_PreNetworkType();
        # 步骤4：点击"3G"
        self.page_network.click_3G();

