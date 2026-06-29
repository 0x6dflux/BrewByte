from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from sale.models import OrderModel, OrderItemModel, CartModel, CartItemModel
from client.models import User
from general.models import BusinessSetting
from sale.utils import get_tax_ratio

@login_required
class CreateOrder(View):
    template_name = 'client/signup.html'
    tax_ratio = get_tax_ratio()
    def get(self, request):
        user = request.user
        try:
            order  = OrderModel.objects.filter(user_id = user, is_active = True).first()
            if order:
                order_items = OrderItemModel.objects.filter(order_id = order)
                if order_items:
                    return render(
                                request,
                                self.template_name,
                                context= {"active_order": active_order ,
                                            "active_order_items":active_order_items})
            else:
                cart = CartModel.objects.filter(user_id = target_user, is_active = True)
                target_cart_items = CartItemModel.objects.filter(cart_id = target_cart)
                if len(target_cart_items) != 0:
                    active_order = OrderModel.objects.create(
                        user_id = target_user,
                        cart_id = target_cart,
                        total_amount = target_cart.total_amount,
                        discount = 0,
                        discounted_amount = target_cart.total_amount,
                        tax = target_cart.total_amount * (self.tax_ratio / 100 ),
                        taxed_amount = target_cart.total_amount,
                    )
                    active_order_items = []
                    for cart_item in target_cart_items:
                        order_item = OrderItemModel.objects.create(
                            order_id = active_order,
                            product_id = cart_item.product_id,
                            quantity = cart_item.quantity,
                            price = cart_item.price,
                            amount = cart_item.amount
                        )
                        active_order_items.append(order_item)
                    return render(
                        request,
                        self.template_name,
                        context= {"active_order": active_order ,
                                    "active_order_items":active_order_items })
                else:
                    error = "No Items In Your Cart!"
                    return render(
                        request,
                        self.template_name,
                        context= {"error": error })
            except CartModel.DoesNotExist:
                error = "No Cart Found!"
                return render(
                    request,
                    self.template_name,
                    context= {"error": error })

    



            
