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
        self.__result = None
        self.__pull_all()

    def __pull_all(self):
        for i in listdir('../Json'):
            name = i[:-5]
            with open('../Json/' + i) as json_data:
                item = json.load(json_data)
                self.__dir[str(name)] = item

    def __pull(self, file):
        pass

    def __save(self, file_path, data):
        with open(file_path, 'w') as outfile:
            json.dump(data, outfile)

    def get_all(self):
        self.__result = self.__dir

    def get(self, path):
        try:
            item = str(path).split('/')
            storage = self.__dir
            for i in item:
                storage = storage[i]

            self.__result = storage
        except KeyError:
            self.__error = "empty or worng path"

    def result(self):
        return self.__result

    def update(self, data, path):
        dir_look_up = str(path).split('/')
        file = "../json/" + dir_look_up[0] + ".json"
        self.__save(data, file)
        # self.__pull()

    def error(self):
        return self.__error


JsonData.getinstance().get('test')

if not JsonData.getinstance().error():
    print(JsonData.getinstance().result())
else:
    print(JsonData.getinstance().error())