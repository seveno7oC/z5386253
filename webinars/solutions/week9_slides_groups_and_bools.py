""" week9_slides_groups_and_bools.py

Codes discussed in class during Week 9

IMPORTANT: This code requires the lec_utils module (available in dropbox)

    toolkit/
    |   ...
    |__ webinars/
    |   |__ __init__.py                         <- Required (empty file)
    |   |__ lec_utils.py                        <- Required
    |   |__ week9_slides_groups_and_bools.py    <- This module
    |       ...
    |__ toolkit_config.py


"""
import pandas as pd

from webinars import lec_utils as utils

utils.pp_cfg.sep = True
utils.pp_cfg.df_info = False



# ---------------------------------------------------------------------------- 
#  Create the event data_new frame
# ---------------------------------------------------------------------------- 
def mk_rec_df0():
    """ Creates an example DF

    Returns
    -------
    data_new frame :

                                     firm   action  event_date
        date
        2012-02-16 07:42:00       JP MORGAN   main  2012-02-16
        2020-09-23 08:58:55   DEUTSCHE BANK   main  2020-09-23
        2020-09-23 09:01:26   DEUTSCHE BANK   main  2020-09-23
        2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23
        2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23
        2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18
        2020-12-09 15:34:34       JP MORGAN   main  2020-12-09

        <class 'pandas.core.frame.DataFrame'>
        DatetimeIndex: 7 entries, 2012-02-16 07:42:00 to 2020-12-09 15:34:34
        Data columns (total 3 columns):
        #   Column      Non-Null Count  Dtype
        ---  ------      --------------  -----
        0   firm        7 non-null      object
        1   action      7 non-null      object
        2   event_date  7 non-null      object
        
    """
    cnts_rec_csv = '''
    date                , firm           , action
    2020-09-23 09:01:26 , Deutsche Bank  , main
    2020-09-23 09:11:01 , Wunderlich     , down
    2020-09-23 11:15:12 , Deutsche bank  , up
    2020-11-18 11:07:44 , Morgan Stanley , up
    2020-12-09 15:34:34 , JP Morgan      , main
    2012-02-16 07:42:00 , JP Morgan      , main
    2020-09-23 08:58:55 , Deutsche Bank  , main
    '''
    df = utils.csv_to_df(cnts_rec_csv, index_col='date', parse_dates=['date'])

    # Upper case version of 'firm' column
    #df.loc[:, 'firm'] = [x.upper() for x in df.loc[:, 'firm']]
    df.loc[:, 'firm'] = df.loc[:, 'firm'].str.upper()
    df.loc[:, 'event_date'] = df.index.strftime('%Y-%m-%d')
    return df



