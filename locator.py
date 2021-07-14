from selenium.webdriver.common.by import By


class MainPageLocators(object):
    CALENDAR_INPUT = (By.CSS_SELECTOR, '.calendar-container.select_container')
    DURATION_INPUT = (By.XPATH, '//*[@id="nights-control"]/div/div[1]/div')
    EXTRA_PARAMETERS = (By.XPATH, '//div[contains(text(),\'Papildomi parametrai\')]')
    DURATION_WINDOW = (By.CLASS_NAME, 'nights-range-picker')
    SELECTED_DURATION = (By.XPATH, '//*[@id="nights-control"]/div/div[2]/div/div/div[10]/span')
    SPAM = (By.XPATH, '//body/div[@id=\'PopupSignupForm_0\']/div[2]/div[1]')
    LOADING_BAR = (By.XPATH, '//*[@id="progresSearch"]/div[1]/div[1]')
    SEARCH_BTN = (By.XPATH, '//button[contains(text(),\'Ieškoti\')]')
    STARS = (By.CSS_SELECTOR, 'div.empty-star.star5')
    SPAM = (By.XPATH, '//body/div[@id=\'PopupSignupForm_0\']/div[2]/div[1]')
    MORE_BTN = (By.XPATH, '//body/div[@id=\'content\']/div[1]/div[3]/div[2]/div[2]/div[1]/div[5]/img[1]')


class CalendarLocators(object):
    ARROW_CALENDAR = (By.CSS_SELECTOR, '.month2 .next')
    CALENDAR_BOX = (By.CLASS_NAME, 'date-picker-wrapper')
    MONTH = (By.CLASS_NAME, 'month1')
    DAY_LOCATION = (By.XPATH, '//span[text()=\'6\']')


class HotelLocators(object):
    HOTEL_CONTAINER = (By.ID, 'itemBox')
    HOTEL_LIST = (By.CLASS_NAME, 'hotel_point')
