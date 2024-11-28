#task 1 cars
print()
print("------------------------TASK 1----------------------")
print()
class Car:
    def __init__(self, model, year_of_release, manufacturer, engine_capacity, color, price):

        self._model = model
        self._year_of_release = year_of_release
        self._manufacturer = manufacturer
        self._engine_capacity = engine_capacity
        self._color = color
        self._price = price

    
    def get_model(self):
        return self._model

    def get_year_of_release(self):
        return self._year_of_release

    def get_manufacturer(self):
        return self._manufacturer

    def get_engine_capacity(self):
        return self._engine_capacity

    def get_color(self):
        return self._color

    def get_price(self):
        return self._price

    
    def set_model(self, model):
        self._model = model

    def set_year_of_release(self, year_of_release):
        self._year_of_release = year_of_release

    def set_manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    def set_engine_capacity(self, engine_capacity):
        self._engine_capacity = engine_capacity

    def set_color(self, color):
        self._color = color

    def set_price(self, price):
        self._price = price

    
    def display_info(self):
        print(f"Car Information:")
        print(f"  Model: {self._model}")
        print(f"  Year of Release: {self._year_of_release}")
        print(f"  Manufacturer: {self._manufacturer}")
        print(f"  Engine Capacity: {self._engine_capacity}L")
        print(f"  Color: {self._color}")
        print(f"  Price: ${self._price:,}")


if __name__ == "__main__":
    
    car = Car("Model S", 2020, "Tesla", 3.5, "Red", 79999)


    
    car.display_info()
    print()
    print("Modified info: ")
    print()
    car.set_color("Blue")
    car.set_price(75999)

    
    car.display_info()

print()
# task 2 celsius to fahrenheit

print("------------------------TASK 2----------------------")
print()
class TemperatureConverter:
    _conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter._conversion_count += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter._conversion_count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        return TemperatureConverter._conversion_count



if __name__ == "__main__":
    print("Conversions:")
    print(f"25°C to Fahrenheit: {TemperatureConverter.celsius_to_fahrenheit(25)}°F")
    print(f"77°F to Celsius: {TemperatureConverter.fahrenheit_to_celsius(77)}°C")
    print(f"100°C to Fahrenheit: {TemperatureConverter.celsius_to_fahrenheit(100)}°F")
    print(f"32°F to Celsius: {TemperatureConverter.fahrenheit_to_celsius(32)}°C")

    print("\nTotal conversions performed:", TemperatureConverter.get_conversion_count())
