from product import Product

class Store(object):
    def __init__(self, products, address, owner):
        self.products = products
        self.address = address
        self.owner = owner
    
    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        self.products.remove(product)
        return self

    def inventory(self):
        for product in self.products:
            product.display_info()
        return self

if __name__ == '__main__':
    store1 = Store([Product(200,'sadf',22,'dsafd',22)],'sfa','dsaf')
    store1.inventory()