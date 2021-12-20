import tkinter as tk

from module import convert_string_to_sql as convert_string
from module import init_tkinter as init_tk

if __name__ == '__main__':
    # tkinter を用いた GUI 作成
    root = tk.Tk()
    # 画面の初期設定
    initTkinter = init_tk.initTkinter()
    initTkinter.run(root)

    # テストデータを SQL 文に変換するボタン
    ConvertStringToSql = convert_string.ConvertStringToSql(master=root)

    # テストデータを入力するテキストボックスを生成
    ConvertStringToSql.create_textbox()

    # 変換後の文字列を表示するテキストボックスを生成
    ConvertStringToSql.create_textbox(state='disabled')

    # テストデータを SQL 文に変換するボタン生成
    ConvertStringToSql.create_button(command='insert')

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()
