"""
易购306（Yewgo306）项目：
本脚本项目基于Chrome浏览器74版本引擎开发
1.自动运行脚本打开12306
2.根据选项脚本自动选择出发地、目的地、出发日期、出发时间
3.若有票蜂鸣提示，并自动登陆到验证码页面
4.若无票则退出浏览器引擎
"""

# 导入selenium的webdriver模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from winsound import Beep
# from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")

# 出发地（fromStationText）：设为西安
fromStation=driver.find_element_by_id("fromStationText")
fromStation.click()
fromStation.clear()
fromStation.send_keys("西安")
fromStation.send_keys(Keys.DOWN)
fromStation.send_keys(Keys.ENTER)

# 目的地（toStationText）：设为上海
toStation=driver.find_element_by_id("toStationText")
toStation.click()
toStation.clear()
toStation.send_keys("上海\n")

# 出发日期（date_range）:设为5月25日
date_range=driver.find_element_by_xpath('//*[@id="date_range"]/ul/li[4]/span[1]')
date_range.click()

# 出发时间（start-time）:设为12：00-18：00
start_time=driver.find_element_by_xpath('//*[@id="cc_start_time"]/option[4]')
start_time.click()

# 选择出发站的checkbox为西安
check_station=driver.find_element_by_id("cc_from_station_西安_check")
check_station.click()

# 如果有票提示
hasTicket=driver.find_elements_by_xpath('//td[starts-with(@id,"YZ") and @class="yes"]')[0]
# 蜂鸣提示
if(hasTicket!=0):
    Beep(500,1000)
    # Todo:根据硬座的id找到火车的id点击订票按钮
    # driver.find_elements_by_xpath('')
    # 先找一个确定值的button试功能
    pay_btn=driver.find_element_by_class_name("btn72")
    pay_btn.click()
    # 点击账号登陆
    account_login=driver.find_element_by_xpath("/html/body/div[32]/div[2]/ul/li[2]/a")
    account_login.click()
    # 输入账号、密码
    login_email=driver.find_element_by_id("J-userName")
    login_email.send_keys("cdrcty@sina.com")
    login_password=driver.find_element_by_id("J-password")


else:
    driver.quit()