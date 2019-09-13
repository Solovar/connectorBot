import json
from os import listdir
import collections
import six

try:
    collectionsAbc = collections.abc
except:
    collectionsAbc = collections


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

    def update(self, old_dict, new_data, top_dict):  # build and update a json file
        if self.__error is False:
            file = "../json/" + top_dict + '.json'
            for k, v in six.iteritems(new_data):
                dv = old_dict.get(k, {})
                if not isinstance(dv, collectionsAbc.Mapping):
                    old_dict[k] = v
                elif isinstance(v, collectionsAbc.Mapping):
                    old_dict[k] = self.update(dv, v, top_dict)
                else:
                    old_dict[k] = v
                # return old_dict
            self.__save(old_dict, file)
            self.__pull_all()
            return old_dict

    def error(self):  # return the current error
        return self.__error


# work/testing area

x = JsonData.getinstance()
x.get("test")
print(x.result())
y = {
    'persons': {
        'anna': {
            "age": 40
        }
    }
}


def update(d, u):
    for k, v in six.iteritems(u):
        dv = d.get(k, {})
        if not isinstance(dv, collectionsAbc.Mapping):
            d[k] = v
        elif isinstance(v, collectionsAbc.Mapping):
            d[k] = update(dv, v)
        else:
            d[k] = v
    return d


print(x.result())
print(update(x.result(), y))

'''
x = JsonData.getinstance()
x.get("test")
print(x.result())
y = {
    'persons': {
        'anna': {
            "age": 40
        }
    }
}
x.update(x.result(), y, "test")

x.get("test")
print(x.result())

exit()
if not x.error():
    print(x.result())
    print(x.get_rule())
else:
    print(x.error())
'''