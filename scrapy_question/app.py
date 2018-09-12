# from appium import webdriver
#
# desired_caps = {}
#
# # desired_caps['platformName'] = 'Android'
# #
# # desired_caps['platformVersion'] = '4.4.2'
# #
# # desired_caps['deviceName'] = 'Android Emulator'
# #
# # desired_caps['appPackage'] = 'com.android.calculator2'\
# #
# #desired_caps['appActivity'] = '.Calculator'
#
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '8.0.0'
# desired_caps['deviceName'] = '3329692b'
# desired_caps['appPackage'] = 'com.android.calculator2'\
#
# desired_caps['appActivity'] = '.Calculator'
# # desired_caps['appPackage'] = 'com.yishiwan'
# # desired_caps['appActivity'] = 'com.e4a.runtime.android.StartActivity'
#
#
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
# driver.find_element_by_name("1").click()
#
# driver.find_element_by_name("5").click()
#
# driver.find_element_by_name("9").click()
#
# driver.find_element_by_name("9").click()
#
# driver.find_element_by_name("5").click()
#
# driver.find_element_by_name("+").click()
#
# driver.find_element_by_name("6").click()
#
# driver.find_element_by_name("=").click()
#
# driver.quit()



from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0'
desired_caps['deviceName'] = '3329692b'
desired_caps['appPackage'] = 'com.yishiwan'
desired_caps['appActivity'] = 'com.e4a.runtime.android.StartActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.lock(5)
createContactBtn = driver.find_element_by_id('com.miui.home:id/icon_icon')
# 模拟点击操作
createContactBtn.click()

driver.find_element_by_id('com.android.dialer:id/search_box_collapsed').click()
search_box = driver.find_element_by_id('com.android.dialer:id/search_view')
search_box.click()
search_box.send_keys('hello toby')



# from appium import webdriver
#
# class Appium_Contect:
#     def __init__(self,reset):
#         self.desired_caps = {'platformName': 'Android',
#                         'deviceName': '3329692b',
# 			            # 'app':'D:\ADT\T.apk',#
#                         'appPackage': 'com.yishiwan',
#                         'appActivity': 'com.e4a.runtime.android.StartActivity',
#                         'noReset': reset,#是否重置，清除数据。true不重置，false重置
#                         "unicodeKeyboard":True,
#                         "resetKeyboard":True}
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
#
#     def get_driver(self):
#         return self.driver
#
#     def quit_driver(self):
#         self.driver.quit()
#
# if __name__=='__main__':
#     ac=Appium_Contect(True)
#     ac.get_driver()
#     ac.quit_driver()




# from appium import webdriver
#
# # import os
# # java_path = "C:\Program Files\Java\jdk1.8.0_151\\bin" # replace this
# # os.environ['JAVAHOME'] = "C:\Program Files\Java\jdk1.8.0_151"
#
# import time
#
# import unittest  # 导入unittest框架，此文用到了断言
#
# desired_caps = {
#
#  'platformName': 'Android',
#
#  'deviceName': '3329692b',
#
#  'platformVersion': '8.0.0',
#
#  'appPackage': 'com.yishiwan',
#
#  'appActivity': 'com.e4a.runtime.android.StartActivity',
#
#  # 'unicodeKeyboard': True,
#
# # 'resetKeyboard': True
#
# }
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

