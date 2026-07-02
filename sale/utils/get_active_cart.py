from typing import List, Optional, Tuple
from client.models import User
from sale.models import CartModel, CartItemModel


def get_active_cart(user: User) -> Optional[Tuple[CartModel, List[CartItemModel]]]:
    cart = CartModel.objects.filter(user_id=user, is_active=True).first()
    if cart:
        cart_items = CartItemModel.objects.filter(cart_id=cart)
    else:
        cart_items = []
    return cart, cart_items
