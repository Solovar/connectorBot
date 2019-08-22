

class EnvRead:

    def __init__(self, get=''):
        get_length = len(get)+1
        self._return_data = ''
        self._error = False
        try:
            f = open("../.env", "r")
            for x in f:
                if not x.find(get):
                    self._return_data = x[get_length:].strip().encode('utf-8')
                    break
            f.close()
        except (OSError, IOError) as e:
            self._error = e

    def __str__(self):
        return self._return_data.decode('utf-8')

    def error(self):
        return self._error

# print(str(EnvRead('TWITTER_CON_KEY')))
