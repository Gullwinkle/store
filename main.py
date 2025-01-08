class Store:
    def __init__(self, name, address, items=None):
        if items is None:
            items = {}
        self.name = name
        self.address = address
        self.items = items

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def see_price(self, item):
        if item in self.items:
            print(f'Цена {item} = {self.items[item]} руб.')
        else:
            return None

    def new_price(self, item, price):
        self.items[item] = price


store1 = Store('Перекрёсток', 'ул. Революции, 66')
store2 = Store('Пятёрочка', 'ул. Ленина, 16')
store3 = Store('Чижик', 'ул. Подлесная, 3')

store1.add_item('Картофель', 50)
store1.add_item('Молоко', 100)
store1.add_item('Яйцо', 125)
store1.see_price('Молоко')
store1.see_price('Курица')
store1.see_price('Картофель')
store1.new_price('Молоко', 110)
store1.see_price('Молоко')
store1.remove_item('Картофель')
store1.see_price('Картофель')
store1.remove_item('Курица')

store2.add_item('Картофель', 45)
store2.add_item('Молоко', 90)
store2.add_item('Яйцо', 110)

store3.add_item('Картофель', 30)
store3.add_item('Молоко', 80)
store3.add_item('Яйцо', 95)
