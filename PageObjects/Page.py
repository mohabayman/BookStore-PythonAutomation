from PageParts import Header


class Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)
