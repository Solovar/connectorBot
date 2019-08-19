

class EnvRead:

    def __init__(self, get=''):
        get_length = len(get)+1
        self.return_data = False
        try:
            f = open("../.env", "r")
            for x in f:
                if not x.find(get):
                    self.return_data = str(x[get_length:])
                    break
            f.close()
        except (OSError, IOError) as e:
            self.return_data = e

    def __repr__(self):
        return self.return_data
