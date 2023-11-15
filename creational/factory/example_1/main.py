from payment_factory import PaymentFactory

factory = PaymentFactory()
# payment = factory.create("CreditCardPayment")
# payment = factory.create("GooglePayPayment")
payment = factory.create("ApplePayPayment")
payment.pay(1000.00)