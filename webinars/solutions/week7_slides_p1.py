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
res  = ser.loc[label]
#printit(res, f"ser.loc[{label}]:")

label = '2020-01-30'
#res = ser.loc[label] # --> KeyError
#printit(res)



# ------------------------------------------------------------
# Series.loc: Selection using a sequence of labels
# ser.loc[seq] --> series if labels in index, error otherwise
# ------------------------------------------------------------
label_seq = ['2020-01-10', '2020-01-13']
res  = ser.loc[label_seq]
#printit(res, f"ser.loc[{label_seq}]")

label_seq = ['2020-01-10', '2020-01-11']
#res = ser.loc[label_seq] # --> KeyError

# ------------------------------------------------------------
# Series.loc: Selection using slices
# ser.loc[slice] --> series
# ------------------------------------------------------------
# IMPORTANT: ENDPOINTS ARE INCLUDED!!!
start = '2020-01-10'
end = '2020-01-13'
res  = ser.loc[start:end]
#printit(res, f"ser.loc[{start}:{end}]")


# Pandas will return the interval of labels between the slice and index
start = '3020-01-10'
end = '2020-01-13'
res  = ser.loc[start:end]
#printit(res, f"ser.loc['{start}':'{end}']")


# ---- .loc[scalar] can be used in assignment statements ----
ser2 = ser.copy()

# target = expression
ser2.loc['2020-01-11'] = -99
#printit(ser2, f"The ser2:")

start = '2020-01-10'
end = '2020-01-13'
ser2.sort_index(inplace=True)
res  = ser2.loc[start:end]
#printit(res, f"ser2.loc['{start}':'{end}']")

# Problem: not sorted...


# ------------------------------------------------------------
# Series.iloc: Selection using a single pos
# ser.iloc[pos] --> scalar if pos <= ser.size
# ------------------------------------------------------------
#printit(ser.size, f"ser.size:")
pos = 0
res  = ser.iloc[pos]
#printit(res, f"ser.iloc[{pos}]")


# ------------------------------------------------------------
# Series.iloc: Selection using a seq of positions
# ser.iloc[seq of pos] --> series if pos <= ser.size
# ------------------------------------------------------------
# Try it first!
pos_seq = [0, 1]
res  = ser.iloc[pos_seq]
#printit(res, f"ser.iloc[{pos_seq}]")


# ------------------------------------------------------------
# Series.iloc: Selection using slices
#   ser.iloc[slice] --> series
#
# IMPORTANT: Endpoints are NOT included
# ------------------------------------------------------------
# Try it first!
start = 0
end = 1
res  = ser.iloc[start:end]
#printit(res, f"ser.iloc[{start}:{end}]")

#res  = ser.iloc[0]
#printit(res, f"ser.iloc[0]")


# pandas will try to return the interval of "positions" inside the slice
start = 0
end = 100000
#res  = ser.iloc[start:end]

start = -1
end = 0
res  = ser.iloc[start:end]
#printit(res, f"ser.iloc[{start}:{end}]")


# --------------------------------------------------------------------------------------------
# Series[] : can be used with either pos or labels
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
x1  = ser[pos]
x2  = ser[label]
#print(x1, x2)

# ---- Problem: If labels are numbers, it can be quite confusing... ---
ser2 = ser.copy()
ser2.index = [x+1 for x in range(ser2.size)]
#printit(ser2, f"This is ser2")

# Single position, ser2[pos] same as ser2.loc[pos]
pos = 1
label = 1
# Exercise:
#   1. Select the element with label/position using [], .loc, and .iloc
#       and compare the results
# NOTE: use ser2, not ser
printit( ser2.loc[label], f"ser2.loc[{label}]")
printit( ser2.iloc[pos], f"ser2.iloc[{pos}]")
printit( ser2[pos], f"ser2[{pos}]")

# With slices, it's different
# Exercise: 
#   1. Select elements from ser using [], .iloc, and .loc and the slice parms
#   below. Compare the results
# NOTE: use ser2, not ser

