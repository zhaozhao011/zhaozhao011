#fileName:test_display.py
import os, sys
#print(os.getcwd());#输出"D:\PyCharm_WK\py3_project01"
sys.path.append(os.getcwd()) #把当前工作目录"D:\PyCharm_WK\py3_project01"添加进系统环境变量PATH中，用于解决：pytest找不到模块问题！

from base.base_driver import init_driver
from page.page_display import PageDisplay #导入此页面类PageDisplay类
from appium import webdriver

class TestDisplay:
    def setup(self):
        self.driver = init_driver()
        self.page_display = PageDisplay(self.driver) #页面类PageDisplay的类对象

    def teardown(self):
        self.driver.quit()

    def test_mobile_display_input(self):
        #步骤1：点击“显示”按钮
        self.page_display.click_display();
        #步骤2：点击“放大镜”按钮
        self.page_display.click_fandajin();
        #步骤3：在“搜索文本框”中输入"hello"
        self.page_display.input_search_text("hello");
        #步骤4：点击“返回箭头”按钮
        self.page_display.click_back();
