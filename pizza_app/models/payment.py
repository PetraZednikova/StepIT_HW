class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)

class CreditCardPayment:
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card")

class PayPalPayment:
    def pay(self, amount):
        print(f"Paying {amount} using PayPal")