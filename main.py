# import selenium
from selenium import webdriver
import time

five_seconds_from_now = time.time() + 5
SECONDS_IN_MINUTE = 60
FIVE_MINUTES_FROM_NOW = time.time() + (SECONDS_IN_MINUTE * 5)

chrome_driver_path = 'type chrome driver path here'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

total_cookies_accumulated = 0

driver.get(url='http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id(id_='cookie')

all_children_divs = driver.find_elements_by_css_selector(css_selector='#store > *')

id_attribute_values = [
    all_children_divs[children_div_index].get_attribute(name='id')
    for children_div_index
    in range(len(all_children_divs) - 1)
]
# print(id_attribute_values)

while True:
    if time.time() >= FIVE_MINUTES_FROM_NOW:
        cookies_per_second = driver.find_element_by_id(id_='cps').text
        print(cookies_per_second)
        break
    cookie.click()
    # total_cookies_accumulated += 1
    total_cookies_accumulated = int(driver.find_element_by_id(id_='money').text.replace(',', ''))
    # print(total_cookies_accumulated)
    if time.time() >= five_seconds_from_now:
        for id_attribute_value in id_attribute_values[::-1]:
            if total_cookies_accumulated < int(driver.find_element_by_xpath(
                    xpath='//*[@id="{id}"]/b'
                    .format(id=id_attribute_value)).text.split()[-1].replace(',', '')):
                # print(id_attribute_value)
                continue
            if driver.find_element_by_id(id_=id_attribute_value).get_attribute(name='class') == 'grayed':
                continue
            total_cookies_accumulated -= int(driver.find_element_by_xpath(
                    xpath='//*[@id="{id}"]/b'.format(id=id_attribute_value)
                ).text.split()[-1].replace(',', ''))
            # print(total_cookies_accumulated)
            driver.find_element_by_id(id_=id_attribute_value).click()
            # print(id_attribute_value)
            five_seconds_from_now = time.time() + 5
            break

# # print(total_cookies_accumulated)
# cookies_per_second = driver.find_element_by_id(id_='cps').text
# print(cookies_per_second)

# driver.quit()
