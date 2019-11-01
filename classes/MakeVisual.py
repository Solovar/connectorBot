

class MakeVisual:

    def __init__(self):
        self.__blob = ''
        self.__add_block = ''
        self.__script_to_add = ''

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

    def add_html_from_file(self, filename):
        f = open("html/routes/" + filename + ".html", "r")
        self.__add_block = f.read()

    def navigation(self):
        f = open("html/nav.html", "r")
        return f.read()

    def modal(self):
        pass

    def add_script(self, file_name):
        self.__script_to_add = file_name

    def __scripts(self):
        files = ('jquery-3.4.1.min.js', 'bootstrap.bundle.min.js', self.__script_to_add)
        return_data = ''
        for item in files:
            if not item == '':
                return_data += '<script src="/static/javaScript/' + item + '"></script> '
        return return_data

    def printing(self):
        self.__blob = '<!DOCTYPE html><html><head>' + self.style() + '</head><body><div class="container p-0">' + self.header() + '<div class="row">' + self.navigation() + '<div id="content-area" class="col-10">' + self.__add_block + '</div></div></div>' + self.__scripts() + '</body></html>'
        return self.__blob


# x = MakeVisual()

#print()