from _01_Model import Shoe
from _02_Controller import ShoeController
from _03_View import ShoeView


if __name__ == "__main__":
    controller = ShoeController()
    view = ShoeView()

    shoe1 = Shoe("Мужская", "Кроссовки", "Черный", 5000, "Nike", 42)
    shoe2 = Shoe("Женская", "Сапоги", "Красный", 8000, "Vigorous", 38)
    shoe3 = Shoe("Мужская", "Кеды", "Белый", 4500, "Reebok", 40)

    controller.add_shoe(shoe1)
    controller.add_shoe(shoe2)
    controller.add_shoe(shoe3)

    view.display_message("Список обуви:")
    view.display_shoes(controller.get_shoes())

    view.display_message("\nПоиск обуви по стилю 'Кроссовки':")
    found_shoes = controller.find_shoe_by_style("Кроссовки")
    view.display_shoes(found_shoes)

    view.display_message("\nПоиск обуви по типу 'Мужская':")
    found_shoes = controller.find_shoe_by_shoe_type("Мужская")
    view.display_shoes(found_shoes)

    view.display_message("\nПоиск обуви по типу 'Женская':")
    found_shoes = controller.find_shoe_by_shoe_type("Женская")
    view.display_shoes(found_shoes)