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
        pass
        # webview.create_window(title, self._blocks["compiled"])
        # webview.start()

    def build(self, title):
        build_dirs = ("../javaScript", "../html", "../css")
        order = ('JS', 'body', 'head')
        # need to figur out build/constructing logic
        for i, val in enumerate(build_dirs):
            for item in listdir(val):
                f = open(val + '/' + item, "r")
                self._blocks[order[i]] = self._blocks[order[i]] + str(f.read())
                f.close()

        return self._lunch_gui(title)

    def get_block(self):
        return self._blocks

    def get_data(self):
        return self._data


x = MakeVisual()
print(x.get_block())
x.build('title')