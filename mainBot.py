import re
from selenium import webdriver
import time
import pandas as pd
from utils import Utils
from selenium.webdriver import ChromeOptions
import page


class HotelGetter:
    def __init__(self):
        self.utils = Utils()
        self.working_dir = self.utils.get_current_dir()
        self.options = ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(self.working_dir / 'chromedriver.exe', options=self.options)
        self.driver.get('https://www.teztour.lt/')
        self.xls_data = self.read_csv()
        self.hotel_dict = {'Name': [], 'Price': [], 'Info': [], 'Updated': []}
        self.discount_df = pd.DataFrame

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
        discount_df = self.check_if_hotel_discounted()
        if discount_df is not None:
            self.discount_df = discount_df
            self.set_and_sort_dicounts()
            self.save_xls('dicounts.xlsx', self.discount_df)

        self.save_xls('hotels_' + str(self.utils.get_current_date()) + '.xlsx', self.hotel_dict)
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

    def save_xls(self, name, final_dict):
        try:
            pd.DataFrame.from_dict(data=final_dict, orient='columns').to_excel(
                name, header=True, index=False, encoding='utf-8-sig')
        except Exception as e:
            print('error due to' + str(e))

    def check_if_hotel_discounted(self):
        if self.xls_data is not None:
            dicount_dict = {'Name': [], 'OLD_Price': [], 'NEW_Price': [], 'Dicount': [], 'Dicount_percent': []}
            try:
                for new_price, name in zip(self.hotel_dict['Price'], self.hotel_dict['Name']):
                    old_price = self.return_change_price(name, new_price)
                    if old_price:
                        print(name + ' ' + old_price + ' >> ' + new_price)
                        dicount_dict['Name'].append(name)
                        dicount_dict['NEW_Price'].append(self.remove_eur_sign_and_to_int(new_price))
                        dicount_dict['OLD_Price'].append(self.remove_eur_sign_and_to_int(old_price))
                        dicount_dict['Dicount'].append(
                            self.remove_eur_sign_and_to_int(old_price) - self.remove_eur_sign_and_to_int(new_price))
                        dicount_dict['Dicount_percent'].append(None)
            except KeyError:
                pass
            return pd.DataFrame.from_dict(dicount_dict)
        return None

    def return_change_price(self, name, price):
        try:
            filt = self.xls_data['Name'] == name
            price_xls_with_eur = self.xls_data.loc[filt, 'Price'].values[0]
            price_xls = self.remove_eur_sign_and_to_int(price_xls_with_eur)
            price = self.remove_eur_sign_and_to_int(price)
            if price < price_xls:
                return price_xls_with_eur
        except (KeyError, IndexError) as e:
            return None
        return None

    def remove_eur_sign_and_to_int(self, price):
        return int(re.sub(r'[^\w]', '', price))

    def set_and_sort_dicounts(self):
        self.discount_df.sort_values(by=['Dicount', 'OLD_Price'], ascending=[False, False], inplace=True)
        self.discount_df['Dicount_percent'] = (self.discount_df['Dicount'] / self.discount_df['OLD_Price'] * 100)


if __name__ == '__main__':
    main = HotelGetter()
    main.gather_hotels()
