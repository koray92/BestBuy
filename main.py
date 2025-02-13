from products import Product
from store import Store

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

best_buy = Store([bose, mac])
price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
print(f"Order cost: {price} dollars.")