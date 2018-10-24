class pdts():
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.price = price
        self.name = name
        self.stock = stock

    def addpdts(self):
        inventory = {   
        'product_id': self.product_id,
        'price': self.price,
        'name': self.name,
        'stock': self.stock
        }
        return inventory
