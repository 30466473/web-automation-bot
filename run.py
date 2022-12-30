import time
import datetime
from booking.book import Booking

target_date = datetime.datetime.now() + datetime.timedelta(days=6)
target_date_formatted = target_date.strftime('%Y-%m-%d')

with Booking() as bot:
    bot.land_first_page()
    bot.set_username(bot.get_username())
    bot.set_password(bot.get_password())
    if (bot.next_month()):
        bot.select_month()
    bot.select_date(date = target_date_formatted)
    bot.select_time(time_court = "2200|2300|2")
    bot.book_submit()
    time.sleep(150000)