import json
import os

R_FILE = "countries.json"


# Первый вариант, без всяких там классов и итераторов //
# R_FILE = "countries.json"
# W_FILE = "countries.txt"
# URL = 'http://en.wikipedia.org/wiki/'
#
# with open(R_FILE, "r") as read_file:
#     data = json.load(read_file)
#
# url_country = {}
# for country in data:
#     country_name = country['name']['common']
#     url_country[country_name] = URL + country_name.replace(' ', '_')
#
# pprint(url_country)
#
# with open(W_FILE, "w", encoding='utf-8') as write_file:
#     for c, u in url_country.items():
#         write_file.write(c + ' - ' + u + '\n')
#

class CountryUrl:
    URL = 'http://en.wikipedia.org/wiki/'

    def __init__(self, file):
        self.url_country = {}
        self.file = file
        self.save_file = os.path.splitext(self.file)[0] + '.txt'
        with open(self.file, "r") as read_file:
            data = json.load(read_file)
        i = 0
        for country in data:
            country_name = country['name']['common']
            self.url_country[i] = country_name
            i += 1

    def get_url(self, country_name):
        return self.URL + country_name.replace(' ', '_')

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor > len(self.url_country) - 2:
            raise StopIteration
        url = self.get_url(self.url_country[self.cursor])
        with open(self.save_file, "a", encoding='utf-8') as write_file:
            write_file.write(self.url_country[self.cursor] + ' - ' + url + '\n')
        return url


countries = CountryUrl(R_FILE)

for country in countries:
    print(country)
