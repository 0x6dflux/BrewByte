from typing import List, Optional
from sale.models import OrderItemModel, OrderModel, CartItemModel


def create_order_items(
    order: OrderModel, cart_items: List[CartItemModel]
) -> Optional[List[OrderItemModel]]:
    order_items = [
        OrderItemModel(
            order_id=order,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity,
            price=cart_item.price,
            amount=cart_item.amount,
        )
        for cart_item in cart_items
    ]
    OrderItemModel.objects.bulk_create(order_items)

    return order_items
