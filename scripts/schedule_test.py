import schedule
import time
import datetime

def job():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print( str(TNOW) +" Print 5 sec interval for 3 times")

def minjob():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print('\n' + str(TNOW) +" This prints every min \n")

schedule.every(1).minutes.do(minjob)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("19:27").do(job)
schedule.every().minute.at(":17").do(job)
schedule.every().minute.at(":05").do(job)
schedule.every().minute.at(":10").do(job)
schedule.every().minute.at(":15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)