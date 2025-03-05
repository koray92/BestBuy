from products import Product, NonStockedProduct, LimitedProduct
from store import Store
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount



# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250),
                 NonStockedProduct("Windows License", price=125),
                 LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

MAX_PROD_AMOUNT = len(product_list)

# Create promotion catalog
second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = Store(product_list)

def show_menu():
    print("   Store Menu\n   ----------\n1. List all products in store\n"
          "2. Show total amount in store\n3. Make an order\n4. Quit")


def show_products(product_list):
    print("------------------")
    for index, product in enumerate(product_list.products, 1):
        print(f"{index}. {product.show()}")
    print("------------------")


def start(store_object):
    """ Start Function """
    while True:
        show_menu()
        user_input = input("Please choose a number: ")

        if user_input == "1":
            show_products(store_object)
            continue

        elif user_input == "2":
            print(f"Total of {store_object.get_total_quantity()} items in store")
            continue

        elif user_input == "3":
            show_products(store_object)
            print("When you want to finish order, enter empty text.")

            shop_list = []
            while True:
                try:
                    product_num_input = input("Which product # do you want? ")
                    if product_num_input.isdigit() and int(product_num_input) in range(1, MAX_PROD_AMOUNT + 1):
                        product_amount_input = int(input("What amount do you want? "))
                        product = store_object.products[int(product_num_input) - 1]

                        # For LimitedProduct
                        if isinstance(product, NonStockedProduct):
                            # No stock check for NonStockedProduct
                            shop_list.append((product, product_amount_input))
                            print("Product added to list!")
                            continue

                        # Check if stock is sufficient
                        if product.get_quantity() < product_amount_input:
                            print("Not enough stock available.")
                            continue  # Skip adding this product to the list

                        # For LimitedProduct
                        if isinstance(product, LimitedProduct) and product_amount_input > product.maximum:
                            raise ValueError(f"Cannot purchase more than {product.maximum} unit(s) of this product.")

                        # Add to shopping list if stock is sufficient
                        shop_list.append((product, product_amount_input))
                        print("Product added to list!")

                    elif product_num_input == "":
                        total_payment = store_object.order(shop_list)
                        if total_payment > 0:
                            print(f"Order made! Total payment: ${total_payment}")
                        break
                    else:
                        print("Error adding product!")
                except ValueError as e:
                    print(e)
                    continue

        elif user_input == "4":
            break


start(best_buy)