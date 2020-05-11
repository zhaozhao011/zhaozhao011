#fileName:page_display.py
import os, sys
sys.path.append(os.getcwd()) #解决bug：找不到导入的base模块
from base.page_base import PageBase #导入自定义的PageBase类

from selenium.webdriver.common.by import By

#页面类最好以“Page”开头
class PageDisplay(PageBase): #继承PageBase类
    #抽取这几个元素的元素定位特征(另外，通过XPATH定位的元素可简化XPATH)
    # “显示”按钮
    #display_button = By.XPATH,"//*[contains(@text,'Display')]"  # 是一个匿名元组。display_button[0]就是“By.XPATH”
    display_button = By.XPATH, "text,Display"
    # “放大镜”按钮
    search_button = By.ID,"com.android.settings:id/search"
    # “搜索文本框”
    input_text_view = By.ID,"android:id/search_src_text"
    # “返回箭头”按钮
    back_button = By.CLASS_NAME,"android.widget.ImageButton"

    def __init__(self, driver):
        PageBase.__init__(self, driver)  # 初始化父类的构造函数

    #函数功能：找到并点击“显示”按钮
    def click_display(self):
        self.click(self.display_button)

    #函数功能：找到并点击“放大镜”按钮
    def click_fandajin(self):
        self.click(self.search_button);

    #函数功能：找到“搜索文本框”，并输入文本text
    def input_search_text(self, text):
        self.input_text(self.input_text_view,text);

    #函数功能：点击“返回箭头”按钮
    def click_back(self):
        self.click(self.back_button);

