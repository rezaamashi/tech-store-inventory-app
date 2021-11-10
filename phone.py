from item import Item


class Phone(Item):
    pay_rate = 0.75

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributers / methods from parent
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert (
            broken_phones >= 0
        ), f"Broken Phones: {quantity} ( must not be negative or zero )"

        # Assign to self object
        self.broken_phones = broken_phones
