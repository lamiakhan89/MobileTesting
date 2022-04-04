#! /usr/bin/env monkeyrunner

import os
import subprocess
import pytest
import json
import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

version = '1.0.0'
test = 'test1'


def setup_module(module):
    subprocess.call(['python3', 'OnStreamClearFolders.py'])
    return module


@pytest.fixture(scope="class")
def directory(request):
    name = os.environ.get('PYTEST_CURRENT_TEST')
    """.split(':')[-1].split(' ')[0]"""
    direct = '/Users/dishbusiness/Desktop/OnStreamTestFiles/Pictures/'
    request.cls.direct = direct
    request.cls.name = name
    yield


@pytest.fixture(scope="class")
def setup(request):
    subprocess.call(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_HOME'])
    appium_service = AppiumService()
    appium_service.start()
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Dish\'s 8th FireTVStick '
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['udid'] = '192.168.43.73:5555'
    desired_caps['platformVersion'] = '7.2.4.2'
    desired_caps['appPackage'] = 'tv.accedo.xdk.dishtv'
    ##desired_caps['appWaitActivity'] = 'MainActivity'
    desired_caps['appActivity'] = 'tv.accedo.dishonstream2.ui.main.MainActivity' # only keep this one
    desired_caps['eventTimings'] = 'True'
    desired_caps['recordDeviceVitals'] = 'True'
    desired_caps['recordDeviceVitals']='True'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.cls.driver = driver
    yield
    time_events = driver.get_events()
    ##with open('/Users/dishbusiness/Desktop/OnStreamTestFiles/Duration/Event_Time_Log.json', 'w', encoding='utf-8') as t:
        ##json.dump(time_events, t, ensure_ascii=False, indent=4)
    ##cpu = driver.get_performance_data('tv.accedo.xdk.dishtv', 'memoryinfo', 10)
    ##with open('/Users/dishbusiness/Desktop/OnStreamTestFiles/Duration/cpu.txt', 'w', encoding='ISO-8859-1') as c:
        ##print(cpu, file=c)
    driver.quit()


@pytest.mark.usefixtures("setup", "directory")
class TestHomeScreen:
    def test_home_screen_main(self):
        try:
            time.sleep(20)
            self.driver.find_element(By.XPATH,"//*[contains(@resource-id, 'tv.accedo.xdk.dishtv:id/home')]")  # wait for homepage to load
            time.sleep(10)
            self.driver.press_keycode(23)  # home key
            time.sleep(10)
            self.driver.press_keycode(20)  # down
            self.driver.press_keycode(23)  # learn more
            self.driver.press_keycode(4)  # back
            self.driver.press_keycode(22)  # right level
            self.driver.press_keycode(23)  # click learn more
            self.driver.press_keycode(4)  # back
            self.driver.press_keycode(20)#down to featured channels
            self.driver.press_keycode(22)#right
            self.driver.press_keycode(22)#right
            self.driver.press_keycode(21)  # left
            self.driver.press_keycode(21)  # left
            self.driver.press_keycode(23)  # click 1st box
            self.driver.press_keycode(23)  # click
            self.driver.press_keycode(23)  # click
            self.driver.press_keycode(24) #down
            #removing to the sports area

            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'Welcome to your new live TV')]") #welcome message
            self.driver.find_element_by_xpath("//tv.accedo.xdk.dishtv:id/title") #remove
            self.driver.find_element_by_xpath("")
            self.driver.find_element_by_xpath("//android.view.View[contains(@text,'Enjoy live TV on any device,anywhere on the property')]") #remove message
            self.driver.find_element_by_xpath("//android.view.View[contains(@text,'Enjoy live TV on any device, anywhere on the property ")
            self.driver.find_element_by_xpath("//android.view.View[contains@text,'Home')]")
            self.driver.find_element_by_xpath("//android.View.View[contains@text,'@resourceid 'Featured Channels')]")
            self.driver.find_element_by_xpath("//android.View.View[contains@text,")
            self.driver.find_element_by_xpath("//android.View.View[contains@text,'@resouceid 'tv.accedo.xdk.dishtv:id/program_image'") #program letters




            self.driver.find_element_by_xpath("//android.widget.Image[contains(@text,Dish Logo')]")
            self.driver.find_element_by_xpath("//android.widget.Image[contains(@text,Dish Logo')]")
            self.driver.find_element_by_xpath("//android.widget.Image[contains(@text,'Dish Logo')]")
            self.driver.find_element_by_xpath("//android.widget.Image[contains(@text,'")
            self.driver.find_element_by_xpath("//android.widget.Image[contains(@text")
            self.driver.find_element_by_xpath("android.widget.Image[contains@text,ENABLE LARGE FONT SIZE'")
            self.driver.find_element_by_xpath("//android.widget.Image[contains@text,'Dish Logo')]")
            self.driver.find_element_by_xpath("//android.widget.Image[contains@text,'Time remaining')]")
            self.driver.find_element_by_xpath("//android.widget.Image[contains@text,'False Widget')]")
            self.driver.find_element_by_xpath("//android.widget.Image[contains@text,'@resourceiid 'tv.accedo.xdk.dishtv:id/faqs')]")
            self.driver.find_element_by_xpath("//android.widget.Image[contains@text,'Dish Remove')]")
            self.driver.find_element_by_xpath("//android.widget.Image[[80,160][1840,1080]") # the 5/2 game
            self.driver.find_element_by_xpath("//android.widget.Image[contains@text,Dish Logo')]") # NHL sports logo eagle
            self.driver.find_element_by_xpath("//android.widget.Image[contains@text,Dish Logo')]") #NHL sports eagle drop
            self.driver.find_element_by_xpath("//android.widget.Image[contains@text @bounds-")
        except NoSuchElementException as e:
            self.driver.save_screenshot("//android.widget.Image[contains(bounds,'[204,678,612,283']")
            self.driver.save_screenshot("//andrdoid.widget.Image[contains(bounds,'[205,789.431.298']")
            self.driver.save_screenshot("//android.widget.Image[contains") #remove bounds
            self.driver.save_screenshot("//android.Widget.Image[contains") #left bounds
            self.driver.find_element_by_xpath("//android.Widget.Image[contins@resource-id, tv.accedo.xdk.dishtv:id/error_title") # content uavaiable screen


            self.driver.save_screenshot("//androisd.widget.Image[contains")#remove left bounds

        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t
    def test_text_displayed(self):
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'MOST POPULAR CHANNELS')]")\
                .is_displayed()  # popular
            self.driver.find_element_by_xpath("//android.view.View[containts(")
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'WANT MORE CHANNELS, "
                                              "A DVR, OR ADDITIONAL FEATURES?')]").is_displayed()  # banner1
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'CALL 866-794-6166')]")\
                .is_displayed()  # banner2
            self.driver.find_element_by_xpath("")
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'www.dish.com/fiber')]")\
                .is_displayed()  # banner3
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[585,534][672,574]')]")\
                .is_displayed()  # on1
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1113,534][1200,574]')]")\
                .is_displayed()  # on2
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1641,534][1728,574]')]")\
                .is_displayed()  # on3
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t

    def test_button_displayed(self):
        try:
            time.sleep(10)
            self.driver.press_keycode(22)
            time.sleep(5)
            self.driver.press_keycode(20)
            time.sleep(3)
            self.driver.press_keycode(23)
            time.sleep(3)
            self.driver.press_keycode(23)
            print("Sleep over")
            ##self.driver.find_element_by_xpath("//*[resource-id='tv.accedo.xdk.dishtv:id/tv_guide')").is_displayed()  # tv guide
            ##t = self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'tv.accedo.xdk.dishtv:id/home')]")  # home click
            ##print(t.text)
            ##time.sleep(5)
            ##p = self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'tv.accedo.xdk.dishtv:id/tv_guide')]")  # tv guide click
            ##self.driver.find_element(By.XPATH, "//*[contains(@resource")
            ##guide = ActionChains(self.driver).click(p)
            ##guide.perform()
            ##time.sleep(5)
            ##time.sleep(5)
            ##self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[312,51][430,110]')]").click() #trying bounds
            ##time.sleep(3)
            time.sleep(5)
            ##self.driver.find_element_by_xpath("//android.view.View[contains(android.widget.TextView")
            ##self.driver.find_element_by_xpath("//android.widget.Textview[contains(@text,'Tv Guide')]").click() # old code
            ##self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'tv.accedo.xdk.dishtv:id/on_demand')]").click()  # tv guide click
            ##time.sleep(30)
            ##self.driver.find_element_by_xpath("//*[@resource-id='tv_guide']").click()# tv guide click
            ##time.sleep(30)
            '''self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id, 'tv.accedo.xdk.dishtv:id/tv_guide')]").click() #remove click
            self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id, 'tv-guide')]")
            self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id, 'tv-guide')]")
            self.driver.find_element_by_xpath("//android.view.View[contains@resource-id,'tv-guide')]")
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1792,49][1859,105]')]")\
                .is_displayed()  # setting
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'VIEW FULL TV GUIDE')]")\
                .is_displayed()  # full_guide
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[192,805][672,886]')]")\
                .is_displayed()  # live1
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[720,805][1200,886]')]")\
                .is_displayed()  # live2
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1248,805][1728,886]')]")\
                .is_displayed()  # live3 '''
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t 


    def test_button_clickable(self):
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id, 'home')]")\
                .is_enabled()  # home
            self.driver.find_element_by_xpath("tv.accedo.xdk.dishtv:idtv_guide")
            self.driver.find_element_by_xpath("")
            self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id, 'tv-guide')]")\
                .is_enabled()  # guide
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1792,49][1859,105]')]")\
                .is_enabled()  # setting
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'VIEW FULL TV GUIDE')]")\
                .is_enabled()  # full_guide
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[192,805][672,886]')]")\
                .is_enabled()  # live1
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[720,805][1200,886]')]")\
                .is_enabled()  # live2
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1248,805][1728,886]')]")\
                .is_enabled()  # live3
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t


