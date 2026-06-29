import json

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from activity.models import FavoriteModel
from inventory.models import Category, Product

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
        my_body = json.loads(request.body)

        js_request = my_body.get("request")
        if js_request:
            if request.user.id:
                return HttpResponse("OK")
            return HttpResponse("To add a product in your favorites, please sign in.")

        star_product_id = my_body.get("star_product_id")
        if star_product_id and (current_user := request.user):
            user_favorite_products = Product.objects.filter(
                favoritemodel__user_id=current_user.id
            )
            if Product.objects.get(id=star_product_id) in user_favorite_products:
                FavoriteModel.objects.get(
                    user_id=current_user.id,
                    product_id=star_product_id,
                ).delete()
                return HttpResponse("✩")
            else:
                FavoriteModel(
                    user_id=current_user,
                    product_id=Product.objects.get(id=star_product_id),
                    created_by=current_user,
                    updated_by=current_user,
                ).save()
                return HttpResponse("🌟")

        js_request = my_body.get("update")
        if js_request == "favorites":
            user_favorite_products = Product.objects.filter(
                favoritemodel__user_id=request.user.id
            )

            return render(
                request,
                "general/favorites.html",
                context={
                    "user_favorite_products": user_favorite_products,
                },
            )

        product_id = my_body.get("product_id")
        if product_id:
            product_id_value = my_body.get("value")  # product_id is an int object

            return HttpResponse(f"{product_id_value}")

            # return render(
            #     request,
            #     "general/change_favorites.html",
            #     context={"user_favorite_products": user_favorite_products},
            # )
