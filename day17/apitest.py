import requests


class Request():

    def __init__(self, url, country = "", name = "") -> None:
        self.filtered = False
        self.url = url
        self.filterCountries = "country="
        self.filterName = "name="
        self.country = ""
        self.name = ""
        if country != "":
            self.filtered = True
            temp = country.split(" ")
            for unit in temp:
                if self.country != "":
                    self.country = self.country + "+"
                self.country = self.country+unit.capitalize()
        if name != "":
            self.filtered = True
            temp = name.split(" ")
            for unit in temp:
                if self.name != "":
                    self.name = self.name + "+"
                self.name = self.name+unit.capitalize()
        self.headers = {'Accept': 'application/json'}

    def get(self):
        if self.filtered:
            self.url = self.url + "?"
            if self.country != "":
                self.url = self.url + self.filterCountries + self.country
                if self.name != "":
                    self.url += ","
            if self.name != "":
                self.url = self.url + self.filterName + self.name

        self.r = requests.get(self.url, headers=self.headers)
        self.response_dict = self.r.json()

    

url = 'http://universities.hipolabs.com/search'
r = Request(url, country = "United states")
r.get()
print(r.response_dict[0])