import json

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from inventory.models import Category, Product

# from activity.models import FavoriteModel

# from sale.models import CartItemModel, CartModel


class HomeView(View):
    template_name = "general/home.html"

    def get(self, request):
        categories = Category.objects.all()
        products = Product.objects.all()
        if current_user := request.user.id:
            user_favorite_products = Product.objects.filter(
                favoritemodel__user_id=current_user
            )
        else:
            user_favorite_products = []
        return render(
            request,
            self.template_name,
            context={
                "categories": categories,
                "products": products,
                "user_favorite_products": user_favorite_products,
            },
        )

    def post(self, request):
        print(request.body)
        my_body = json.loads(request.body)
        print(my_body)
        product_id = my_body.get("product_id")
        product_id_value = my_body.get("value")
        print(product_id)
        print(product_id_value)

        return HttpResponse(f"{product_id_value}")
