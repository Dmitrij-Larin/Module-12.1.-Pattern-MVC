import json

from _01_Model import Recipe


class RecipeController:
    def __init__(self, json_file):
        self.json_file = json_file
        self.recipes = self.load_recipes()

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        self.save_recipes()

    def save_recipes(self):
        with open(self.json_file, 'w', encoding='utf-8') as fh:
            json.dump([recipe.to_dict() for recipe in self.recipes], fh, ensure_ascii=False, indent=4)

    def load_recipes(self):
        try:
            with open(self.json_file, 'r', encoding='utf-8') as fh:
                return [Recipe.from_dict(recipe) for recipe in json.load(fh)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_recipes(self):
        return self.recipes