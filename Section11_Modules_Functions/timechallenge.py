#!/usr/bin/env python3

"""
Create a program that allows a user to choose one of
up to 9 time zones from a menu. You can choose any
zones you want from the all_timezones list.

The program will then display the time in that timezone, as
well as local time and UTC time.

Entering 0 as the choice will quit the program.

Display the dates and times in a format suitable for the
user of your program to understand, and include the
timezone name when displaying the chosen time.
"""

import datetime
import pytz

available_tz = {'1': 'Africa/Johannesburg',
                '2': 'America/Anchorage',
                '3': 'America/Los_Angeles',
                '4': 'America/New_York',
                '5': 'Asia/Calcutta',
                '6': 'Asia/Tokyo',
                '7': 'Australia/Sydney',
                '8': 'Europe/London',
                '9': 'Europe/Moscow',
                }

while True:
    for place in sorted(available_tz):
        print('{}. {}'.format(place, available_tz[place]))
    # get input
    chosen_tz = input('Choose a timezone (1-9) from the above list or 0 to quit: ')
    if chosen_tz in available_tz.keys():
        display_time = pytz.timezone(available_tz[chosen_tz])
        # time in selected timezone
        tz_time = datetime.datetime.now(tz=display_time)
        # local time
        localtime = datetime.datetime.now()
        # UTC time
        utctime = datetime.datetime.utcnow()
        print('{}: {}'.format(available_tz[chosen_tz], tz_time.strftime('%c %Z')))
        print('Local time: {}'.format(localtime.strftime('%c')))
        print('UTC time: {}'.format(utctime.strftime('%c')))
        print('\n')
    else:
        exit(0)
