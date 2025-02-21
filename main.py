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


def start(store_object):
    """ Start Function """

    while True:
        show_menu()
        user_input = input("Please choose a number: ")

        if user_input == "1":
            print("------------------")
            for product in store_object.products:
                print(product.show())
            print("------------------")
            continue


        elif user_input == "2":
            print(f"Total of {store_object.get_total_quantity()} items in store")
            continue


        elif user_input == "3":
            print("------------------")
            for product in store_object.products:
                print(product.show())
            print("------------------")
            print("When you want to finish order, enter empty text.")


            shop_list = []
            while True:

                product_num_input = input("Which product # do you want? ")
                if product_num_input.isdigit() and int(product_num_input) in range(1, MAX_PROD_AMOUNT + 1):
                    product_amount_input = int(input("What amount do you want? "))
                    shop_list.append((store_object.products[int(product_num_input) - 1], product_amount_input))
                    print("Product added to list!")


                elif product_num_input == "":
                    print(f"Order made! Total payment: ${store_object.order(shop_list)}")
                    break

                else:
                    print("Error adding product!")


        elif user_input == "4":
            break


start(best_buy)