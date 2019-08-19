import webview
from os import listdir

class MakeVisual:

    def __init__(self):
        self._blocks = {"compiled": "", "head": "", "body": "", "JS": ""}
        self._data = ()

    def add_data(self, data):
        pass

    def add_block(self, html, where):
        pass

    def _lunch_gui(self, title):
        webview.create_window(title, self._blocks["compiled"])
        webview.start()

    def build(self, title):
        build_dirs = ("../javaScript", "../html", "../css")
        # need to figur out build/constructing logic
        self._lunch_gui(title)

    def get_block(self):
        return self._blocks

    def get_data(self):
        return self._data


print(listdir(mypath))