from django.views import View
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from client.models import Address
from sale.services import CheckoutService
from client.services import ClientCheckoutService
from sale.utils import get_active_order


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
        if address_id := request.POST.get("address"):
            order, _ = get_active_order(request.user)
            address = Address.objects.get(id=address_id)
            order.address_id = address
            order.save()
            return redirect("sale:finalize_order")

        messages.error(request, "Please Select Address!")
        return redirect("sale:create_order")
