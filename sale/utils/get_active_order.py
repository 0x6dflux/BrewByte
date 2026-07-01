from typing import List, Tuple, Optional
from sale.models import OrderModel, OrderItemModel
from client.models import User


def get_active_order(user: User) -> Optional[Tuple[OrderModel, List[OrderItemModel]]]:
    order = OrderModel.objects.filter(user_id=user, is_active=True).first()
    if order:
        print("i was hereeeeeeeeeeeeeeeee")
        order_items = OrderItemModel.objects.filter(order_id=order)
        print(order_items)
    else:
        print("i was not hereeeeeeeeeeeeeeeeeeeeeee")
        order_items = None
    return order, order_items
