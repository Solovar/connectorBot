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
    def getinstance(file='../static/Json'):  # get current instance, if non make one
        if JsonData.__instance is None:
            JsonData(file)
        return JsonData.__instance

    def __init__(self, file):
        if JsonData.__instance is not None:  # check that no new instance was attempted
            raise Exception("this class is a singleton")
        else:
            JsonData.__instance = self

        self.__error = False  # error var, save errors here
        self.__dir = {}  # the main storage dict
        self.__result = None  # the results var
        self.__rule = {}  # rules set for the current path
        self.__file_dir = file
        self.__pull_all()  # run pull all to the main dir

    def __pull_all(self):  # pulls all json from it's folder
        self.__dir = {}
        for i in listdir(self.__file_dir):
            name = i[:-5]
            with open(self.__file_dir + '/' + i) as json_data:
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

    def update(self, new_data, target_file):  # build and update a json file
        file = self.__file_dir + "/" + target_file + '.json'
        self.get(target_file)
        if not self.__error and self.__rule["update"]:
            old_dict = self.result()

            def json_update(d, u):
                for k, v in six.iteritems(u):
                    dv = d.get(k, {})
                    if not isinstance(dv, collectionsAbc.Mapping):
                        d[k] = v
                    elif isinstance(v, collectionsAbc.Mapping):
                        d[k] = json_update(dv, v)
                    else:
                        d[k] = v
                return d
            return_data = json_update(old_dict, new_data)
            self.__save(file, return_data)
            self.__pull_all()
        else:
            self.__error = "file not found or not permitted to do .update()"

    def delete(self, delete_keys, target):
        self.get(target)
        if not self.__error and self.get_rule()['delete']:
            pass  # unfinished method needs be compleated at some point before commands function get's added
        else:
            self.__error = "file not found or not permitted to do .delete()"

    def set_file_dir(self, dir):
        self.__file_dir = dir

    def error(self):  # return the current error
        return self.__error


# work/testing area
'''
x = JsonData.getinstance()
x.get("test")
print(x.result())
y = {
    'persons': {
        'anna': {
            "age": 10
        },
        'jasper': {
            "sandwitch": "ældskfjgiromv"
        }
    }
}

v = ("persons", "anna", "age")
x.update(y, "test")
x.get('test')
print(x.result())

x.delete(v, "test")

print(x.result())
'''