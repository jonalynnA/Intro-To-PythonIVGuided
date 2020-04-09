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


'''
A store can have multiple departments. A department can hold multiple products. 
The store has a name. Departments have names. Products have names and prices.
Soccer Ball is a Product.

Nouns tend to be classes
If a noun"has" something, that something tends to be an attribute.
Verbs tend to be methods.

'''


class Store:
    """ Holds info about a Store """  # <- documentation string

    def __init__(self, name, departments=None):
        """ Construct a new Store"""
        self.name = name
        #self.departments = []

        # if departments is None:
        #self.departments = []
        # else:
        #self.departments = departments
        self.departments = [] if departments is None else departments  # shorthand for the above


class Departments:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_products(self, product):
        self.products.append(product)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class SportsBall(Product):
    def __init__(self, name, price, diameter):
        super().__init__(name, price)
        self.diameter = diameter


class SoccerBall(SportsBall):
    def __init__(self, diameter):
        super().__init__("Soccer Ball", 34.99, 22)


class BasketBall(SportsBall):
    def __init__(self, diameter):
        super().__init__("Basket Ball", 34.99, 24)

# soccer_ball = Product("Soccer Ball", 14.99) <- before we made a soccerBall class


sporting_goods = Departments("Sporting Goods")

# sporting_goods.products.append(soccer_ball)
# if you don't have a method "add_product" use ^^^ but its ugly

# sporting_goods.add_products(soccer_ball)
# if you have a method "add_product" use ^^
