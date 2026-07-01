from django.views import View
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from sale.models import OrderItemModel
from sale.services import CheckoutService
from client.services import ClientCheckoutService
from sale.utils import calculate_price
import json


class CreateOrder(LoginRequiredMixin, View):
    template_name = "sale/new_order.html"

    def get(self, request):
        try:
            order, order_items = CheckoutService.checkout_active_order_and_items(
                request.user
            )
            addresses = ClientCheckoutService.checkout_address(request.user)
        except ValueError as e:
            messages.error(request, str(e))
            return redirect("general:home")

        return render(
            request,
            self.template_name,
            {
                "order": order,
                "order_items": order_items,
                "addresses": addresses,
            },
        )

    def post(self, request):
        my_body = json.loads(request.body)

        order_item_id = my_body.get("item_id")
        value = int(my_body.get("value"))
        if order_item_id and value:
            order_item = OrderItemModel.objects.get(id=order_item_id)
            if order_item.quantity + value >= 0:
                order_item.quantity += value
                order_item.save()
                calculate_price(order_item.order_id)

            return JsonResponse(
                {
                    "quantity": order_item.quantity,
                    "amount": str(order_item.amount),
                    "total_amount": str(order_item.order_id.total_amount),
                    "discounted_amount": str(order_item.order_id.discounted_amount)
                    or 0,
                    "tax": str(order_item.order_id.tax),
                    "taxed_amount": str(order_item.order_id.taxed_amount),
                }
            )
