
import logging

logging.basicConfig(level=logging.INFO)

def login(user,password):

    if user=="admin" and password=="admin123":
        return True
    raise Exception("Invalid credentials")


def add_product(price,qty):

    return price*qty


def apply_discount(amount):

    if amount<0:
        raise ValueError("Invalid amount")

    return amount*0.9


def payment(amount):

    if amount<=0:
        raise Exception("Payment failed")

    return "Payment Successful"
