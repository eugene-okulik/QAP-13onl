import json


class CountryData:
    def __init__(self, my_filename):
        self.filename = my_filename
        self.data = json.loads(self.read_file())
        self.country = self.data['Country']
        self.avg_temp = self.data['avg_temp']

    def read_file(self):
        with open(self.filename, 'r') as data_file:
            return data_file.read()
