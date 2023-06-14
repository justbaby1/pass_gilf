from selenium  import webdriver

#实例化webdriver
class Webdriver(object):
    __driver = None
    @classmethod
    def get_webdriver(cls):
        if cls.__driver is None:
           cls.__driver = webdriver.Chrome()
           cls.__driver.get("****")
           cls.__driver.maximize_window()
           cls.__driver.implicitly_wait(10)
        return cls.__driver
