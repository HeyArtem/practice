from selenium import webdriver
import time
from auth_data import vk_password
from selenium.webdriver.common.keys import Keys



# авторизируюсь в вк

# options меняю юзер агента
options = webdriver.ChromeOptions()

# то, на что меняю
# options.add_argument('user-agent=HelloTemka!!! ;-)')
options.add_argument('User-Agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0')

# инициализируем браузер
driver = webdriver.Chrome(
    executable_path='/home/heyartem/PycharmProjects/practice/selenium/web_driver/chromedriver',
    options=options)

try:
    # отправляю браузер на этот адрес VK
    driver.get('https://vk.com/')
    time.sleep(3)

    # нахожу строку ввода майла
    email_input = driver.find_element_by_id('index_email')

    # очищаю это поле
    email_input.clear()

    # вводим данные в эту строку
    email_input.send_keys('89164406110')

    # пауза
    time.sleep(2)

    # нахожу строку ввода пароля
    pasword_input = driver.find_element_by_id('index_pass')

    # очищаю поле
    pasword_input.clear()

    # ввожу пароль
    pasword_input.send_keys(vk_password)
    time.sleep(2)

    # I вар: кликаем по кнопке
    # нахожу кнопку по id  и вызываю метод clik
    login_button = driver.find_element_by_id('index_login_button').click()
    time.sleep(3)

    # # II вар. авторизуюсь нажав ENTER
    # # для этого импортну (from selenium.webdriver.common.keys import Keys)
    # pasword_input.send_keys(Keys.ENTER)
    # # enter+clik on ENTER выведет другие клавиши, ИХ МНОГО
    # time.sleep(10)


    # кликаю на мою страницу
    news_link = driver.find_element_by_id('l_pr').click()

    time.sleep(10)










except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()