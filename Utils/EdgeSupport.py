

class EdgeSupport(object):

    @staticmethod
    def click_element(driver, elem):
        driver.execute_script("arguments[0].click()", elem)
