""" week8_slides_p1.py

Codes discussed in class during Week 7, Part 1: the datetime module

IMPORTANT: This code requires the lec_utils module (available in dropbox)

    toolkit/
    |   ...
    |__ webinars/
    |   |__ __init__.py             <- Required (empty file)
    |   |__ lec_utils.py            <- Required
    |   |__ week8_slides_p1.py      <- This module
    |   |__ week8_slides_p2.py      
    |       ...
    |__ toolkit_config.py


I will talk about the `lec_utils.py` module during class

"""
import datetime as dt

from webinars import lec_utils as utils

# Config for this part of the lecture
utils.pp_cfg.sep = True
utils.pp_cfg.show_type = True



# ----------------------------------------------------------------------------
# Notes about datetime and lec_utils 
#
# The datetime module 
#  - datetime.datetime --> class representing both date and time stamps
#  - datetime.timedelta --> class representing duration
# 
# Note that we are importing datetime as dt.  This is useful so we do not
# confuse datetime (the module) with datetime.datetime (the class)
#
#
# Notes about lec_utils.pprint: 
#  - The function pprint is not to be confused with the module pprint (I did
#    this on purpose to illustrate how useful namespaces can be).
#
#  - The only functions from lec_utils we will use are 
#       lec_utils.pprint. 
#       lec_utils.csv_to_df
#       lec_utils.csv_to_fobj
# ----------------------------------------------------------------------------


# ---------------------------------------------------------------------------- 
# The datetime class:
#   Implements several methods to generate instances of `datetime`
#   representing a certain date
# ---------------------------------------------------------------------------- 

# One of the methods implemented by `dt.datetime` is called `now`, which
# returns an instance of `dt.datetime` representing the current date/time.

# Instance of `dt.datetime` with the current date/time
dt_now  = dt.datetime.now()
#print('')
#print( str(dt_now) )
#print( repr(dt_now) )

# How can we print a representation of an object?
#
# repr(obj): 
#   Returns a string containing a printable representation of an object.
#   Typically, there is an attempt to return the string that would
#   generate an object with the same type and value
# 
# str(obj):
#   Returns a string "version" of the object (typically an "informal" printable
#   representation of the object, not necessarily how the object was
#   constructed)
#   

# Let's look at an example using `dt_now`
# First, str(obj)

#print("str(dt.datetime.now()) is:")
#print(str(dt_now))

# NOTE: print(obj) is the same as print(str(obj))
# This means that `obj` is converted to string before printing

# Now, using `repr(obj)`

#print("repr(dt.datetime.now()) is:")
#print(repr(dt_now))
# Note that `dt_now` is an instance of datetime.datetime

# NOTE: How does `lec_utils.pprint` represent objects?
# For non-string objects, set the parameter `pretty`:
#   If pretty = True -> will use `repr` (DEFAULT)
#   If pretty = False -> will use `str`

# Example:
#utils.pprint(dt_now, msg="This is dt_now (pretty=True)", pretty=True)
#utils.pprint(dt_now, msg="This is dt_now (pretty=False)", pretty=False)



# dt_now is an instance of dt.datetime
# Let's take a look at this class using help(dt.datetime)
#help(dt.datetime)


# From the output above, we can see that instances of `datetime` store the
# date (year, month, day) and time (hour, minute, second, microsecond). You
# can access these attributes directly from the instance:
#
#   dt_now.day            
#   dt_now.month          
#   dt_now.year           
#   dt_now.hour           
#   dt_now.minute         
#   dt_now.second         
#   dt_now.microsecond    



# ----------------------------------------------------------------------------
#   Creating datetime.datetime instances
# ----------------------------------------------------------------------------

# Create another datetime instance 

dt0 = dt.datetime(
    year=2022, 
    month=11, 
    day=1, 
    hour=8, 
    minute=0, 
    second=0, 
    microsecond=0)

#utils.pprint(dt0, "dt0 is:\n", pretty=False)


# We do not need to specify all the parameters (year, month, day are required)
dt1 = dt.datetime(
    year=2022,
    month=11,
    day=1,
    hour=8,
)
#utils.pprint(dt1, "dt1 is:\n", pretty=False)
#utils.pprint(dt1.hour, 'dt1.hour')


# ---------------------------------------------------------------------------- 
#   `datetime.timedelta` objects
# ---------------------------------------------------------------------------- 
# Lets create two other datetime instances:
#   dt0 --> 2019-12-31 00:00:00
#   dt1 --> 2020-01-01 00:00:00
dt0  = dt.datetime(2019, 12, 31)
dt1  = dt.datetime(2020, 1, 1)

#utils.pprint(dt0, "dt0 is:\n", pretty=False)
#utils.pprint(dt1, "dt1 is:\n", pretty=False)


