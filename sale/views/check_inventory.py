from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from sale.models import OrderItemModel, OrderModel
import json


class CheckInventory(LoginRequiredMixin, View):
    def post(self, request):
        my_body = json.loads(request.body)
        order = OrderModel.objects.get(id=my_body.get("order_id"))
        order_items = OrderItemModel.objects.filter(order_id=order)

        for order_item in order_items:
            if order_item.quantity > order_item.product_id.inventory_stock:
                return JsonResponse(
                    {
                        "item_product_id": order_item.product_id.id,
                        "inventory_message": f"Only {order_item.product_id.inventory_stock} items are available.",
                    },
                    status=400,
                )

        return JsonResponse({"success": True}, status=200)
