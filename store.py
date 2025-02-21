

class Store:

    def __init__(self, products: list):
        self.products = products


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        self.products.remove(product)


    def get_total_quantity(self):
        total_quantity = 0
        for item in self.products:
            total_quantity +=item.get_quantity()
        return total_quantity


    def get_all_products(self):
        all_active_products = []
        for item in self.products:
            if item.is_active():
                all_active_products.append(item)
        return all_active_products


    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            price = product.buy(quantity)
            total_price += price

        return total_price



