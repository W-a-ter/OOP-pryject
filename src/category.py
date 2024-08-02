class Category:
    counter_products = 0
    counter_category = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        self.counter_products += 1
        self.counter_category += 1
