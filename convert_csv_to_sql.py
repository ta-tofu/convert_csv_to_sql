import csv
import os
from tkinter import filedialog


class convertCSV2Sql():
    def __init__(self):
        self.sql_char = '-- insert into '

    def get_file_path(self) -> str:
        file_type = [('テキスト', '*.csv')]
        current_path = os.getcwd()
        file_path = filedialog.askopenfilename(filetypes=file_type, initialdir=current_path) 
        return file_path

    def count_rows(self, file_path: str) -> int:
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader]
        return len(rows)

    def create_sql_char(self, file_path: str, row_len):
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for i, row in enumerate(spamreader):
                if i == 0:
                    # sql 文にテーブル名を追加
                    self.sql_char += ''.join(row) + ' '
                elif i == 1:
                    # sql に各カラム名を追加
                    self.sql_char += '(' + ','.join(row) + ') '
                    self.sql_char += 'values '
                elif i >= 2:
                    self.sql_char += '(' + ','.join(row) + ')'
                    if i != row_len - 1:
                        self.sql_char += ','
                    else:
                        self.sql_char += ';'

    def get_sql_char(self):
        return self.sql_char


if __name__ == '__main__':
    Instance = convertCSV2Sql()
    file_path = Instance.get_file_path()
    row_len = Instance.count_rows(file_path)
    Instance.create_sql_char(file_path, row_len)
    print(Instance.get_sql_char())
