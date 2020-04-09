class Departments:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_products(self, product):
        self.products.append(product)
