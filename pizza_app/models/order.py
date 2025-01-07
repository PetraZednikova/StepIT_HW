class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_total(self):
        return sum(pizza.calculate_price() for pizza in self.pizzas)
