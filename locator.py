from selenium.webdriver.common.by import By


class MainPageLocators(object):
    CALENDAR_INPUT = (By.XPATH,
                      '/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form['
                      '1]/div[1]/div[1]/div[3]/div[1]/input[1]')
    DURATION_INPUT = (By.XPATH,
                      '/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form['
                      '1]/div[1]/div[1]/div[4]/div[1]/div[1]')

    EXTRA_PARAMETERS = (By.XPATH, '//div[contains(text(),\'Papildomi parametrai\')]')
    DURATION_WINDOW = (By.CLASS_NAME, 'nights-range-picker')

    SELECTED_DURATION = (By.XPATH,
                         '//body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div['
                         '1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[10]/span[1]')
    MIN_EUR = (By.XPATH,
               '/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div['
               '3]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]')

    MAX_EUR = (By.XPATH,
               '/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div['
               '3]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]')

    SPAM = (By.XPATH, '//body/div[@id=\'PopupSignupForm_0\']/div[2]/div[1]')
    LOADING_BAR = (By.XPATH, '//body/div[@id=\'content\']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]')
    SEARCH_BTN = (By.XPATH, '//button[contains(text(),\'Ieškoti\')]')

    STARS = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form['
                       '1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div['
                       '1]/div[5]')

    SPAM = (By.XPATH, '//body/div[@id=\'PopupSignupForm_0\']/div[2]/div[1]')
    MORE_BTN = (By.XPATH, '//body/div[@id=\'content\']/div[1]/div[3]/div[2]/div[2]/div[1]/div[5]/img[1]')


class CalendarLocators(object):
    ARROW_CALENDAR = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div['
                                '2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/table['
                                '2]/thead[1]/tr[1]/th[3]/span[1]')

    CALENDAR_BOX = (By.CLASS_NAME, 'date-picker-wrapper')
    MONTH = (By.CLASS_NAME, 'month1')

    DAY_LOCATION = (By.XPATH, '//body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form['
                              '1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody['
                              '1]/tr[5]/td[6]/div[1]/span[1]')


class HotelLocators(object):
    HOTEL_CONTAINER = (By.ID, 'itemBox')
    HOTEL_LIST = (By.CLASS_NAME, 'hotel_point')
