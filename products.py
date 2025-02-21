

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        try:
            if name == "" or price <= 0:
                raise ValueError
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True
            self.promotion = None
        except ValueError as v:
            print(v)

    def set_promotion(self, promotion):
        self.promotion = promotion

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
                raise ValueError("Not enough stock available.")
            total_price = self.price * quantity

            if self.promotion:
                total_price = self.promotion.apply_promotion(self, quantity)

            self.quantity -= quantity  # reduce stock after purchase
            return total_price
        except ValueError as v:
            print(v)


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        # Call the parent class constructor with quantity=0 for non-stocked products
        super().__init__(name, price, quantity=0)

    def buy(self, quantity):

        total_price = self.price * quantity

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)

        self.quantity -= quantity  # reduce stock after purchase
        return total_price


    def show(self):
        return f"{self.name}, Price: {self.price}, this product is not stocked."


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum


    def show(self):
        return f"{self.name}, Price: {self.price}, maximum purchase count: {self.maximum}"













