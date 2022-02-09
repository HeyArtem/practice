from selenium import webdriver
import time
from auth_data import vk_password, username


# войду в инстаграмм

# options меняю юзер агента
options = webdriver.FirefoxOptions()

# то, на что меняю (почему стал  set_arguments&)
options.set_preference( ,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')

# инициализируем браузер
driver = webdriver.Firefox(
    executable_path='/home/heyartem/PycharmProjects/practice/selenium/web_driver_fireFox/geckodriver',
    options=options)

try:
    driver.get('https://www.instagram.com/')
    time.sleep(5)

    # нахожу строку для ввода имени, испоьлзую поиск ячейки по имени
    username_input = driver.find_element_by_name('username')
    username_input.clear()
    username_input.send_keys(username)
    time.sleep(5)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()