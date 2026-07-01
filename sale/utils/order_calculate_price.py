from sale.models import OrderModel, OrderItemModel
from sale.utils import get_tax_ratio
from decimal import Decimal
from django.db.models import Sum


def calculate_price(order: OrderModel):

    order.total_amount = OrderItemModel.objects.filter(order_id=order).aggregate(
        total=Sum("amount")
    )["total"] or Decimal("0.0")
    order.discounted_amount = order.total_amount - order.discount
    order.tax = order.discounted_amount * get_tax_ratio()
    order.taxed_amount = order.discounted_amount + order.tax
    order.save()
