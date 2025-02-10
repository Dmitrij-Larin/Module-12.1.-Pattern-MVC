class ShoeView:
    def display_shoes(self, shoes):
        if not shoes:
            print("Нет доступной обуви.")
            return

        for shoe in shoes:
            print(shoe.to_dict())

    def display_message(self, message):
        print(message)