from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.db import transaction

from sale.utils import get_active_order, get_notification_responsible_user
from activity.models import NotificationModel
from client.models import User
from inventory.models import Product


class FinalizeOrder(LoginRequiredMixin, View):
    template_name = "sale/finalize_order.html"

    def get(self, request):
        order, order_items = get_active_order(request.user)

        if not order:
            messages.error(request, "No active order found.")
            return redirect("sale:create_order")

        addresse = order.address_id

        context = {
            "order": order,
            "order_items": order_items,
            "addresse": addresse,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        order, order_items = get_active_order(request.user)
        responsible_user = get_notification_responsible_user()
        if not responsible_user:
            responsible_user = User.objects.filter(is_superuser=True).first()
        notification = NotificationModel.objects.create(
            responsible_user_id=responsible_user,
            order_id=order,
            description=f"A new order is submited! {order}",
            is_seen=False,
        )
        with transaction.atomic():
            products = []
            for order_item in order_items:
                order_item.product_id.inventory_stock -= order_item.quantity
                products.append(order_item.product_id)
            Product.objects.bulk_update(products, ["inventory_stock"])
            order.is_active = False
            order.save()
        return redirect("general:home")
