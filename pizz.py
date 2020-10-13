class Pizza:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.list = []

    def add_pizza(self,pizza):
        self.list.append(pizza)

    def __repr__(self):
        return f'Ваша Пицца:{self.name}'

    def delete(self):
        self.list.pop()

    def to_order(self,money):
        if money >= self.price:
            result = money - self.price
            return f'Ваша сдача:{result}'
        else:
            return 'У вас недостаточно средств'


new_elem1 = Pizza('Пиперони',400)

new_elem1.add_pizza(new_elem1)
print(new_elem1.list)
print(new_elem1.to_order(400))