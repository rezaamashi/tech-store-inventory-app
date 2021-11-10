class Item:
    pay_rate = 0.8  # The pay rate after 20% Discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} must not be negative or zero"
        assert quantity >= 0, f"Quantity {quantity} must not be negative or zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 8)
item1.apply_discount()
print(item1.price)


item2 = Item("Laptop", 1000, 5)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