@pytest.mark.usefixtures("setup", "directory")
class TestGuideScreen:
    def test_images_displayed(self):
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(
            (By.XPATH, "//android.view.View[contains(@text, 'VIEW FULL TV GUIDE')]")))
        self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id, 'tv-guide')]").click()
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(
            (By.XPATH, "//android.view.View[contains(@resource-id, 'tv-guide')]")))
        try:
            self.driver.find_element_by_xpath("//android.widget.Image[contains(@text, 'Dish Logo')]")\
                .is_displayed()  # dish
            self.driver.find_element_by_xpath("//android.widget.Image[contains(@text, 'Infio Whites')]")\
                .is_displayed()  # fiber
            self.driver.find_element_by_xpath("//android.widget.Image[contains(@bounds, '[332,366][359,392]')]")\
                .is_displayed()  # info
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,299][318,429]')]")\
                .is_displayed()  # logo1
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,429][318,559]')]")\
                .is_displayed()  # logo2
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,559][318,689]')]")\
                .is_displayed()  # logo3
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,689][318,819]')]")\
                .is_displayed()  # logo4
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,819][318,949]')]")\
                .is_displayed()  # logo5
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,949][318,1076]')]")\
                .is_displayed()  # logo6
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t

    def test_text_displayed(self):
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'TODAY')]")\
                .is_displayed()  # today
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[326,224][678,279]')]")\
                .is_displayed()  # time1
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1030,224][1382,279]')]")\
                .is_displayed()  # time2
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1734,224][1920,279]')]")\
                .is_displayed()  # time3
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'MORE INFO')]")\
                .is_displayed()  # info
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'ON NOW')]")\
                .is_displayed()  # on
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t

    def test_button_displayed(self):
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id, 'tv-guide')]")\
                .is_displayed()  # guide
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1792,49][1859,105]')]")\
                .is_displayed()  # setting
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'ON NOW')]")\
                .is_displayed()  # on
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t

    def test_button_clickable(self):
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id, 'tv-guide')]")\
                .is_enabled()  # guide
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1792,49][1859,105]')]")\
                .is_enabled()  # setting
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'ON NOW')]")\
                .is_enabled()  # on
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t


