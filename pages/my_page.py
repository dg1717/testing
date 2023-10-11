from pages.base_page import BasePage


class MyPage(BasePage):

    @property
    def page_title(self):
        return self.driver.title