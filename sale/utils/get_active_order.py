from typing import List, Tuple, Optional
from sale.models import OrderModel, OrderItemModel
from client.models import User


def get_active_order(user: User) -> Optional[Tuple[OrderModel, List[OrderItemModel]]]:
    order = OrderModel.objects.filter(user_id=user, is_active=True).first()
    if order:
        order_items = OrderItemModel.objects.filter(order_id=order)
    else:
        order_items = None
    return order, order_items
