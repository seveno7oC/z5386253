""" week7_slides_p1.py

Scaffold with the codes we will discuss during the first part of the class (Week 7)

"""
import pprint as pp

import pandas as pd


# This is an auxiliary function, please do not modify
def printit(obj, msg=None):
    """ Pretty prints `obj`

    Parameters
    ----------
    obj : any object

    msg : str, optional
        Message preceding obj representation

    """
    sep = '-'*40
    if isinstance(obj, str):
        prt = obj
    elif isinstance(obj, (pd.DataFrame, pd.Series)):
        prt = obj.to_string()
    else:
        prt = pp.pformat(obj)

    if not isinstance(obj, str):
        prt = f'{prt}\n\nObj type is: {type(obj)}'
    if msg is not None:
        prt = f'{msg}\n\n{prt}'
    to_print = [
        '',
        sep,
        prt,
        sep,
        ]
    print('\n'.join(to_print))


# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
    '2020-01-02',
    '2020-01-03',
    '2020-01-06',
    '2020-01-07',
    '2020-01-08',
    '2020-01-09',
    '2020-01-10',
    '2020-01-13',
    '2020-01-14',
    '2020-01-15',
]
prices = [
    7.1600,
    7.1900,
    7.0000,
    7.1000,
    6.8600,
    6.9500,
    7.0000,
    7.0200,
    7.1100,
    7.0400,
]
# Trading day counter
bday = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10]

# ----------------------------------------------------------------------------
#   Create instances
# ----------------------------------------------------------------------------
# Create a series object
ser = pd.Series(data=prices, index=dates)
printit(ser, "The series `ser`:")

# Data Frame with close and Bday columns
df = pd.DataFrame(data={'close': ser, 'bday': bday}, index=dates)
printit(df, "The data_new frame `df`:")

# ----------------------------------------------------------------------------
#   Series
# ----------------------------------------------------------------------------
# ser:
#   2020-01-02    7.16
#   2020-01-03    7.19
#   2020-01-06    7.00
#   2020-01-07    7.10
#   2020-01-08    6.86
#   2020-01-09    6.95
#   2020-01-10    7.00
#   2020-01-13    7.02
#   2020-01-14    7.11
#   2020-01-15    7.04


# ------------------------------------------------------------
# Series.loc: Selection using a single label
# ser.loc[label] --> scalar if label in index, error otherwise
# ------------------------------------------------------------
label = '2020-01-10'
res  = '?'
#printit(res, f"ser.loc[{label}]:")

#label = '2020-01-30'
#res = ser.loc[label] # --> KeyError
#printit(res)


# ------------------------------------------------------------
# Series.loc: Selection using a sequence of labels
# ser.loc[seq] --> series if labels in index, error otherwise
# ------------------------------------------------------------
label_seq = ['2020-01-10', '2020-01-13']
res  = '?'
#printit(res)

#label_seq = ['2020-01-10', '2020-01-11']
#res = ser.loc[label_seq] # --> KeyError

# ------------------------------------------------------------
# Series.loc: Selection using slices
# ser.loc[slice] --> series
# ------------------------------------------------------------
# IMPORTANT: ENDPOINTS ARE INCLUDED!!!
start = '2020-01-10'
end = '2020-01-13'
res  = '?'
#printit(res)


# Pandas will return the interval of labels between the slice and index
start = '3020-01-10'
end = '2020-01-13'
res  = '?'
#printit(res)

# ---- .loc[scalar] can be used in assignment statements ----
#ser2 = ser.copy()

#ser2.loc['2020-01-11'] = -99
#printit(ser2)

start = '2020-01-10'
end = '2020-01-13'
res  = '?'
#printit(res)

# Problem: not sorted...


# ------------------------------------------------------------
# Series.iloc: Selection using a single pos
# ser.iloc[pos] --> scalar if pos <= ser.size
# ------------------------------------------------------------
#printit(ser.size)
pos = 0
res  = '?'
#printit(res)


