class Shoe:
    def __init__(self, shoe_type, shoe_style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.shoe_style = shoe_style
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def to_dict(self):
        return {
            "тип обуви": self.shoe_type,
            "вид обуви": self.shoe_style,
            "цвет": self.color,
            "цена": self.price,
            "производитель": self.manufacturer,
            "размер": self.size
        }

    @staticmethod
    def from_dict(data):
        return Shoe(
            shoe_type=data["тип обуви"],
            shoe_style=data["вид обуви"],
            color=data["цвет"],
            price=data["цена"],
            manufacturer=data["производитель"],
            size=data["размер"]
        )