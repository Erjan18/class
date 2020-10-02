class Pizza:
    def __init__(self,name,discription,price):
        self.name = name
        self.disc = discription
        self.price = price

    def  order(self):
        self.order= []

    def push(self,order):
        self.name.append(order)

    def delete(self):
        self.name.pop()

    def Price(self,money):
        if money > self.price:
