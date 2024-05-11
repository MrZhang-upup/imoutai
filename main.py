from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType
import time
import os

daily_subscribe = 0
daily_tour = 0
luck_day = 0
daily_check = 0
test = 0

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformversion'] = '7.1.1'
desired_caps['deviceName'] = '192.168.0.104:5556'
# desired_caps['udid'] = '192.168.0.101:5556'
#desired_caps['appPackage'] = 'com.moutai.mall'
#desired_caps['appActivity'] = '.MainActivity'
desired_caps['noReset'] = 'True'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = None

# print(driver.current_package)
# print(driver.current_activity)


def handleException():
    try:
        driver.find_element_by_xpath("//*[@text='登录']")
        driver.find_element_by_id("com.moutai.mall:id/etPhone").clear()
        driver.find_element_by_id("com.moutai.mall:id/etPhone").send_keys("15895919875")
        flag = driver.find_element_by_class_name('android.widget.CheckBox').get_attribute('checked')
        if flag == "false":
            driver.find_element_by_class_name('android.widget.CheckBox').click()
        driver.find_element_by_xpath("//*[@text='获取验证码']").click()

        driver.start_activity('com.tencent.mobileqq', '.activity.SplashActivity')
        driver.find_element_by_xpath("//*[contains(@content-desc, 'phil')]").click()
        driver.find_element_by_class_name('android.widget.EditText').send_keys("i茅台登录过期，请输入验证码")
        driver.find_element_by_xpath("//*[@text='发送']").click()
        time.sleep(50)
        string = ""
        eles = driver.find_elements_by_class_name('android.widget.TextView')
        for i in range(len(eles)-1, -1, -1):
            if eles[i].text.find("yzm") != -1:
                string = eles[i].text[3:]
                break
        print(string)
        driver.press_keycode(4)  # back
        driver.press_keycode(4)  # back
        driver.find_element_by_id("com.moutai.mall:id/etVerifyCode").clear()
        driver.find_element_by_id("com.moutai.mall:id/etVerifyCode").send_keys(string)
        driver.find_element_by_xpath("//*[@text='登录']").click()
    except NoSuchElementException as e:
        print(e)


def daily_subcribe():
    try:
        #driver.start_activity('com.moutai.mall', '.MainActivity')
        driver.find_element_by_xpath("//*[@content-desc='i茅台']").click()
        driver.find_element_by_xpath("//*[@text='首页']").click()
        driver.find_element_by_xpath("//*[@text='首页']").click()
        driver.find_element_by_xpath("//*[@text='首页']").click()
        driver.find_element_by_id("com.moutai.mall:id/ivLeft").click()
        driver.find_element_by_xpath("//*[@text='预约申购']").click()
        driver.find_element_by_xpath("//*[@text='申购']").click()
        driver.find_element_by_xpath("//*[@text='确定申购']").click()
        driver.find_element_by_xpath("//*[@text='继续申购']").click()
        time.sleep(2)
        driver.swipe(530, 1700, 530, 300, 200)
        driver.swipe(530, 1700, 530, 300, 200)
        driver.find_element_by_xpath("//*[@text='预约申购']").click()
        driver.find_element_by_xpath("//*[@text='申购']").click()
        driver.find_element_by_xpath("//*[@text='确定申购']").click()
        driver.find_element_by_xpath("//*[@text='继续申购']").click()

        #check
        driver.press_keycode(4)  # back
        time.sleep(1)
        driver.press_keycode(4)  # back
        driver.find_element_by_xpath("//*[@text='我的']").click()
        driver.find_element_by_xpath("//*[@text='我的申购单']").click()
        date = driver.find_elements_by_id("com.moutai.mall:id/date_time")
        status = driver.find_elements_by_id("com.moutai.mall:id/draw_status")
        time.sleep(2)
        date = driver.find_elements_by_id("com.moutai.mall:id/date_time")
        status = driver.find_elements_by_id("com.moutai.mall:id/draw_status")
        string = ""
        for i in range(0, min(2, len(date))):
            string += date[i].text + status[i].text
        print(string)
        current_date = time.strftime("%Y-%m-%d", time.localtime())
        str = current_date + "静候申购结果" + current_date + "静候申购结果"
        print(str)
        driver.press_keycode(4)  # return
        if string == str:
            print("申购成功")
            return 0
        else:
            return -1
    except NoSuchElementException as e:
        print(e)
        handleException()
        return -1


