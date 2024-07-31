import datetime as dt 
import pandas as pd
import pymssql
import glob 
import os

path = r'C:\\Users\Trenkin.Sergey\Downloads\\' # указать папку, в которую падает файл после загрузки
list_of_files = glob.glob(f'{path}Otchet_po_otpravleniyam*.xlsx') 
latest_file = max(list_of_files, key=os.path.getctime)

df = pd.read_excel(latest_file, header=6)
df.drop(columns=['Unnamed: 0'], inplace=True)

df['report_date']= pd.to_datetime(dt.date.today().strftime('%Y-%m-%d'))
