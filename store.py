from products import Product



class Store():


    def __init__(self, product_list):
        self.product_list = product_list


    def add_product(self, product):
        Store.product_list.append(product)


    def remove_product(self, product):
        Store.product_list.remove(product)


    def get_total_quantity(self):
        return Product.get_quantity()


    def get_all_products(self):
        if Product.is_active:
            return self.product_list


    def order(self, shopping_list):
        total_price = 0
        for name, quantity in shopping_list:
            total_price += name.buy(quantity)
        return total_price



