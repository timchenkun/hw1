import json


class ColorizeMixin:
    def __repr__(self):
        return "\033[1;33;10m" + f'{self.title} | {self.price} ₽' + "\n"


class Advert(ColorizeMixin):
    def __init__(self, values):
        # checking for json format and translating it to a dictionary
        if type(values) is str:
            self.values = json.loads(values)
        else:
            self.values = values

        # checking that the price > 0 and error output if price < 0 and price = 0 if the value is omitted
        if 'price' in values:
            if self.values['price'] >= 0:
                self.price = self.values['price']
            else:
                raise ValueError('must be >= 0')
        else:
            self.price = 0

    def __getattr__(self, item):
        # checking on class
        if item == 'class_':
            return self.values[item[:-1]]
        # checking on dict
        if type(self.values[item]) == dict:
            return Advert(self.values[item])
        return self.values[item]


class print_color(ColorizeMixin):
    def __init__(self, title, price):
        self.title = title
        self.price = price


lesson_str = """{
    "title": "python",
    "price": 1,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
}"""

lesson_ad = Advert(lesson_str)
print(lesson_ad)
print(lesson_ad.title)
print(lesson_ad.price)
print(lesson_ad.location.address)
print(lesson_ad.location.metro_stations)

corgi = """{
  "title": "Вельш-корги",
  "price": 1000,
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
  }
}"""

corgi = Advert(corgi)
print(corgi)
print(corgi.title)
print(corgi.price)
print(corgi.class_)
print(corgi.location.address)

iphone_ad = print_color('iPhone X', 100)
print()
print(iphone_ad)
