import json
from pprint import pprint

with open("countries.json", "r") as read_file:
    data = json.load(read_file)

URL = 'http://en.wikipedia.org/wiki/'
url_country = {}
for country in data:
    country_name = country['name']['common']
    url_country[country_name] = URL + country_name.replace(' ', '_')

pprint(url_country)

with open("countries.txt", "w", encoding='utf-8') as write_file:
    for c, u in url_country.items():
        write_file.write(c + ' - ' + u + '\n')
