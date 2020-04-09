# Inheritance
"""
[Animal] <- [Dog]
   ^
   |
 [Cat] <- [Tabby]
"""


class Animal:  # Base class: class that everything inherits from
    def __init__(self, leg_count=4):
        print("Animal Constructor")
        self.leg_count = leg_count

    def make_sound(self):
        print("[generic animal noise]")


class Dog(Animal):  # Dog inherits from Animal, dog is an animal. is-a relationship
    def make_sound(self):  # Override the make_sound method
        print("Woof")


class Cat(Animal):
    def __init__(self, tail_length):
        super().__init__()  # Call the constructor of Animal with 4 legs
        self.tail_length = tail_length


class Tabby(Cat):
    def __init__(self):  # all the constructor of Cat with tail length 8
        super().__init__(8)


centipede = Animal(100)
snake = Animal(0)

cat = Animal()
cat = Cat(8)
dog = Dog()
dog = Animal()

cat.make_sound()  # [generic animal noise]
dog.make_sound()  # Woof
dog.make_sound  # [generic animal noise]
print(dog.leg_count)  # 4
