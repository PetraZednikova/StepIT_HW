class Pizza:
    def __init__(self, name, size, base_price):
        self.name = name
        self.size = size
        self.base_price = base_price
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def calculate_price(self):
        return self.base_price + sum(topping.price for topping in self.toppings)

    def __str__(self):
        toppings_list = ", ".join(topping.name for topping in self.toppings)
        return f"{self.name} ({self.size}) - {self.base_price} USD + [{toppings_list}]"