# Operations between datetime objects will return timedelta objects
delta  = dt0 - dt1

msg = f"The operation:\n  {repr(dt1)} \n    - {repr(dt0)}\ngives:"
#utils.pprint(delta, msg=msg)

# Let's create another timedelta using
#
#  `start`: 2020-12-31 00:00:00
#  `end`  : 2020-12-31 12:00:00
# 
start  = dt.datetime(2020, 12, 31)
end = dt.datetime(2020, 12, 31, hour=12)

# These two dates are 12 hours apart
new_delta  = end - start
#utils.pprint(new_delta)

# Add 12 hours to some date
#   - `start` will be the starting date (same as above)
#   - `delta` will be a period of 12 hours (same as new_delta)
#   - `new_end` will be the ending date (same as `end` above)
delta  = dt.timedelta(hours=12)
#utils.pprint(delta, "this is delta")


delta1  = dt.timedelta(days=1.5)
#utils.pprint(delta1, "this is delta1")
#utils.pprint(delta1.seconds, "this is delta1.seconds")
#help(dt.timedelta)


# This is the new date
#new_end = start + delta


# ----------------------------------------------------------------------------
#   Important note about attributes:
#   dt = datetime.datetime(...) --> dt.year, dt.month, dt.day, dt.seconds, ...
#   td = datetime.timedelta(...) --> td.days , dt.seconds, dt.microseconds
# ----------------------------------------------------------------------------
# For instance, consider the following timedelta
#delta_2yr = dt.timedelta(days=365*2) 
#utils.pprint(delta_2yr, "delta_2yr:\n") 


# ----------------------------------------------------------------------------
#   Exercises (5 mins)
# ----------------------------------------------------------------------------
# 1. For how many seconds have you been alive?  
bday = dt.datetime(1974, 11, 1, hour=8, minute=45)
now = dt.datetime.now()
alive = now - bday
secs = (alive.days * 24 * 60 * 60) + alive.seconds
#utils.pprint(secs, "secs:")
#utils.pprint(alive.total_seconds())

# 2. How old will you be in 1,340 days
future = dt.datetime.now() + dt.timedelta(days=1340)
#utils.pprint(future, pretty=False)
alive = future - bday
#age = alive.days/365.
#print(age)



# ---------------------------------------------------------------------------- 
#   The `strftime` method
#   Used to create strings representing dates (in different format)
# ---------------------------------------------------------------------------- 

# | Directive | Meaning                                                       | Example                  |
# |-----------|---------------------------------------------------------------|--------------------------|
# | %a        | Weekday as locale's abbreviated name.                         | Sun, Mon,...             |
# | %A        | Weekday as locale's full name.                                | Sunday, Monday,...       |
# | %w        | Weekday as a decimal number (Sunday=0,Saturday=6)             | 0, 1,..., 6              |
# | %d        | Day of the month as a zero-padded decimal number.             | 01, 02, …, 31            |
# | %b        | Month as locale's abbreviated name.                           | Jan, Feb,..., Dec        |
# | %B        | Month as locale's full name.                                  | January, February,...    |
# | %m        | Month as a zero-padded decimal number.                        | 01, 02, …, 12            |
# | %y        | Year without century as a zero-padded decimal number.         | 00, 01,..., 99           |
# | %Y        | Year with century as a decimal number.                        | 0001, 1999, 2013, 2014   |
# | %H        | Hour (24-hour clock) as a zero-padded decimal number.         | 00, 01, …, 23            |
# | %I        | Hour (12-hour clock) as a zero-padded decimal number.         | 01, 02, …, 12            |
# | %p        | Locale's equivalent of either AM or PM.                       | AM, PM                   |
# | %M        | Minute as a zero-padded decimal number.                       | 00, 01, …, 59            |
# | %S        | Second as a zero-padded decimal number.                       | 00, 01, …, 59            |
# | %j        | Day of the year as a zero-padded decimal number.              | 001, 002, …, 366         |
# | %U        | Week number of the year (Sunday as the first day of the week) | 00, 01, …, 53            |
# | %W        | Week number of the year (Monday as the first day of the week) | 00, 01, …, 53            |
# | %c        | Locale's appropriate date and time representation.            | Tue Aug 16 21:30:00 1988 |

# Create a datetime object representing
#   2020-12-31 00:00:00
date = dt.datetime(year=2020, month=12, day=31, hour=8)
utils.pprint(date, "date is:", pretty=False)

# Convert to a **string** with the following formats
#   2020-12-31
#   Dec 31, 2020
s1  = date.strftime('%Y-%m-%d')
utils.pprint(s1)
s2  = date.strftime('%b %d, %Y')
utils.pprint(s2)