def groupby_example0():
    """ Select the last recommendation for each firm (only)

    """
    # ----------------------------------------------------------------------------
    #   Creates the example data_new frame
    # ----------------------------------------------------------------------------
    df = mk_rec_df0()
    utils.pprint(df, "This is df:")

    # --------------------------------------------------------
    #   Split-Apply-Combine (illustration)
    # --------------------------------------------------------

    # Select last rec for each "FIRM" (only)

    # original DF:

        # date                           firm action  event_date
        # 2012-02-16 07:42:00       JP MORGAN   main  2012-02-16
        # 2020-09-23 08:58:55   DEUTSCHE BANK   main  2020-09-23
        # 2020-09-23 09:01:26   DEUTSCHE BANK   main  2020-09-23
        # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23
        # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23
        # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18
        # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09


    # Split the df into groups (by firm)

        # date                           firm action  event_date
        # 2012-02-16 07:42:00       JP MORGAN   main  2012-02-16
        # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09

        # date                           firm action  event_date
        # 2020-09-23 08:58:55   DEUTSCHE BANK   main  2020-09-23
        # 2020-09-23 09:01:26   DEUTSCHE BANK   main  2020-09-23
        # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23

        # date                           firm action  event_date
        # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23

        # date                           firm action  event_date
        # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18

    # Apply the operation (select last rec)

        # date                           firm action  event_date
        # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09

        # date                           firm action  event_date
        # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23

        # date                           firm action  event_date
        # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23

        # date                           firm action  event_date
        # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18

    # Combine

        # date                           firm action  event_date
        # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09
        # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23
        # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23
        # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18


    # ----------------------------------------------------------------------------
    #   Creating groupby objects
    # ---------------------------------------------------------------------------- 
    groups  = df.groupby('firm') # -> GroupBy
    #utils.pprint(groups, "df.groupby('firm')")

    # The attribute "groups" 
    #utils.pprint(groups.groups, "groups.groups:")

    # Output:
    # {'DEUTSCHE BANK': DatetimeIndex(['2020-09-23 08:58:55', '2020-09-23 09:01:26', '2020-09-23 11:15:12'],
    #                   dtype='datetime64[ns]', name='date', freq=None),
    # 
    #  'JP MORGAN': DatetimeIndex(['2012-02-16 07:42:00', '2020-12-09 15:34:34'], 
    #                   dtype='datetime64[ns]', name='date', freq=None),
    # 
    #  'MORGAN STANLEY': DatetimeIndex([ '2020-11-18 11:07:44'], 
    #                     dtype='datetime64[ns]', name='date', freq=None),
    # 
    #  'WUNDERLICH': DatetimeIndex(['2020-09-23 09:11:01'], 
    #                     dtype='datetime64[ns]', name='date', freq=None)
    #  }

    # ---------------------------------------------------------------------------- 
    #   The elements of groups.groups
    # ---------------------------------------------------------------------------- 
    df = mk_rec_df0()
    groups = df.groupby(by='firm') 
    for firm, idx in groups.groups.items():
        group_df  = df.loc[idx]
        msg = f"Data for Firm == {firm}:"
        #utils.pprint(group_df, msg=msg, show_type=True)


    # ---------------------------------------------------------------------------- 
    #   Applying functions to individual groups and combining
    # ---------------------------------------------------------------------------- 
    df = mk_rec_df0()
    groups = df.groupby(by='firm') 

    # First, using a loop:
    # (we will save the result in a dictionary)
    dic = {}
    for firm, idx in groups.groups.items():
        nobs  = len(df.loc[idx])
        #print(f"Number of obs for Firm == {firm} is {nobs}")
        dic[firm] = nobs
    #utils.pprint(dic, "This is dic:\n")

    # Combine the result into a series
    ser = pd.Series(dic)
    utils.pprint(ser, "This is ser:\n")


    # Then using the apply method
    res  = groups.apply(len)
    #utils.pprint(res,  "groups.apply(len):\n")


    # split-apply-combine in Pandas
    # 1. GroupBy (groups = df.groupby(...))
    # 2. Decide which function to apply or create your own
    # 3. res = groups.apply(func)
    # IMPORTANT: the index in res is the values of the dictionary
    # groups.groups


    # You can apply your own functions
    def get_last(df):
        """ Sorts the dataframe on its index and returns
            last row of the sorted dataframe
        """
        df.sort_index(inplace=True)
        return df.iloc[-1]

    #df0 = df.copy()
    #df.sort_index(inplace=True) # -> None
    #utils.pprint(df0, "df0:")


    #res = get_last(df)
    #utils.pprint(res,  "get_last(df):")

    res  = groups.apply(get_last)
    utils.pprint(res,  "groups.apply(get_last):\n")


    # Some group by operations are so common that Pandas implements them directly
    # on any created instance of `GroupBy`. Here are some examples:
    # 
    # - `GroupBy.count`: count observations per group (exclude missing values)
    # - `GroupBy.size`: get group size, i.e., count observations per group (including missing values)
    # - `GroupBy.last`: select last of observation in each group


    # Count the number of observations inside each group:
    # (includes missing values if any)
    df = mk_rec_df0() 
    groups = df.groupby('firm')
    res = groups.count()
    utils.pprint(res,  "groups.count():\n")


    # Select last obs by group 
    res = df.groupby('firm').last()
    utils.pprint(res,  "df.groupby('firm').last():\n")




def groupby_example1():
    """ Grouping using multiple columns
    """
    # ----------------------------------------------------------------------------
    #   Creates the example data_new frame
    # ----------------------------------------------------------------------------
    df = mk_rec_df0()

    # This is optional
    #df.sort_index(inplace=True)
    #df.reset_index(inplace=True)
    #df.set_index('date', drop=False, inplace=True)

    utils.pprint(df, "This is df:")

    # Split the data_new into groups
    groups  = df.groupby(['firm', 'event_date'])
    #utils.pprint(groups, "df.groupby(['firm', 'event_date']):\n")

    # Select the most recent obs for each group
    res = groups.last()
    #utils.pprint(res,  "groups.last():", df_info=True)

    # The index of the new DF is a MultiIndex
    #utils.pprint(res.index,  "The res.index:\n")

    # Converting the index to columns
    df = res.reset_index()
    df.set_index('date', inplace=True)
    utils.pprint(df,  "res.reset_index():\n")



