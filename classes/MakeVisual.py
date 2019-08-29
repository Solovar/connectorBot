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

        def evaluate_all(window):
            window.load_css(self._blocks['head'])
            result = window.evaluate_js(
                str(self._blocks["JS"])
            )

        window = webview.create_window(title, html=str(self._blocks["compiled"]), min_size=(800, 500), confirm_close=True, background_color='#FFF', text_select=True)
        webview.start(evaluate_all, window)

    def _compile(self):
        self._blocks['compiled'] += '<!DOCTYPE html><html lang="en">'
        self._blocks['compiled'] += '<div class="container">'
        self._blocks['compiled'] += '<body>' + self._blocks['body'] + '</body>'
        self._blocks['compiled'] += '</div>'
        self._blocks['compiled'] += '</html>'

    def build(self, title):
        build_dirs = ("../javaScript", "../html", "../css")
        order = ('JS', 'body', 'head')
        for i, val in enumerate(build_dirs):
            for item in listdir(val):
                f = open(val + '/' + item, "r")
                self._blocks[order[i]] = self._blocks[order[i]] + str(f.read())
                f.close()

        self._compile()
        return self._lunch_gui(title)

    def get_block(self):
        return self._blocks

    def get_data(self):
        return self._data


x = MakeVisual()

x.build('title')
exit()
for i in x.get_block():
    print('<-------- ' + str(i) + " block")
    print(x.get_block()[i])
    print('<-------- end of ' + str(i) + " block")