def check_daily_subcribe():
    driver.find_element_by_xpath("//*[@content-desc='i茅台']").click()
    driver.find_element_by_xpath("//*[@text='我的']").click()
    driver.find_element_by_xpath("//*[@text='我的申购单']").click()
    date = driver.find_elements_by_id("com.moutai.mall:id/date_time")
    status = driver.find_elements_by_id("com.moutai.mall:id/draw_status")
    string = ""
    for i in range(len(date)):
        string += date[i].text + ":" + status[i].text + "\n"
    print(string)
    driver.start_activity('com.tencent.mobileqq', '.activity.SplashActivity')
    driver.find_element_by_xpath("//*[contains(@content-desc, 'phil')]").click()
    driver.find_element_by_class_name('android.widget.EditText').send_keys(string)
    driver.find_element_by_xpath("//*[@text='发送']").click()
    time.sleep(2)
    driver.press_keycode(4)  # back
    driver.press_keycode(4)  # back

def xiao_mao_yun():
    driver.find_element_by_xpath("//*[@content-desc='i茅台']").click()
    try:
        driver.find_element_by_xpath("//*[@text='小茅运']").click()
        driver.find_element_by_xpath("//*[@text='旅行']").click()
        driver.find_element_by_xpath("//*[contains(@text, '100耐力去旅行')]").click()
        driver.find_element_by_xpath("//*[@text='1650539651c20999']").click()  # exit
        return 0
    except NoSuchElementException as e:
        print(e)

    try:
        driver.find_element_by_xpath("//*[@text='小茅运']").click()
        driver.find_element_by_xpath("//*[@text='旅行']").click()
        driver.find_element_by_xpath("//*[@text='领取奖励']").click()
        driver.find_element_by_xpath("//*[@text='我知道了']").click()
        # driver.find_element_by_xpath("//*[@text='我知道啦']").click()
        time.sleep(2)
        TouchAction(driver).tap(x=315, y=1704).perform()
        driver.find_element_by_xpath("//*[@text='1650539651c20999']").click()  # exit
    except NoSuchElementException as e:
        print(e)
    return 1

    # driver.find_element_by_xpath("//*[@text='60耐力 加速完成']").click()
    # driver.find_element_by_xpath("//*[@text='40耐力 加速完成']").click()
    # driver.find_element_by_xpath("//*[@text='20耐力 加速完成']").click()
    # driver.find_element_by_xpath("//*[@text='小茅累了，明日继续']").click()
    # TouchAction(driver).tap(x=544, y=1620).perform()


def unlock():
    try:
        driver.unlock()
        time.sleep(1)
        driver.swipe(530, 1700, 530, 300, 200)
        TouchAction(driver).press(x=536, y=993).move_to(x=247, y=1283).move_to(x=536, y=1283).move_to(x=828, y=1283).release().perform()
        driver.press_keycode(3)  # home
    except Exception as e:
        print(e)

def lock():
    try:
        driver.press_keycode(4)  # back
        time.sleep(2)
        driver.press_keycode(4)  # back
        driver.press_keycode(3)  # home
        time.sleep(2)
        driver.close_app()
        time.sleep(2)
        driver.lock(0)
        # driver.press_keycode(26)  # power
        # driver.quit()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(20)
    while 1:
        current_time = time.localtime(time.time())
        if current_time.tm_hour == 8:
            print(current_time)
            daily_subscribe = 0
            daily_tour = 0
            luck_day = 0
            daily_check = 0
        elif current_time.tm_hour == 9 and daily_subscribe is 0:
            print(current_time)
            unlock()
            if daily_subcribe() == 0:
                daily_subscribe = 1
            lock()
        elif current_time.tm_hour == 9 and daily_tour is 0:
            print(current_time)
            unlock()
            if xiao_mao_yun() == 0:
                daily_tour = 1
            lock()
        elif test:
            print(current_time)
            unlock()
            lock()
        # elif current_time.tm_hour == 18 and 20 < current_time.tm_min < 50 and daily_check is 0:
        #     print(current_time)
        #     unlock()
        #     check_daily_subcribe()
        #     lock()
        #     daily_check = 1

        time.sleep(5)
