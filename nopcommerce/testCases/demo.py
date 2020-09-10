from selenium import webdriver
import time


class TestVoltageUI:

    def __int__(self, driver):
        self.driver = driver

    def load_ui_page(self, driver):
        self.driver = driver
        print("driver is ",self.driver)
        self.driver.get("http://localhost:4200/#/login")
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    def verify_page_title(self, title):
        login_page_title = 'Voltage SecureData'

        if login_page_title == title:
            return True
        else:
            return False

    def get_last_value(self, current_url):
        url = current_url
        last_value = url.split('/')[-1]
        return last_value

    def login(self, driver):
        self.driver = driver
        page_title = self.driver.title
        flag = self.verify_page_title(page_title)

        if flag:
            print("Title Found : ", self.driver.title)
            print("Current URL : ", self.driver.current_url)
            print("----------------------------------------------")
            last_value = self.get_last_value(self.driver.current_url)
            if last_value == 'login':
                self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("admin")
                self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("voltage123")

                login_button_xpath = self.driver.find_element_by_xpath('//div[2]/div[2]/form/div[3]/button')
                login_button_enabled = login_button_xpath.is_enabled()

                if login_button_enabled:
                    login_button_xpath.click()
                    time.sleep(5)

                    cur_url = self.driver.current_url
                    print("Current URL : ", self.driver.current_url)
                    print("----------------------------------------------")
                    last_value = self.get_last_value(cur_url)
                    if last_value == 'home':
                        print('*****Login Successful*****')

                        mini_maxi_xpath = self.driver.find_element_by_xpath('//div[1]/ux-side-menu/button')
                        mini_maxi_xpath.click()
                        time.sleep(4)
                        mini_maxi_xpath.click()
                        time.sleep(4)

                        key_management_xpath = self.driver.find_element_by_xpath('//ux-side-menu/div/ux-side-menu-item[2]/button')
                        key_management_xpath.click()
                        time.sleep(4)

                        key_rotation_group_xpath = self.driver.find_element_by_xpath('//ux-side-menu-item[2]/div/ux-side-menu-item[2]/button')
                        key_rotation_group_xpath.click()
                        time.sleep(4)

                        client_policy_settings_xpath = self.driver.find_element_by_xpath('//ux-side-menu-item[2]/div/ux-side-menu-item[3]/button')
                        client_policy_settings_xpath.click()
                        time.sleep(4)

                        data_protection_settings_xpath = self.driver.find_element_by_xpath('//div[1]/ux-side-menu/div/ux-side-menu-item[3]/button')
                        data_protection_settings_xpath.click()
                        time.sleep(4)

                        authentication_settings = self.driver.find_element_by_xpath('//div[1]/ux-side-menu/div/ux-side-menu-item[4]/button')
                        authentication_settings.click()
                        time.sleep(4)

                        authentication_settings_methods_xpath = self.driver.find_element_by_xpath('//ux-side-menu-item[4]/div/ux-side-menu-item[2]/button')
                        authentication_settings_methods_xpath.click()
                        time.sleep(4)

                        pie_xpath = self.driver.find_element_by_xpath('//div[1]/ux-side-menu/div/ux-side-menu-item[5]/button')
                        pie_xpath.click()
                        time.sleep(4)

                        administration_xpath = self.driver.find_element_by_xpath('//div[1]/ux-side-menu/div/ux-side-menu-item[6]/button')
                        administration_xpath.click()
                        time.sleep(4)

                        administration_authentication_methods_xpath = self.driver.find_element_by_xpath('//ux-side-menu-item[6]/div/ux-side-menu-item[2]/button')
                        administration_authentication_methods_xpath.click()
                        time.sleep(4)

                        administration_backup_xpath = self.driver.find_element_by_xpath('//ux-side-menu-item[6]/div/ux-side-menu-item[3]/button')
                        administration_backup_xpath.click()
                        time.sleep(4)

                        administration_restore_xpath = self.driver.find_element_by_xpath('//ux-side-menu-item[6]/div/ux-side-menu-item[4]/button')
                        administration_restore_xpath.click()
                        time.sleep(4)

                        key_management_xpath.click()
                        time.sleep(4)

                        key_management_district_xpath = self.driver.find_element_by_xpath('//ux-side-menu-item[2]/div/ux-side-menu-item[1]/button')
                        key_management_district_xpath.click()
                        time.sleep(4)

                        new_district = self.driver.find_element_by_xpath('//div[2]/ux-side-menu-content/sd-district//div/button[1]')
                        new_district.click()
                        time.sleep(4)

                        new_district_ok = self.driver.find_element_by_xpath('//modal-container//sd-modal-content/div[2]/div/div[3]/button[1]')
                        new_district_ok.click()
                        time.sleep(4)

                        delete_district = self.driver.find_element_by_xpath('//table/tbody/tr[2]/td[5]/button[2]')
                        delete_district.click()
                        time.sleep(4)

                        delete_confirmation = self.driver.find_element_by_xpath('//sd-modal-content/div[2]/div[2]/div[3]/ux-checkbox/label/span')
                        delete_confirmation.click()
                        time.sleep(3)

                        delete_button = self.driver.find_element_by_xpath('//sd-modal-content/div[2]/div[2]/div[3]/button[1]')
                        delete_button.click()
                        time.sleep(3)

                        data_protection_settings_xpath.click()
                        time.sleep(3)

                        all_formats = self.driver.find_element_by_xpath('//*[@id="ux-tab-14"]/span')
                        all_formats.click()
                        time.sleep(2)

                        credit_formats = self.driver.find_element_by_xpath('//*[@id="ux-tab-15"]/span')
                        credit_formats.click()
                        time.sleep(2)

                        social_security_number = self.driver.find_element_by_xpath('//*[@id="ux-tab-16"]/span')
                        social_security_number.click()
                        time.sleep(2)

                        variable_length_string = self.driver.find_element_by_xpath('//*[@id="ux-tab-17"]/span')
                        variable_length_string.click()
                        time.sleep(2)

                        specified_format_string = self.driver.find_element_by_xpath('//*[@id="ux-tab-18"]/span')
                        specified_format_string.click()
                        time.sleep(2)

                        date_xpath = self.driver.find_element_by_xpath('//*[@id="ux-tab-19"]/span')
                        date_xpath.click()
                        time.sleep(2)

                        number_xpath = self.driver.find_element_by_xpath('//*[@id="ux-tab-20"]/span')
                        number_xpath.click()
                        time.sleep(2)

                        home = self.driver.find_element_by_xpath('//div[1]/ux-side-menu/div/ux-side-menu-item[1]/button')
                        home.click()
                        time.sleep(2)

                    else:
                        print("XXXXX-Login Failed-XXXXX")
                else:
                    print("Waiting for login button to enable...")
            else:
                print("URL is not correct")
        else:
            print("Title of the page not valid")

        self.driver.close()

if __name__ == '__main__':
    driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")
    obj = TestVoltageUI()
    obj.load_ui_page(driver)
    obj.login(driver)



