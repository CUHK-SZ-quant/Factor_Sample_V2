import os, sys 
import re
from typing import List

DATA_FILE_FORMAT = r'^\d{8}_AllSymbols_1min.parquet'
DATE_FORMAT = r'^\d{8}'

DEFAULT_OPEN_TIME = '09:30:00'
DEFAULT_CLOSE_TIME = '15:00:00'

def get_all_data_files(folder_dir: str, start_date: str, end_date: str) -> List:
    fn_lst = []
    for f in os.listdir(folder_dir):
        if os.path.isfile(os.path.join(folder_dir, f)) and re.match(DATA_FILE_FORMAT, f):
            fn_date = re.match(DATE_FORMAT, f).group()
            if fn_date >= start_date and fn_date < end_date:
                fn_lst.append(os.path.join(folder_dir, f))
    fn_lst.sort()
    return fn_lst
    