start = 1
end = 3
printit(ser2.loc[start:end], f"ser2.loc[{start}:{end}]")
printit(ser2.iloc[start:end], f"ser2.iloc[{start}:{end}]")
printit(ser2[start:end], f"ser2[{start}:{end}]")


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
#printit(df, "The df:")

# df.loc[row label, col label] --> scalar
rlabel = '2020-01-02'
clabel = 'close'
res = df.loc[rlabel, clabel]
#printit(res, f"df.loc[{rlabel}, {clabel}]")


# df.loc[row label] --> df.loc[row label, :]
df1 = df.loc[rlabel]
df2 = df.loc[rlabel, :]
#printit(f'df.loc[{rlabel}] is\n{df1}')
#printit(f'df.loc[{rlabel}, :] is\n{df2}')

# df.loc[ column label ] --> KeyError (unless there row with same label exists)
#res = df.loc[clabel]

# df.loc[:, clabel] --> series with column values (same index)
res  = df.loc[:, clabel]
#printit(res)

# ----------------------------------------------------------------------------
# DataFrames.loc using seq of labels
#
# NOTE:
#   df.loc[label, seq of labels] --> series with COLUMN labels
#   df.loc[seq of labels, label] --> series with ROW (index) labels
# ----------------------------------------------------------------------------
rlabel = '2020-01-02'
rlabel_seq = ['2020-01-02', '2020-01-06']

clabel = 'close'
clabel_seq = ['close', 'bday']

# df.loc[seq labels, label] --> series
res  = df.loc[ rlabel , clabel_seq]
#printit(res, f"df.loc[{rlabel}, {clabel_seq}]")

#msg = f"df.loc[{rlabel_seq}, {clabel}] is:"
#printit(res, msg)

# df.loc[label, seq of labels] --> series
res  = df.loc[rlabel_seq, clabel]
#printit(res, f"df.loc[rlabel_seq, clabel]")

#msg = f"df.loc[{rlabel}, {clabel_seq}] is:"
#printit(res, msg)


# ----------------------------------------------------------------------------
# DataFrames.loc using slices
# ----------------------------------------------------------------------------
clabel_start = 'close'
clabel_end = 'bday'

rlabel_start = '2020-01-10'
rlabel_end = '2020-01-15'

# df.loc[slice] --> data_new frame
res  = df.loc[rlabel_start:rlabel_end]
#printit(res)


# Remember that pandas will not sort the index before selecting the objs
df2 = df.copy()
df2.loc['2020-01-11', ['close', 'bday']] = 1, 1
#printit(df2, f"The df2:")
res  = df2.loc[rlabel_start:rlabel_end]
#printit(res, f"df2.loc['{rlabel_start}':'{rlabel_end}']")


# df.loc[slice, label] --> series
res  = df.loc[rlabel_start:rlabel_end, 'close']
#printit(res)

# df.loc[label, slice] --> series
rlabel = '2020-01-02'
clabel_start = 'close'
clabel_end = 'bday'
res  = df.loc[rlabel, clabel_start:clabel_end]
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
res  = df.iloc[rpos, cpos]
#printit(res)

# df.iloc[pos] --> df.iloc[pos, :] --> series iff pos <= df.shape[0]
#printit(df.shape)

res  = df.iloc[pos]
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
res = df.iloc[:, [1, 0]]
#printit(res1)
# NOTE: You can use the following slide: res1  = df.iloc[:, ::-1 ]

#   2. a SERIES with the last two values from the 'bday' column
res2  = df.iloc[ [-2, -1], 1]
#printit(res2)

#   3. a DF with the the first two rows of df (and all columns)
res3  = df.iloc[ [0, 1]]
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
res1  = df.iloc[ 1:]
#printit(res1)

#   2. a DF (NOT A SERIES) with the last column of df
res2  = df.iloc[:, -1:]
#printit(res2)

#   3. a DF with the first two rows of df (using slices, not seq of positions)
res3  = df.iloc[:2]
#printit(res3)

#   4. a df with the last 100 (one hundred) rows from df (assume you don't know how many
#       rows the data_new frame df has)
res4  = df.iloc[-100:]
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
res  = df[ 'close': 'bday' ]
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


