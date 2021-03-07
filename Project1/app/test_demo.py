from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = 'zs'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.WwMainActivity'
        caps['noReset'] = 'true'
        # 客户端与Appium服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def teardown(self):
        self.driver.quit()

    # def test_daka(self):
    #     '''
    #         前提条件: 已登录状态（ noReset=True）
    #         打卡用例：
    #         1、打开【企业微信】应用
    #         2、进入【工作台】
    #         3、点击【打卡】
    #         4、选择【外出打卡】tab
    #         5、点击【第N次打卡】
    #         6、验证【外出打卡成功】
    #         7、退出【企业微信】应用
    #         :return:
    #         '''
    #     self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup//*[@text='工作台']").click()
    #     # android_uiautomator 里面要用双引号，外面用单引号。
    #     # 向下滑动两次，再向上查找，直到找到元素
    #     self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
    #                              'new UiScrollable(new UiSelector()'
    #                              '.scrollable(true).instance(0))'
    #                              '.scrollIntoView(new UiSelector()'
    #                              '.text("打卡").instance(0));').click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
    #     self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
    #     print(self.driver.page_source)
    #     # sleep(2)
    #     # assert "外出打卡成功" in self.driver.page_source
    #     # 激活隐式等待
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")

    def test_addmember(self):
        '''
        企业添加联系人
                    前提条件: 已登录状态（ noReset=True）
                    打卡用例：
                    1、打开【企业微信】应用
                    2、进入【通讯录】
                    3、点击【添加成员】
                    4、选择【手动输入添加】
                    5、输入【姓名】
                    6、输入【手机号】
                    7、点击【保存】
                    :return:
                    '''
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        sleep(3)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        sleep(3)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b7m").send_keys("zs")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fwi").send_keys("18600000000")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        sleep(3)
        #断言
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
