import json

from _01_Model import Shoe


class ShoeController:
    def __init__(self, filename='обувь.json'):
        self.filename = filename
        self.shoes = self.load_shoes()

    def load_shoes(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                shoes_data = json.load(file)
                return [Shoe.from_dict(shoe) for shoe in shoes_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_shoes(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([shoe.to_dict() for shoe in self.shoes], file, ensure_ascii=False, indent=4)

    def add_shoe(self, shoe):
        self.shoes.append(shoe)
        self.save_shoes()

    def get_shoes(self):
        return self.shoes

    def find_shoe_by_style(self, shoe_style):
        return [shoe for shoe in self.shoes if shoe.shoe_style == shoe_style]

    def find_shoe_by_shoe_type(self, shoe_type):
        return [shoe for shoe in self.shoes if shoe.shoe_type == shoe_type]


