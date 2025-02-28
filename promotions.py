

class Promotion:
    def __init__(self, member):
        self.member = member


    def apply_promotion(self, product, quantity: float):
        return product.price * quantity


class SecondHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)


    def apply_promotion(self, product, quantity: int):
        # Apply half price for the second unit and onwards
        total_price = product.price * quantity
        if quantity > 1:
            total_price = (((product.price * quantity) // 2) * 1.5)
        return total_price


class ThirdOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)


    def apply_promotion(self, product, quantity: int):
        # Buy 2, get 1 free
        total_price = product.price * (quantity - quantity // 3)
        return total_price


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent


    def apply_promotion(self, product, quantity: int):
        # Apply percent discount
        total_price = product.price * quantity
        total_price -= total_price * (self.percent / 100)
        return total_price