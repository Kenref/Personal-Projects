class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than 0!"
        assert quantity >= 0, f"Price {quantity} is not greater than 0!"


        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Phone", -100, 2)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())