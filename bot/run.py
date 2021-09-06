from booking.booking import Booking

# instance = Booking()
# instance.land_on_first_page()


# usage of a context manager
with Booking() as bot:
    bot.land_on_first_page()
    bot.change_currency(currency='EUR')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2021-09-20',
                     check_out_date='2021-10-25')
    bot.select_adults(10)
    bot.click_search()
    bot.apply_filters()
