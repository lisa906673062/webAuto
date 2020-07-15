
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.baidu.com") #打开百度
time.sleep(3)#等待3秒
driver.maximize_window()#最大化窗口
driver.refresh()#刷新页面

driver.get("http://www.taobao.com") #打开淘宝
time.sleep(3)#再等待3秒

driver.get("http://www.jd.com")#打开京东
time.sleep(3)#等待3秒
# driver.minimize_window()#窗口最小化
time.sleep(3)

driver.back()#回退后一步，上一个页面，这里回退到淘宝
time.sleep(3)#等待3秒

driver.forward()#前进下一个页面，这里会到京东
driver.maximize_window()#最大化窗口

driver.close()#关闭页面
# driver.quit()#退出所有窗口