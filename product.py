class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'for sale'
    
    def __repr__(self):
        return "<Product object: {}\nPrice: {}>".format(self.name, self.price)
    
    def sell(self):
        self.status = 'sold'
        return self

    def add_tax(self, tax):
        return self.price * (1 + tax)

    def return_product(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'in box like new':
            self.status = 'for sale'
        elif reason == 'opened':
            self.status = 'used'
            self.price *= 0.8
        return self

    def display_info(self):
        print 'Price: $' + str(self.price)
        print 'Name: ' + self.name
        print 'Weight: ' + str(self.weight)
        print 'Brand: ' + self.brand
        print 'Cost: $' + str(self.cost)
        print 'Status: ' + self.status
        return self

if __name__ == '__main__':
    prod1 = Product(200,'sadf',22,'dsafd',22)
    prod1.display_info()