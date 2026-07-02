from django.db import transaction

from sale.models import CartItemModel
from sale.utils import (
    get_active_cart,
    get_active_order,
    create_order,
    create_order_items,
    deactivate_cart,
)


class CheckoutService:
    @staticmethod
    def checkout_active_order_and_items(user):
        order, order_items = get_active_order(user)
        if order and not order_items:
            cart_items = CartItemModel.objects.filter(cart_id=order.cart_id)
            with transaction.atomic():
                order_items = create_order_items(order, cart_items)
        elif not order and not order_items:
            cart, cart_items = get_active_cart(user)
            if not cart or not cart_items:
                raise ValueError("No Active Carts Contains Items!")

            with transaction.atomic():
                order = create_order(user, cart)
                order_items = create_order_items(order, cart_items)
                deactivate_cart(cart)
        return order, order_items
