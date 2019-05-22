# 导入selenium的webdriver模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from winsound import Beep

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

# 如果有票提示
hasTicket=driver.find_elements_by_xpath('//td[starts-with(@id,"YZ") and @class="yes"]')[0]
# 蜂鸣提示
if(hasTicket!=0):
    Beep(500,1000)
    # Todo:根据硬座的id找到火车的id点击订票按钮
    # driver.find_elements_by_xpath('')
else:
    driver.quit()