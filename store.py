'''
A store can have multiple departments. A department can hold multiple products. 
The store has a name. Departments have names. Products have names and prices.
Soccer Ball is a Product.

Nouns tend to be classes
If a noun"has" something, that something tends to be an attribute.
Verbs tend to be methods.

has-a is also called "Composition"

'''
from dept import Departments


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
