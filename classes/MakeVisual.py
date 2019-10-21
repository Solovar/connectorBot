

class MakeVisual:

    def __init__(self):
        self.__blob = ''
        self.__add_block = ''

    def style(self):
        files = ('bootstrap.min.css', 'style.css')
        return_data = '<style> '
        for item in files:
            f = open("css/" + item, "r")
            return_data += ' /* SPACER!! */ ' + f.read()

        return_data += '</style>'
        return return_data

    def header(self):
        f = open("html/header.html", "r")
        return f.read()

    def add_html(self, filename):
        f = open("html/routes/" + filename + ".html", "r")
        self.__add_block = f.read()

    def navigation(self):
        f = open("html/nav.html", "r")
        return f.read()

    def modal(self):
        pass

    def scripts(self):
        files = ('bootstrap.bundle.min.js', 'jquery-3.3.1.slim.min.js', 'script.js')
        return_data = '<script> '
        for item in files:
            f = open("javaScript/" + item, "r")
            return_data += ' /* SPACER!! */ ' + f.read()

        return_data += '</script>'
        return return_data

    def print(self):
        self.__blob = '<!DOCTYPE html><html><head>' + self.style() + '</head><body><div class="container p-0">' + self.header() + self.navigation() + '<div id="content-area" class="col-9 p-0">' + self.__add_block + '</div></div>' + self.scripts() + '</body></html>'
        return self.__blob


# x = MakeVisual()

#print()