import re
from selenium import webdriver
import time
import pandas as pd
from utils import Utils
from selenium.webdriver import ChromeOptions
import page


class HotelGetter():
    def __init__(self):
        utils = Utils()
        self.working_dir = utils.get_current_dir()
        self.options = ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(self.working_dir / 'chromedriver.exe', options=self.options)
        self.driver.get('https://www.teztour.lt/')
        self.xls_data = self.read_csv()
        self.hotel_dict = {'Name': [], 'Price': [], 'Info': [], 'Updated': []}

    def gather_hotels(self):
        time.sleep(2)
        main_page = page.MainPage(self.driver)
        main_page.fill_calendar()
        main_page.open_more_options()
        main_page.fill_duration()
        main_page.min_price = '900'
        main_page.max_price = '1650'
        main_page.select_stars()
        main_page.click_search()

        hotel_page = page.HotelPage(self.driver)
        hotel_page.wait_to_load()
        self.hotel_dict = hotel_page.fill_hotels()
        self.check_if_hotel_discounted()
        self.save_xls()
        print('done')
        self.driver.quit()

    def read_csv(self):
        data = None
        try:
            data = pd.read_excel(self.working_dir / 'hotels.xlsx')
            print('file red')
        except Exception as e:
            print('error due to' + str(e))
        return data

    def save_xls(self):
        try:
            pd.DataFrame.from_dict(data=self.hotel_dict, orient='columns').to_excel(
                'hotels.xlsx', header=True, index=False, encoding='utf-8-sig')
        except Exception as e:
            print('error due to' + str(e))

    def check_if_hotel_discounted(self):
        if self.xls_data is not None:
            try:
                for price, name in zip(self.hotel_dict['Price'], self.hotel_dict['Name']):
                    new_price = self.return_reduced_price(name, price)
                    if new_price:
                        print(name + ' ' + new_price + ' >> ' + price)
            except KeyError:
                pass

    def return_reduced_price(self, name, price):
        try:
            filt = self.xls_data['Name'] == name
            price_xls_with_eur = self.xls_data.loc[filt, 'Price'].values[0]
            price_xls = re.sub(r'[^\w]', '', price_xls_with_eur)
            price = re.sub(r'[^\w]', '', price)
            if int(price) < int(price_xls):
                return price_xls_with_eur
        except (KeyError, IndexError) as e:
            return None
        return None


if __name__ == '__main__':
    main = HotelGetter()
    main.gather_hotels()
