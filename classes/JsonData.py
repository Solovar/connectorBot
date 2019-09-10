import json
from os import listdir


class JsonData:
    __instance = None  # set up the singleton instance
    @staticmethod
    def getinstance():  # get current instance, if non make one
        if JsonData.__instance is None:
            JsonData()
        return JsonData.__instance

    def __init__(self):
        if JsonData.__instance is not None:  # check that no new instance was attempted
            raise Exception("this class is a singleton")
        else:
            JsonData.__instance = self

        self.__error = False  # error var, save errors here
        self.__dir = {}  # the main storage dict
        self.__result = None  # the results var
        self.__rule = {}  # rules set for the current path
        self.__pull_all()  # run pull all to the main dir

    def __pull_all(self):  # pulls all json from it's folder
        self.__dir = {}
        for i in listdir('../Json'):
            name = i[:-5]
            with open('../Json/' + i) as json_data:
                item = json.load(json_data)
                self.__dir[str(name)] = item

    def __pull(self, file):
        pass

    def __save(self, file_path, data):  # save Json to spesefic file
        with open(file_path, 'w') as outfile:
            json.dump(data, outfile)

    def get_all(self):  # get the whole data set
        self.__result = self.__dir

    def get(self, path):  # get the data at the path
        try:
            item = str(path).split('/')
            storage = self.__dir
            for i in item:
                storage = storage[i]
                self.__set_rule(storage)

            self.__result = storage
        except KeyError:
            self.__error = "empty or worng path"

    def __set_rule(self, current):  # set up the rule container, so we can easyly get the rules relevant for last path
        if type(current) is dict:
            if "rule" in current.keys():
                self.__rule = current['rule']

    def get_rule(self):  # return the rule set
        return self.__rule

    def result(self):  # return the result of the current path
        return self.__result

    def update(self, data, path):  # build and update a json file
        self.get(path)
        if self.get_rule()['update'] and self.__error is False:
            dir_look_up = tuple(str(path).split('/'))
            self.get(dir_look_up[0])
            print(dir_look_up[-2])
            storage = json.dumps(self.result())
            print(storage)
            # self.__save(updated_data, file)
            # self.__pull_all()

    def error(self):  # return the current error
        return self.__error


# work/testing area
x = JsonData.getinstance()
x.get("test/persons/anna")
print(x.result())
x.update('36', "test/persons/anna/age")

x.get("test/persons")
print(x.result())

exit()
if not x.error():
    print(x.result())
    print(x.get_rule())
else:
    print(x.error())