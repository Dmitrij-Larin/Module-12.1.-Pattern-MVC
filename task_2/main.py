from _01_Model import Recipe
from _02_Controller import RecipeController
from _03_View import RecipeView

if __name__ == '__main__':
    controller = RecipeController('рецепты.json')
    view = RecipeView()

    recipe1 = Recipe(
        title="Паста Карбонара",
        author="YouTube канал \"Атлас рецепты\"",
        recipe_type="Второе блюдо",
        description="Классическая паста с соусом из яиц и сыра.",
        ingredients=["паста", "яйцо", "сыр", "бекон", "перец"],
        cuisine="Итальянская",
        link="https://www.youtube.com/watch?v=WvcLXU0X0nc&t=3s"
    )

    recipe2 = Recipe(
        title="Картофильный суп",
        author="Царевна_Несмеяна",
        recipe_type="Первое блюдо",
        description="Вкусный картофильный суп - согревающий и питательный.",
        ingredients=["картофиль", "колбаски", "бекон", "лук", "морковь", "перец", "соль", "зелень"],
        cuisine="Немецкая",
        link="https://www.koolinar.ru/recipe/view/173416"
    )

    controller.add_recipe(recipe1)
    controller.add_recipe(recipe2)
    view.display_message("Список рецептов:")
    view.display_recipes(controller.get_recipes())


