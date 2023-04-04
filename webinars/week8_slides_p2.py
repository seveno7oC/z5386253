""" week7_slides_p2.py

Codes discussed in class during Week 8, Part 2: Time series with Pandas

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
import os
import datetime as dt

import pandas as pd

from webinars import lec_utils as utils
import toolkit_config as cfg

# Set options
utils.pp_cfg.sep = True
utils.pp_cfg.df_info = True


# ----------------------------------------------------------------------------
#   Review (Week 7):
#   The pandas.read_csv function
# ----------------------------------------------------------------------------
# Source file:
QAN_PRC_CSV = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')

# Reading the content of a file
df0 = '?'
#utils.pprint(df, "df0")




# ---------------------------------------------------------------------------- 
# Fake CSV file
# The variable `tsla_prc_csv` will point to a "fake" csv file, containing the
# data_new below.
# ---------------------------------------------------------------------------- 
csv_cnts = '''
date       , open   , high   , low    , close  , adj_close , volume
2010-06-29 , 3.80   , 5.00   , 3.51   , 4.78   , 4.78      , 93831500
2010-06-30 , 5.16   , 6.08   , 4.66   , 4.77   , 4.77      , 85935500
2010-07-01 , 5.00   , 5.18   , 4.05   , 4.39   , 4.39      , 41094000
2010-07-02 , 4.60   , 4.62   , 3.74   , 3.84   , 3.84      , 25699000
2010-07-06 , 4.00   , 4.00   , 3.17   , 3.22   , 3.22      , 34334500
2010-07-07 , 3.27   , 3.32   , 2.99   , 3.16   , 3.16      , 34608500
2010-07-08 , 3.22   , 3.50   , 3.11   , 3.49   , 3.49      , 38557000
2010-07-09 , 3.51   , 3.57   , 3.30   , 3.48   , 3.48      , 20253000
2010-07-12 , 3.58   , 3.61   , 3.40   , 3.41   , 3.41      , 11012500
2010-07-13 , 3.47   , 3.72   , 3.38   , 3.62   , 3.62      , 13400500
2020-11-02 , 394.00 , 406.98 , 392.30 , 400.51 , 400.51    , 29021100
2020-11-03 , 409.73 , 427.77 , 406.69 , 423.90 , 423.90    , 34351700
2020-11-04 , 430.62 , 435.40 , 417.10 , 420.98 , 420.98    , 32143100
2020-11-05 , 428.30 , 440.00 , 424.00 , 438.09 , 438.09    , 28414500
2020-11-06 , 436.10 , 436.57 , 424.28 , 429.95 , 429.95    , 21706000
2020-12-23 , 632.20 , 651.50 , 622.57 , 645.98 , 645.98    , 33173000
2020-12-24 , 642.99 , 666.09 , 641.00 , 661.77 , 661.77    , 22865600
2020-12-28 , 674.51 , 681.40 , 660.80 , 663.69 , 663.69    , 32278600
2020-12-29 , 661.00 , 669.90 , 655.00 , 665.99 , 665.99    , 22910800
'''
tsla_prc_csv = utils.csv_to_fobj(csv_cnts)



# ---------------------------------------------------------------------------- 
#   Time series with Pandas
# ---------------------------------------------------------------------------- 

# ---------------------------------------------------------------------------- 
#   Load the data_new into a dataframe
# ---------------------------------------------------------------------------- 
# df will be:
#             date    open    high     low   close  adj_close    volume
#   0   2010-06-29    3.80    5.00    3.51    4.78       4.78  93831500
#   1   2010-06-30    5.16    6.08    4.66    4.77       4.77  85935500
#   2   2010-07-01    5.00    5.18    4.05    4.39       4.39  41094000
#   3   2010-07-02    4.60    4.62    3.74    3.84       3.84  25699000
#   4   2010-07-06    4.00    4.00    3.17    3.22       3.22  34334500
#   5   2010-07-07    3.27    3.32    2.99    3.16       3.16  34608500
#   6   2010-07-08    3.22    3.50    3.11    3.49       3.49  38557000
#   7   2010-07-09    3.51    3.57    3.30    3.48       3.48  20253000
#   8   2010-07-12    3.58    3.61    3.40    3.41       3.41  11012500
#   9   2010-07-13    3.47    3.72    3.38    3.62       3.62  13400500
#   10  2020-11-02  394.00  406.98  392.30  400.51     400.51  29021100
#   11  2020-11-03  409.73  427.77  406.69  423.90     423.90  34351700
#   12  2020-11-04  430.62  435.40  417.10  420.98     420.98  32143100
#   13  2020-11-05  428.30  440.00  424.00  438.09     438.09  28414500
#   14  2020-11-06  436.10  436.57  424.28  429.95     429.95  21706000
#   15  2020-12-23  632.20  651.50  622.57  645.98     645.98  33173000
#   16  2020-12-24  642.99  666.09  641.00  661.77     661.77  22865600
#   17  2020-12-28  674.51  681.40  660.80  663.69     663.69  32278600
#   18  2020-12-29  661.00  669.90  655.00  665.99     665.99  22910800
#   
#   <class 'pandas.core.frame.DataFrame'>
#   RangeIndex: 19 entries, 0 to 18
#   Data columns (total 7 columns):
#    #   Column     Non-Null Count  Dtype
#   ---  ------     --------------  -----
#    0   date       19 non-null     object
#    1   open       19 non-null     float64
#    2   high       19 non-null     float64
#    3   low        19 non-null     float64
#    4   close      19 non-null     float64
#    5   adj_close  19 non-null     float64
#    6   volume     19 non-null     int64
#   dtypes: float64(5), int64(1), object(1)
#   memory usage: 1.2+ KB

df  = '?'

# This will not work
#df = pd.read_csv(csv_cnts)

# But this will:
#df = pd.read_csv(tsla_prc_csv)
#utils.pprint(df, "This is df:")


# 'date' is a column of strings with dates.
#res = df.loc[:, 'date']
#utils.pprint(res, "df.loc[:, 'date'] gives:")

# The index is just a counter (RangeIndex)
#utils.pprint(df.index, "df.index gives:")

# ----------------------------------------------------------------------------
# The `pandas.to_datetime` method:
#   - converts strings representing dates into datetime and returns a pandas object 
#     with the result. 
#
#   - You can specify the string format using the same arguments as
#     datetime.strftime
#
#   - If you do not specify the format, pandas will guess.
# ----------------------------------------------------------------------------

# strftime format for the dates above is:
fmt = '%Y-%m-%d'

# Important: The type of object returned will depend on the type of object you
# pass to pd.to_datetime
#
# Compare these two cases:

# Case 1. df.loc[:, 'date'] is a series
#date_ser = df.loc[:, 'date'] 
dt_ser  = '?'


# Case 2. df.loc[:, 'date'].array is a pandas array
#date_ary = df.loc[:, 'date'].array
dt_index  = '?'


# Convert the elements in the Date column
#df.loc[:, 'date']  = '?'
#utils.pprint(df)

# ----------------------------------------------------------------------------
#   Setting the index
# ----------------------------------------------------------------------------
#df.set_index('date', inplace=True) 
#utils.pprint(df) 

# Check the new index
#utils.pprint(df.index) 

# ----------------------------------------------------------------------------
#   Setting datetime indexes during read_csv
# ----------------------------------------------------------------------------
# previously:
# df = pd.read_csv(tsla_prc_csv)

# New version
# We must "create a new fake CSV file" first
tsla_prc_csv = utils.csv_to_fobj(csv_cnts)
df  = '?'
#utils.pprint(df)


# ----------------------------------------------------------------------------
#   Illustrating the advantages of a datetime indexes 
# ----------------------------------------------------------------------------
# Select all data_new for a given year in one go
df_2020  = '?'
#utils.pprint(df_2020)

# Select all data_new for a given month
df_2020_11  = '?'
#utils.pprint(df_2020_11)

# Selecting date ranges using strings
df_2020_11_0204  = '?'
#utils.pprint(df_2020_11_0204)


# ----------------------------------------------------------------------------
# Computing returns 
#   - Make sure the data_new frame is sorted!
#   - Make sure you know how pandas will tread missing values 
# ----------------------------------------------------------------------------
# Make sure the dataframe is sorted
#df.sort_index(inplace=True)  

# Note that pandas will use the previous date (whatever that is, by default)
rets  = '?'
#utils.pprint(rets)


# You can specify the frequency pandas will use to computer returns. 
# freq='B' will compute returns using consecutive business days
# (problem)
rets  = '?'
#utils.pprint(rets)


