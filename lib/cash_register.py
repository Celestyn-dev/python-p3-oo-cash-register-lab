#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount              # percentage, like 20 for 20%
        self.total = 0                        # running total price
        self.items = []                       # list of item names
        self.last_transaction = 0             # amount of the most recent item(s)

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def get_items(self):
        return self.items

    def void_last_transaction(self):
        self.total -= self.last_transaction


    def get_items(self):
        return self.items
    def void_last_transaction(self):
        self.total -= self.last_transaction

