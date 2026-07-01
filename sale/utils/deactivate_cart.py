from sale.models import CartModel


def deactivate_cart(cart: CartModel):
    cart.is_active = False
    cart.save()