@pytest.mark.usefixtures("setup", "directory")
class TestSideScreen:
    def test_images_displayed(self):
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(
            (By.XPATH, "//android.view.View[contains(@text, 'VIEW FULL TV GUIDE')]")))
        self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id, 'tv-guide')]").click()
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(
            (By.XPATH, "//android.view.View[contains(@text, 'TODAY')]")))
        self.driver.find_element_by_xpath("//android.view.View[contains(@bounds,'[369,369][471,390]')]").click()
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(
            (By.XPATH, "//android.view.View[contains(@bounds, '[1170,0][1920,1080]')]")))
        try:
            """self.driver.find_element_by_xpath("//android.widget.Image[contains(@text, 'KWGN-DT')]")
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1203,148][1837,502]')]")"""
            self.driver.find_element_by_xpath("//android.widget.Image[contains(@text, 'Dish Logo')]")\
                .is_displayed()  # dish
            self.driver.find_element_by_xpath("//android.widget.Image[contains(@text, 'Infio Whites')]")\
                .is_displayed()  # fiber
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,299][318,429]')]")\
                .is_displayed()  # logo1
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,429][318,559]')]")\
                .is_displayed()  # logo2
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,559][318,689]')]")\
                .is_displayed()  # logo3
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,689][318,819]')]")\
                .is_displayed()  # logo4
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,819][318,949]')]")\
                .is_displayed()  # logo5
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[0,949][318,1076]')]")\
                .is_displayed()  # logo6
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t

    def test_text_displayed(self):
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1228,688][1862,1051]')]")\
                .is_displayed()  # info
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'ON NOW')]")\
                .is_displayed()  # on
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, 'TODAY')]")\
                .is_displayed()  # today
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[326,224][678,279]')]")\
                .is_displayed()  # time1
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1030,224][1382,279]')]")\
                .is_displayed()  # time2
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t

    def test_button_displayed(self):
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, ' WATCH LIVE')]")\
                .is_displayed()  # watch
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t

    def test_button_clickable(self):
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@text, ' WATCH LIVE')]")\
                .is_enabled()  # watch
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t


@pytest.mark.usefixtures("setup", "directory")
class TestSettingScreen:
    def test_images_displayed(self):
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(
            (By.XPATH, "//android.view.View[contains(@text, 'VIEW FULL TV GUIDE')]")))
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@bounds, '[1792,49][1859,105]')]").click()
            self.driver.find_element_by_xpath("//android.widget.Image[contains(@text, 'Dish Logo')]")\
                .is_displayed()  # dish
            self.driver.find_element_by_xpath("//android.widget.Image[contains(@text, 'Infio Whites')]")\
                .is_displayed()  # fiber
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t

    def test_text_displayed(self):
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id, 'informationPanel')]")\
                .is_displayed()  # info1
            subprocess.run(['adb', 'shell', 'input', 'keyevent', '20'])
            self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id, 'informationPanel')]")\
                .is_displayed()  # info2
        except NoSuchElementException as e:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("Element could not be found! Please view the Screenshot!") from e
        except TimeoutException as t:
            self.driver.save_screenshot(self.direct + self.name + ".png")
            raise Exception("The test timed out! Please view the Screenshot!") from t 


def teardown_module(module):
    subprocess.call(['python3', 'EventDataParser.py'])
    subprocess.call(['python3', 'OnStreamMoveFiles.py'])
    return module
