class Item:
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


item1 = Item("Phone", 100, 8)

item2 = Item("Laptop", 1000, 3)


print(item1.calculate_total_price())
print(item2.calculate_total_price())
