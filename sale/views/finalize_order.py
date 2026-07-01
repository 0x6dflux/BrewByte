from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from sale.utils import get_active_order


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
