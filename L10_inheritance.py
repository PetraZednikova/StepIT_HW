"""
class Animal:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello I am {self.name}")
    
class Dog(Animal):
    def make_sound(self):
        print("Haf haf")

d1 = Dog("Baryk")
d1.say_hello()

class Bird(Animal):
    def make_sound(self):
        print("pip pip")
b1 = Bird("Cooco")
b1.say_hello()
"""

#task 1

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Ahoj jsem {self.name} a je mi {self.age} let."

class Builder(Human):
    def __init__(self, name, age, specialization):
        Human.__init__(self, name, age)
        self.specialization = specialization

    def work(self):
        return f"Jsem stavitel a specializuju se na {self.specialization}"

class Sailor(Human):
    def __init__(self, name, age, ship_name):
        Human.__init__(self, name, age)
        self.ship_name = ship_name

    def work(self):
        return f"Jsem námořník pracující na lodi {self.ship_name}"

class Pilot(Human):
    def __init__(self, name, age, airline):
        Human.__init__(self, name, age)
        self.airline = airline
    def work(self):
        return f"Jsem pilot letajici pro {self.airline}"

b1 = Builder(name="Jan", age=35, specialization="Stavby mostu")
s1 = Sailor(name="Tom", age=29, ship_name= "Aurora")
p1 = Pilot(name= "Raul", age=38, airline="Czech Airlines")


print(b1.introduce()) 
print(b1.work())      

print(s1.introduce())   
print(s1.work())        

print(p1.introduce())
print(p1.work())        