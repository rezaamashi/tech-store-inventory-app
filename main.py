import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% Discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} must not be negative or zero"
        assert quantity >= 0, f"Quantity {quantity} must not be negative or zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 4.0, 9.0, etc.
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name }', '{self.price}', '{self.quantity}')"


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributers / methods from parent
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert (
            broken_phones >= 0
        ), f"Broken Phones: {quantity} ( must not be negative or zero )"

        # Assign to self object
        self.broken_phones = broken_phones

        # Actions to execute
        Phone.all.append(self)


phone1 = Phone("jscPhonev10", 700, 5, 3)
print(f"the total price of {phone1.name} is: {phone1.calculate_total_price()}")
phone2 = Phone("jscPhonev20", 900, 5, 2)
