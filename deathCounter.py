import os
import time
"""
death counter


file structure:
    COMMAND_ID.txt
"""


class Counting:

    def __init__(self):
        dir_files = os.listdir('deathCounter')
        if len(dir_files) == 0:
            self.files = []
        else:
            self.files = dir_files

    def is_in(self, counter_name):
        name_len = len(counter_name)
        return_list = []
        for i in self.files:
            if counter_name == i[0:name_len]:
                return_list.append(i)

        return return_list

    def add(self, counter_name):
        total = 0
        counters = self.is_in(counter_name)
        if len(counters) is not 0:
            for i in counters:
                with open('deathCounter/' + str(i), 'r') as inp:
                    content = inp.read()
                    total = int(content) + 1

                with open('deathCounter/' + str(i), 'w') as outp:
                    outp.write(str(total))

    def subtract(self, counter_name):
        total = 0
        counters = self.is_in(counter_name)
        if len(counters) is not 0:
            for i in counters:
                with open('deathCounter/' + str(i), 'r') as inp:
                    content = inp.read()
                    total = int(content) - 1

                with open('deathCounter/' + str(i), 'w') as outp:
                    outp.write(str(total))

    def set(self, counter_name, number):
        counters = self.is_in(counter_name)
        if len(counters) is not 0:
            for i in counters:
                with open('deathCounter/' + str(i), 'w') as outp:
                    outp.write(str(number))

    def create_counter(self, command):
        file_id = int(time.time())
        with open('deathCounter/' + str(command) + '_' + str(file_id) + '.txt', 'w') as outp:
            outp.write(str(0))

    def delete_counter(self, file):
        os.remove('deathCounter/' + file)
        dir_files = os.listdir('deathCounter')
        if len(dir_files) == 0:
            self.files = []
        else:
            self.files = dir_files
