class RecipeView:
    def display_recipes(self, recipes):
        if not recipes:
            print("Нет доступных рецептов.")
            return
        for recipe in recipes:
            print(f"\nНазвание: {recipe.title}")
            print(f"Автор: {recipe.author}")
            print(f"Тип рецепта: {recipe.recipe_type}")
            print(f"Описание: {recipe.description}")
            print(f"Ингредиенты: {', '.join(recipe.ingredients)}")
            print(f"Кухня: {recipe.cuisine}")
            if recipe.link:
                print(f"Ссылка: {recipe.link}")

    def display_message(self, message):
        print(message)