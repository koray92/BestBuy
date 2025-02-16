from products import Product
from store import Store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
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
                try:
                    product_num_input = input("Which product # do you want? ")
                    if product_num_input == "1":
                        product_amount_input = int(input("What amount do you want? "))
                        shop_list.append((store_object.products[0], product_amount_input))
                        print("Product added to list!")

                    elif product_num_input == "2":
                        product_amount_input = int(input("What amount do you want? "))
                        shop_list.append((store_object.products[1], product_amount_input))
                        print("Product added to list!")

                    elif product_num_input == "3":
                        product_amount_input = int(input("What amount do you want? "))
                        shop_list.append((store_object.products[2], product_amount_input))
                        print("Product added to list!")

                    elif product_num_input == "":
                        print(f"Order made! Total payment: ${store_object.order(shop_list)}")
                        break

                    elif product_num_input == "4":
                        break

                    else:
                        print("Error adding product!")
                except Exception as e:
                    print(f"An error occured: {e}")
                    break
        elif user_input == "4":
            break




start(best_buy)