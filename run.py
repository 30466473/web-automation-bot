import time

from booking.book import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.user_name('kevinyan13')
    bot.pass_word('Kejiji@94629')
    # bot.select_month()
    bot.select_date(date = "2022-12-29")
    bot.select_time(time_court = "1800|1900|2")
    bot.book_submit()
    time.sleep(5)