# ------------------------------------------------------------
# Series.iloc: Selection using a seq of positions
# ser.iloc[seq of pos] --> series if pos <= ser.size
# ------------------------------------------------------------
pos_seq = [0, 1]
res  = '?'
#printit(res)


# ------------------------------------------------------------
# Series.iloc: Selection using slices
#   ser.iloc[slice] --> series
#
# IMPORTANT: Endpoints are NOT included
# ------------------------------------------------------------
start = 0
end = 1
res  = '?'
#printit(res)

# pandas will try to return the interval of "positions" inside the slice
start = 0
end = 100000
res  = '?'
#printit(res)


# --------------------------------------------------------------------------------------------
# Series.[] : can be used with either pos or labels
#
# | Selection                     | Result       | Notes                                     |
# |-------------------------------|--------------|-------------------------------------------|
# | Series[label]                 | scalar value | Label must exist, otherwise KeyError      |
# | Series[list of labels]        | Series       | All labels must exist, otherwise KeyError |
# | Series[start_label:end_label] | Series       | Behaviour will vary                       |
# | Series[pos]                   | scalar       | similar to lists                          |
# | Series[list of pos]           | Series       | similar to lists                          |
# | Series[start_pos:end_pos]     | Series       | endpoints not included                    |
# --------------------------------------------------------------------------------------------

pos = 0
label = '2020-01-02'
x1  = '?'
x2  = '?'
#print(x1, x2)

# ---- Problem: If labels are numbers, it can be quite confusing... ---
ser2 = ser.copy()
ser2.index = [x+1 for x in range(ser2.size)]
#printit(ser2)

# Single position, ser2[pos] same as ser2.loc[pos]
pos = 1
label = 1
# Exercise: 
#   1. Select the element with label/position using [], .loc, and .iloc
#       and compare the results

# With slices, it's different
# Exercise: 
#   1. Select elements from ser using [], .iloc, and .loc and the slice parms
#   below. Compare the results

start = 1
end = 3


# ----------------------------------------------------------------------------
#   Data frames
# ----------------------------------------------------------------------------
# df:
#             close  bday
# 2020-01-02   7.16     1
# 2020-01-03   7.19     2
# 2020-01-06   7.00     3
# 2020-01-07   7.10     4
# 2020-01-08   6.86     5
# 2020-01-09   6.95     6
# 2020-01-10   7.00     7
# 2020-01-13   7.02     8
# 2020-01-14   7.11     9
# 2020-01-15   7.04    10


# ----------------------------------------------------------------------------
# DataFrames.loc[row indexer, col indexer] :  Indexing by row and column labels
#
# where indexer can be:
#
#   - a single label
#   - a sequence of labels
#   - a slice of labels
#
# Note:
#   df.loc[row indexer] same as df.loc[row indexer, :]
#
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# DataFrames.loc using single labels
# ----------------------------------------------------------------------------

# df.loc[row label, col label] --> scalar
rlabel = '2020-01-02'
clabel = 'close'
res  = '?'
#printit(res)


# df.loc[row label] --> df.loc[row label, :]
df1  = '?'
df2  = '?'
#printit(f'df.loc[{rlabel}] is\n{df1}')
#printit(f'df.loc[{rlabel}, :] is\n{df2}')

# df.loc[ column label ] --> KeyError (unless there row with same label exists)
#res = df.loc[clabel]

# df.loc[:, clabel] --> series with column values (same index)
res  = '?'
#printit(res)

# ----------------------------------------------------------------------------
# DataFrames.loc using seq of labels
#
# NOTE:
#   df.loc[label, seq of labels] --> series with COLUMN labels
#   df.loc[seq of labels, label] --> series with ROW (index) labels
# ----------------------------------------------------------------------------
rlabel = '2020-01-02'
clabel = 'close'
clabel_seq = ['close', 'bday']
rlabel_seq = ['2020-01-02', '2020-01-06']

# df.loc[seq labels, label] --> series
res  = '?'
msg = 'df.loc[rlabel_seq, clabel] is:'
#printit(res, msg)

# df.loc[label, seq of labels] --> series
res  = '?'
msg = 'df.loc[rlabel, clabel_seq] is:'
#printit(res, msg)


