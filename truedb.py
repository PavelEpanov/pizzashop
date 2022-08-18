import pickle
from main import PizzaShop

shop = PizzaShop()

pickle.dump(shop, open("shopfile.pkl", "wb"))

obj = pickle.load(open("shopfile.pkl", "rb"))

#obj.order("LSP")
