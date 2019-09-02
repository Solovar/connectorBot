import webview
from os import listdir


class MakeVisual:

    def __init__(self):
        self.__blocks = {"compiled": "", "head": "", "body": "", "JS": ""}
        self.__data = ()

    def add_data(self, data):
        pass

    def add_block(self, html, where):
        pass

    def _lunch_gui(self, title):

        def evaluate_all(window):
            window.load_css(self.__blocks['head'])
            result = window.evaluate_js(
                str(self.__blocks["JS"])
            )

        window = webview.create_window(title, html=str(self.__blocks["compiled"]), min_size=(800, 500), confirm_close=True, background_color='#2d2d2d', text_select=True)
        webview.start(evaluate_all, window)

    def _compile(self):
        self.__blocks['compiled'] += '<!DOCTYPE html><html lang="en">'
        self.__blocks['compiled'] += '<body class="fade">'
        self.__blocks['compiled'] += '<div class="container">'
        self.__blocks['compiled'] += self.__blocks['body']
        self.__blocks['compiled'] += '</div>'
        self.__blocks['compiled'] += '</body>'
        self.__blocks['compiled'] += '</html>'

    def build(self, title):
        build_dirs = ("../javaScript", "../html", "../css")
        order = ('JS', 'body', 'head')
        for i, val in enumerate(build_dirs):
            for item in listdir(val):
                f = open(val + '/' + item, "r")
                self.__blocks[order[i]] = self.__blocks[order[i]] + str(f.read())
                f.close()

        self._compile()
        return self._lunch_gui(title)

    def get_block(self):
        return self.__blocks

    def get_data(self):
        return self.__data


x = MakeVisual()

x.build('title')
exit()
for i in x.get_block():
    print('<-------- ' + str(i) + " block")
    print(x.get_block()[i])
    print('<-------- end of ' + str(i) + " block")