# ----------------------------------------------------------------------------
# DataFrames.loc using slices
# ----------------------------------------------------------------------------
clabel_start = 'close'
clabel_end = 'bday'

rlabel_start = '2020-01-10'
rlabel_end = '2020-01-15'

# df.loc[slice] --> data_new frame
res  = '?'
#printit(res)

res  = '?'
#printit(res)

# Remember that pandas will not sort the index before selecting the objs
df2 = df.copy()
df2.loc['2020-01-11', ['close', 'bday']] = 1, 1
#printit(df2)
res  = '?'
#printit(res)


# df.loc[slice, label] --> series
res  = '?'
#printit(res)

# df.loc[label, slice] --> series
rlabel = '2020-01-02'
clabel_start = 'close'
clabel_end = 'bday'
res  = '?'
msg = f"df.loc['{rlabel}', '{clabel_start}':'{clabel_end}']:"
#printit(res, msg)


# ----------------------------------------------------------------------------
# DataFrames.iloc[row indexer, col indexer] :  Indexing by row and column positions
#
# where indexer can be:
#
#   - a single position
#   - a sequence of positions
#   - a slice of positions
#
# Note:
#   df.iloc[row indexer] same as df.iloc[row indexer, :]
#
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# DataFrames.iloc using single labels
# ----------------------------------------------------------------------------
cpos = 0
rpos = 1

# df.iloc[pos, pos] --> scalar
res  = '?'
#printit(res)

# df.iloc[pos] --> df.iloc[pos, :] --> series iff pos <= df.shape[0]
#printit(df.shape)

res  = '?'
#printit(res)


# ----------------------------------------------------------------------------
# DataFrames.iloc using seq of labels
# ----------------------------------------------------------------------------
# Exercise:
# Use .iloc to produce the following objects from df
#   1. a DF with all rows from df but with the order of columns reversed
#   2. a SERIES with the last two values from the 'bday' column
#   3. a DF with the the first two rows of df (and all columns)

# 1. a DF with all rows from df but with the order of columns reversed
res1  = '?'
#printit(res1)

#   2. a SERIES with the last two values from the 'bday' column
res2  = '?'
#printit(res2)

#   3. a DF with the the first two rows of df (and all columns)
res3  = '?'
#printit(res3)


# ----------------------------------------------------------------------------
# DataFrames.iloc using slices
# ----------------------------------------------------------------------------
# Exercise:
# Use .iloc and slices to produce the following objects from df
#   1. a DF with all rows from df except the first one
#   2. a DF (NOT A SERIES) with the last column of df
#   3. a DF with the first two rows of df (using slices, not seq of positions)
#   4. a df with the last 100 (one hundred) rows from df (assume you don't know how many
#       rows the data_new frame df has)

#   1. a DF with all rows from df except the first one
res1  = '?'
#printit(res1)

#   2. a DF (NOT A SERIES) with the last column of df
res2  = '?'
#printit(res2)

#   3. a DF with the first two rows of df (using slices, not seq of positions)
res3  = '?'
#printit(res3)

#   4. a df with the last 100 (one hundred) rows from df (assume you don't know how many
#       rows the data_new frame df has)
res4  = '?'
#printit(res4)


# ----------------------------------------------------------------------------
# DataFrames and []
#
# | Selection            | Result | Notes                              |
# |----------------------|--------|------------------------------------|
# | df[colname]          | series | colname must exist                 |
# | df[list of colnames] | df     | All colname must exist             |
# | df[slices]           | df     | Operates on row index, not columns |
# ----------------------------------------------------------------------------

# df[label] --> series with the elements from the COLUMN labeled 'label'
res  = '?'
#printit(res)

# df[label] -->KeyError if column label not found
#res = df['2020-01-02']


# df[seq of labels] --> DF with the column labels in the order provided
clabel_seq = ['bday', 'close'] 
res  = '?'
#printit(res)

# Very common mistakes
#res = df['bday', 'close']
#res = df['2020-01-02', 'close']