# ----------------------------------------------------------------------------
#   New topic: Selecting using booleans 
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
#   New example DF 
# ----------------------------------------------------------------------------
def mk_rec_df1():
    """ Creates an example DF

    Returns
    -------
    data_new frame :

         event_date            firm action
      0  2012-02-16       JP MORGAN   main
      1  2020-09-23   DEUTSCHE BANK     up
      2  2020-09-23      WUNDERLICH   down
      3  2020-11-18  MORGAN STANLEY     up
      4  2020-12-09       JP MORGAN   null
    
      <class 'pandas.core.frame.DataFrame'>
      RangeIndex: 5 entries, 0 to 4
      Data columns (total 3 columns):
       #   Column      Non-Null Count  Dtype
      ---  ------      --------------  -----
       0   event_date  5 non-null      object
       1   firm        5 non-null      object
       2   action      5 non-null      object
        
    """
    # --------------------------------------------------------
    # Start with the example df and keep only the last rec
    # by a given firm on a given day
    # --------------------------------------------------------
    df = mk_rec_df0()
    df.sort_index(inplace=True) 
    groups = df.groupby(['event_date', 'firm'])
    df = groups.last().reset_index() 
    return df


def bool_example0():
    """ Given a DF with the last rec for each firm/event-day, keep only
    upgrades and downgrades

    """
    # ----------------------------------------------------------------------------
    #   Creates the example data_new frame
    # ----------------------------------------------------------------------------
    df = mk_rec_df1()
    df.index = df.index + 1
    #utils.pprint(df, "This is df:\n")

    # ----------------------------------------------------------------------------
    #   Using booleans to select rows 
    # ----------------------------------------------------------------------------
    # will be a series with boolean values
    cond = df.loc[:, 'action'] == 'up'
    #utils.pprint(cond, "cond = df.loc[:, 'action'] == 'up'\nThen cond is:\n")


    # We can use this series as an indexer:
    # A series of booleans can be used to select rows that meet the criteria
    res  = df.loc[cond, :]
    #utils.pprint(res, "df.loc[cond]:\n")


    # ----------------------------------------------------------------------------
    #   Using booleans to select rows and cols
    # ----------------------------------------------------------------------------
    col_cond = [False, True, False]
    res  = df.loc[:, col_cond]
    #utils.pprint(df, "This is df:\n")
    #utils.pprint(res, f"The output of df.loc[:, {col_cond}] is:\n")


    # ----------------------------------------------------------------------------
    #   Multiple criteria 
    # ----------------------------------------------------------------------------
    # Combine different criteria
    crit = (df.loc[:, 'action'] == 'up') | (df.loc[:, 'action'] == 'down')
    res = df.loc[crit]
    #utils.pprint(res, "df.loc[crit]")

    # ----------------------------------------------------------------------------
    #   Optionally, using the `str.contains` method
    # ----------------------------------------------------------------------------
    crit  = df.loc[:, 'action'].str.contains('up|down')
    #res = df.loc[crit]
    #utils.pprint(res, "df.loc[:, 'action'].str.contains('up|down'):\n")


    # ----------------------------------------------------------------------------
    #  NOTE: Compare the DF above with he output of Step 3
    #  - Discuss apply(ser, axis=1)
    # ----------------------------------------------------------------------------
    df = res.copy()
    utils.pprint(df, 'df:')


    # --------------------------------------------------------
    #   Applying a function to each element of a series 
    # --------------------------------------------------------
    def _mk_et(value):
        if value == 'up':
            return 'upgrade'
        elif value == 'down':
            return 'downgrade'
        else:
            raise Exception('Value must be either up/down')

    df.loc[:, 'event_type'] = df.loc[:, 'action'].apply(_mk_et)


    # --------------------------------------------------------
    #   Creating an index that starts with 1, 2,... 
    # --------------------------------------------------------

    df.reset_index(inplace=True)
    df.index = df.index + 1
    df.index.name = 'event_id'

    cols = ['event_date', 'firm', 'event_type']
    df = df.loc[:, cols]
    utils.pprint(df, "df:")




if __name__ == "__main__":
    #groupby_example0()
    #groupby_example1()
    bool_example0()
    pass


