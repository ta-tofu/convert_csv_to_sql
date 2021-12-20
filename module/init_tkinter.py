class initTkinter():
    def __init__(self):
        self.display_size = '1024x800'
        self.display_title = 'convert string to sql'

    # 画面サイズを返すメソッド
    def get_display_size(self) -> str:
        return self.display_size

    # 画面タイトルを返すメソッド
    def get_display_title(self) -> str:
        return self.display_title

    # 画面の初期設定を行うメソッド
    def run(self, root):
        root.geometry(self.display_size)
        root.title(self.display_title)
