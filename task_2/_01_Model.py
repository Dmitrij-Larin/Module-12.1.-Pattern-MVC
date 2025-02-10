class Recipe:
    def __init__(self, title, author, recipe_type, description, ingredients, cuisine, link=None):
        self.title = title
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.link = link

    def to_dict(self):
        return {
            'Название': self.title,
            'Автор': self.author,
            'Тип рецепта': self.recipe_type,
            'Описание': self.description,
            'Ингредиенты': self.ingredients,
            'Кухня': self.cuisine,
            'Ссылка': self.link
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['Название'],
            author=data['Автор'],
            recipe_type=data['Тип рецепта'],
            description=data['Описание'],
            ingredients=data['Ингредиенты'],
            cuisine=data['Кухня'],
            link=data.get('Ссылка')
        )