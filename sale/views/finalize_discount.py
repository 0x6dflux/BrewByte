from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from sale.models import DiscountModel, OrderModel
from sale.utils import calculate_price
import json


class FinalizeDiscount(LoginRequiredMixin, View):
    def post(self, request):
        my_body = json.loads(request.body)
        order = OrderModel.objects.get(id=my_body.get("order_id"))
        discount_code = my_body.get("code")
        discount = DiscountModel.objects.filter(
            code=discount_code, user_id=order.user_id, is_active=True
        ).first()
        if not discount:
            return JsonResponse(
                {"success": False, "message": "Invalid Discount Code!"}, status=400
            )
        if order.total_amount < discount.order_min_amount:
            return JsonResponse(
                {"success": False, "message": "Insufficient order total amount!"},
                status=400,
            )
        if discount.expire_datetime < timezone.now():
            return JsonResponse(
                {"success": False, "message": "Discount has expired!"}, status=400
            )

        order.discount = min(order.total_amount * discount.percent, discount.max_amount)
        calculate_price(order)
        order.save()

        return JsonResponse(
            {
                "success": True,
                "discount": str(order.discount),
                "discounted_amount": str(order.discounted_amount),
                "tax": str(order.tax),
                "taxed_amount": str(order.taxed_amount),
            }
        )
