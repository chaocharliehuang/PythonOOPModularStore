from store import Store
from product import Product

prod22 = Product(22,'sadf',45,'dsafd',10)
prod33 = Product(33,'sadf',45,'dsafd',10)
store = Store([prod22, prod33], '123 maple dr', 'Dr. Gallo')
store.inventory()