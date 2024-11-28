#task 1 - coffee machine
print()
print("----------------------TASK 1 -------------------------")


class Device:
    def __init__(self, brand, model, power, price):
        
        self.brand = brand
        self.model = model
        self.power = power  
        self.price = price  

    def display_info(self):
        
        print(f"Device Information:")
        print(f"  Brand: {self.brand}")
        print(f"  Model: {self.model}")
        print(f"  Power: {self.power}W")
        print(f"  Price: ${self.price}")



class CoffeeMachine(Device):
    def __init__(self, brand, model, power, price, coffee_type):
        self.brand = brand
        self.model = model
        self.power = power
        self.price = price
        self.coffee_type = coffee_type  

    def make_coffee(self):
        print(f"{self.brand} {self.model} is making a delicious cup of {self.coffee_type} coffee.")

    def display_info(self):
        print(f"Device Information:")
        print(f"  Brand: {self.brand}")
        print(f"  Model: {self.model}")
        print(f"  Power: {self.power}W")
        print(f"  Price: ${self.price}")
        print(f"  Coffee Type: {self.coffee_type}")



class Blender(Device):
    def __init__(self, brand, model, power, price, capacity):
        self.brand = brand
        self.model = model
        self.power = power
        self.price = price
        self.capacity = capacity  

    def blend(self):
        print(f"{self.brand} {self.model} is blending ingredients with a capacity of {self.capacity}L.")

    def display_info(self):
        print(f"Device Information:")
        print(f"  Brand: {self.brand}")
        print(f"  Model: {self.model}")
        print(f"  Power: {self.power}W")
        print(f"  Price: ${self.price}")
        print(f"  Capacity: {self.capacity}L")



class MeatGrinder(Device):
    def __init__(self, brand, model, power, price, blade_material):
        self.brand = brand
        self.model = model
        self.power = power
        self.price = price
        self.blade_material = blade_material  

    def grind_meat(self):
        print(f"{self.brand} {self.model} is grinding meat using {self.blade_material} blades.")

    def display_info(self):
        print(f"Device Information:")
        print(f"  Brand: {self.brand}")
        print(f"  Model: {self.model}")
        print(f"  Power: {self.power}W")
        print(f"  Price: ${self.price}")
        print(f"  Blade Material: {self.blade_material}")



if __name__ == "__main__":
    
    coffee_machine = CoffeeMachine("DeLonghi", "Magnifica", 1350, 599, "Espresso")
    blender = Blender("Philips", "ProBlend 5000", 800, 149, 1.5)
    meat_grinder = MeatGrinder("Bosch", "MFW68640", 2200, 299, "Stainless Steel")

    
    print("\nCoffee Machine:")
    coffee_machine.display_info()
    coffee_machine.make_coffee()

    print("\nBlender:")
    blender.display_info()
    blender.blend()

    print("\nMeat Grinder:")
    meat_grinder.display_info()
    meat_grinder.grind_meat()

#task 4 pizza app.
print()
print("----------------------TASK 4 -------------------------")
print()


def base_pizza():
    return "Pizza base"


def margarita(pizza_function):
    def wrapper():
        return f"{pizza_function()} with tomato sauce, mozzarella, and basil"
    return wrapper

def four_cheese(pizza_function):
    def wrapper():
        return f"{pizza_function()} with mozzarella, gorgonzola, parmesan, and ricotta"
    return wrapper

def capricciosa(pizza_function):
    def wrapper():
        return f"{pizza_function()} with tomato sauce, mozzarella, mushrooms, ham, and artichokes"
    return wrapper

def hawaiian(pizza_function):
    def wrapper():
        return f"{pizza_function()} with tomato sauce, mozzarella, ham, and pineapple"
    return wrapper


if __name__ == "__main__":
   
    margarita_pizza = margarita(base_pizza)
    four_cheese_pizza = four_cheese(base_pizza)
    capricciosa_pizza = capricciosa(base_pizza)
    hawaiian_pizza = hawaiian(base_pizza)

    
    print("Available Pizzas:")
    print(f"Margarita: {margarita_pizza()}")
    print(f"Four Cheese: {four_cheese_pizza()}")
    print(f"Capricciosa: {capricciosa_pizza()}")
    print(f"Hawaiian: {hawaiian_pizza()}")
print()