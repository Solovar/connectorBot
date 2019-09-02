

class EnvRead:

    def __init__(self, get=''):
        get_length = len(get)+1
        self.__return_data = ''
        self.__error = False
        try:
            f = open("../.env", "r")
            for x in f:
                if not x.find(get):
                    self.__return_data = x[get_length:].strip().encode('utf-8')
                    break
            f.close()
        except (OSError, IOError) as e:
            self.__error = e

    def __str__(self):
        return self.__return_data.decode('utf-8')

    def error(self):
        return self.__error

# print(str(EnvRead('TWITTER_CON_KEY')))
