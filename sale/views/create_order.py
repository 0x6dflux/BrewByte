from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from sale.models import OrderModel, OrderItemModel, CartModel, CartItemModel
from client.models import User
from general.models import BusinessSetting

class CreateOrder(request):
    template_name = 'client/signup.html'
    tax_ratio = BusinessSetting.objects.first().default_tax_ratio
    def get(self, request, userid, cartid):
        target_user = User.objects.get(id = userid)
        try:
            active_order  = OrderModel.objects.get(user_id = target_user, is_active = True)
            active_order_items = OrderItemModel.objects.filter(order_id = active_order)
            return render(
                        request,
                        self.template_name,
                        content= {"active_order": active_order ,
                                    "active_order_items":active_order_items })
        except OrderModel.DoesNotExist:
            try:
                target_cart = CartModel.objects.get(id = cartid, is_active = True)
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
                    for cart_item in target_cart_items:
                        order_item = OrderItemModel.objects.create(
                            order_id = active_order,
                            product_id = cart_item.product_id,
                            quantity = cart_item.quantity,
                            price = cart_item.price,
                            amount = cart_item.amount
                        )
            
