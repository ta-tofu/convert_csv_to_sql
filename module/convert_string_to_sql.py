import tkinter as tk


class ConvertStringToSql(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.sql_char: str = ''
        self.position = 1.0
        self.first_textbox = None
        self.last_textbox = None
        self.last_button = None

    def create_textbox(self, state: str = 'normal', fill: str = 'x', padx: int = 150, pady: int = 30):
        if self.first_textbox is None:
            self.first_textbox = tk.Text(self)
            self.first_textbox.configure(state=state)
            self.first_textbox.pack(fill=fill, padx=padx, pady=pady)
        else:
            self.last_textbox = tk.Text(self)
            self.last_textbox.configure(state=state)
            self.last_textbox.pack(fill=fill, padx=padx, pady=pady)

    def create_button(self, text: str = 'ボタン', bg: str = '#67D0E0', fg: str = '#251818', command='', state='normal', fill: str = 'x', padx: int = 400):
        self.last_button = tk.Button(self)
        self.last_button['text'] = text
        self.last_button['bg'] = bg
        self.last_button['fg'] = fg

        if command != '':
            if command == 'insert':
                self.last_button['command'] = self.insert_textbox
        self.last_button.configure(state=state)
        self.last_button.pack(fill=fill, padx=padx)

    def insert_textbox(self):
        # 一度テキストボックスを活性化させる
        # 活性化状態じゃないと、テキストボックスに insert が出来ないみたい
        self.last_textbox['state'] = 'normal'
        print(self.convert())

        # テキストボックスを空白にする
        self.last_textbox.delete(self.position, tk.END)

        # 文字列を追加する処理
        self.last_textbox.insert(tk.END, self.sql_char)
        self.last_textbox['state'] = 'disabled'

    def convert(self):
        self.sql_char = ''
        add_text = self.first_textbox.get(self.position, tk.END)
        add_text_list = add_text.splitlines()
        # テーブルごとにデータを SQL 文に変換していく
        sql_text_block = ''
        sql_text_block_number = 0
        for row in add_text_list:
            char_end = row.find('\t\t')

            # 空白の行はテーブルの変わり目
            # ここまで SQL 文の一塊として作成して、次の SQL 文を作成する
            if char_end == 0:
                self.sql_char += sql_text_block[:-1] + ';' + '\n'
                self.sql_char
                sql_text_block = ''
                sql_text_block_number = 0
                continue
            
            # 事業所名を漢字で書いている行は扱わない
            if row in '■':
                continue

            # テーブル名が記載されている行
            if sql_text_block == '':
                row.rstrip()
                sql_text_block += 'insert into ' + row[0:char_end] + ' values '
                sql_text_block_number += 1
            elif sql_text_block != '' and sql_text_block_number == 1:
                sql_text_block_number += 1
                continue
            else:
                used_data = row[0:char_end].replace('\t', ',')
                sql_text_block += '(' + used_data
                sql_text_block.rstrip()
                sql_text_block += ')' + ','

            sql_text_block_number += 1
