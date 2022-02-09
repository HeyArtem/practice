import schedule, time

# pip install schedule
# https://tirinox.ru/send-bitcoin-over-python/

def job(p):
    print(f'Эта функция работает: {p}')
    
#every () Без параметров задание по умолчанию выполняется один раз в секунду / минуту / час
schedule.every(10).seconds.do(job, p='Каждые 10 секунд!!')
schedule.every(10).minutes.do(job, p='Каждую минуту')
schedule.every().hour.do(job, p='Каждый час')

schedule.every().day.at("10:30").do(job, p="Выполнять задачу каждые день в 10:30")
schedule.every().monday.do(job, p="Выполнять задачу каждый понедельник")
schedule.every().wednesday.at("10:30").do(job, "Выполнять задачу каждую среду в 10:30")


schedule.every(5).to(10).seconds.do(job, p="В случайное время м/у 5 и 10 секундами")


while True:
    
    # запустить все задачи, которые можно запустить
    schedule.run_pending()
    
    # спать в течении одной секунды
    time.sleep (1) #ЗАЧЕМ ЭТОТ ПАРАМЕТР?? От его значения ни чего не меняетс
