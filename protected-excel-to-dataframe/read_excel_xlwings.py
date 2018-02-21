# Load password protected Excel files into Pandas DataFrame
# https://davidhamann.de/2018/02/21/read-password-protected-excel-files-into-pandas-dataframe/

import pandas as pd
import xlwings as xw

PATH = '/Users/user/Desktop/xlwings_sample.xlsx'
wb = xw.Book(PATH)
sheet = wb.sheets['sample']

df = sheet['A1:C4'].options(pd.DataFrame, index=False, header=True).value
print(df)
