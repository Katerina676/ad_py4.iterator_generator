from hashlib import md5
import json


class GetWikiCountry:

    def __init__(self, path: str):
        with open(path, encoding='utf-8') as f:
            self.country = json.load(f)
        self.start = -1
        self.end = len(self.country)
        self.link = 'https://en.wikipedia.org/wiki/'

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        country_name = self.country[self.start]['name']['common']
        links = f"{country_name} - {self.link}{country_name.replace(' ', '_')}\n"
        return links


def hash_generate(path: str):
    with open(path, encoding='utf8') as f:
        for line in f:
            yield md5(line.encode()).hexdigest()


if __name__ == '__main__':
    with open('list_links.txt', 'w', encoding='utf-8') as f:
        for country in GetWikiCountry('countries.json'):
            f.write(country)

    for item in hash_generate('countries.json'):
        print(item)

