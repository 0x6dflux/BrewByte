from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from sale.services import CheckoutService
from client.services import ClientCheckoutService


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
