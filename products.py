class Product:
    def __init__(self, name: str, price: float, quantity: int):
        try:
            if name == "" or price <= 0 or quantity <= 0:
                raise Exception
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True
        except Exception as e:
            print(e)


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()


    def is_active(self):
        if self.active:
            return True
        else:
            return False


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
            total_price = self.price * self.quantity
            self.quantity -= quantity
            return total_price
        except ValueError as v:
            print(v)