import json
from os import listdir


class JsonData:
    __instance = None
    @staticmethod
    def getinstance():
        if JsonData.__instance is None:
            JsonData()
        return JsonData.__instance

    def __init__(self):
        if JsonData.__instance is not None:
            raise Exception("this class is a singleton")
        else:
            JsonData.__instance = self

        self.__error = False
        self.__dir = {}

        for i in listdir('../Json'):
            name = i[:-5]
            with open('../Json/' + i) as json_data:
                item = json.load(json_data)
                self.__dir[str(name)] = item

    def __pull(self, file):
        pass

    def __save(self, path, data):
        with open(path, 'w') as outfile:
            json.dump(data, outfile)

    def get_all(self):
        return self.__dir

    def get(self, get):
        try:
            path = str(get).split('/')
            storage = self.__dir
            for i in path:
                storage = storage[i]

            return storage
        except KeyError:
            self.__error = "empty or worng path"

    def update(self, data, path):
        pass

    def error(self):
        return self.__error


s = JsonData.getinstance()
x = s.get("twitter")

if not s.error():
    print(x)
else:
    print(s.error())