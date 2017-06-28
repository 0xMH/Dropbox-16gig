from selenium import webdriver

class sing_up:
    def __init__(self, link):
        self.driver = webdriver.Firefox()
        self.Referral_ink = link
        self.driver.get(self.Referral_ink)



    def fill(self, xpath2, act, text=None):

        temp = self.driver.find_element_by_xpath(xpath2)
        if act is "write":
            temp.clear()
            temp.send_keys(text)
        else:
            temp.click()

    def close(self):
        return self.driver.close()





