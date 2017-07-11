

class EdgeSupport(object):

    @staticmethod
    def click_element_by_id(driver, elem_id):
        driver.execute_script("document.getElementById('{}').click()".format(elem_id))
