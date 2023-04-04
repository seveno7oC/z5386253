import os
import toolkit_config as cfg
import yf_example2
year:int
def qan_prc_to_csv(tic, start="{year}-01-01", end="{year}-12-31"):
    """
    Download Qantas stock prices for a given year into a CSV file.
    The name of this file will be qan_prc_YYYY.csv, where the YYYY stands for the year.
    This file will be saved under the data_new folder.

    Parameters:
    year (int): The year to download prices for.
    tic = "QAN.AX"

    Returns:
    None
    """
    filename = f"qan_prc_{year}.csv"

    yf_example2.yf_prc_to_csv(start_date, end_date, ticker, filepath)

if __name__ == "__main__":
    qan_prc_to_csv(year=2020)