from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import *
from utils import Utils
from element import BasePageElement


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MinPriceElement(BasePageElement):
    locator = (By.NAME, 'tourMinPrice')


class MaxPriceElement(BasePageElement):
    locator = (By.NAME, 'tourMaxPrice')


class MainPage(BasePage):
    min_price = MinPriceElement()
    max_price = MaxPriceElement()
    day = ''
    month = ''

    def fill_calendar(self):
        self.driver.find_element(*MainPageLocators.CALENDAR_INPUT).click()
        calendar_box = self.driver.find_element(*CalendarLocators.CALENDAR_BOX)
        while self.month not in self.driver.find_element(By.CSS_SELECTOR, '.month1 .month-name').text:
            calendar_box.find_element(*CalendarLocators.ARROW_CALENDAR).click()

        for day in calendar_box.find_elements(By.CSS_SELECTOR, '.flight-date'):
            if day.text == self.day:
                day.click()

    def fill_duration(self):
        self.driver.find_element(*MainPageLocators.DURATION_INPUT).click()
        duration_window = self.driver.find_element(*MainPageLocators.DURATION_WINDOW)
        duration_window.find_element(*MainPageLocators.SELECTED_DURATION).click()

    def click_search(self):
        self.driver.find_element(*MainPageLocators.SEARCH_BTN).click()

    def select_stars(self):
        self.driver.find_element(*MainPageLocators.STARS).click()

    def open_more_options(self):
        self.driver.find_element(*MainPageLocators.EXTRA_PARAMETERS).click()


class HotelPage(BasePage):

    def check_exists_by_link(self, text):
        try:
            self.driver.find_element_by_link_text(text)
        except NoSuchElementException:
            return False
        return True

    def wait_to_load(self):
        close_spam = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(
            MainPageLocators.SPAM))
        close_spam.click()

        WebDriverWait(self.driver, 40).until(EC.invisibility_of_element_located(
            MainPageLocators.LOADING_BAR))

        while self.check_exists_by_link('Daugiau'):
            load_more = self.driver.find_element_by_link_text('Daugiau')
            load_more.click()
            WebDriverWait(self.driver, 40).until(EC.invisibility_of_element_located(
                MainPageLocators.MORE_BTN))

    def fill_hotels(self):
        utills = Utils()
        today_date = utills.get_current_date()
        self.driver.find_element(*HotelLocators.HOTEL_CONTAINER)
        hotels = self.driver.find_elements(*HotelLocators.HOTEL_LIST)
        hotel_dict = {'Name': [], 'Price': [], 'Info': [], 'Updated': []}
        for hotel in hotels:
            name = hotel.find_element_by_class_name('h5')
            hotel_name = name.find_element_by_tag_name('a').text
            hotel_dict['Name'].append(hotel_name)
            price = hotel.find_element_by_class_name('eur-currency').text
            hotel_dict['Price'].append(price)
            leave_date = hotel.find_element_by_class_name('type').text
            hotel_dict['Info'].append(leave_date)
            hotel_dict['Updated'].append(today_date)
        return hotel_dict

