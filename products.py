from BestBuy import Store


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        try:
            if name == "" or price <= 0 or quantity <= 0:
                raise ValueError
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True
        except ValueError as v:
            print(v)


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        try:
            if self.quantity < quantity:
                raise ValueError
            total_price = self.price * quantity
            self.quantity -= quantity  # reduce stock after purchase
            return total_price
        except ValueError as v:
            print(v)


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def show(self):
        return f"{self.name}, Price: {self.price}, this product is not stocked."


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return f"{self.name}, Price: {self.price}, maximum purchase count: {self.maximum}"


class Promotion(Store):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)










