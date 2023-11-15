from .payment import Payment


class ApplePayPayment(Payment):

    def pay(self, amount: float):
        print(f"Successfully paid ${amount} to merchant using Apple Pay.")
