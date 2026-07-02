import json
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from activity.models import FavoriteModel
from inventory.models import Category, Product
from sale.models import CartItemModel, CartModel


class HomeView(View):
    template_name = "general/home.html"

    def get(self, request):
        categories = Category.objects.all()
        # products = Product.objects.all()
        # if current_user := request.user.id:
        #     user_favorite_products = Product.objects.filter(
        #         favoritemodel__user_id=current_user
        #     )
        # else:
        #     user_favorite_products = []
        return render(
            request,
            self.template_name,
            context={
                "categories": categories,
                # "products": products,
                # "user_favorite_products": user_favorite_products,
            },
        )

    def post(self, request):
        my_body = json.loads(request.body)

        js_request = my_body.get("request")
        if js_request and js_request == "user":
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
                "general/favorites_content.html",
                context={
                    "user_favorite_products": user_favorite_products,
                    "content": user_favorite_products,
                },
            )
        elif js_request == "products":
            categories = Category.objects.all()
            products = Product.objects.all()
            user_favorite_products = Product.objects.filter(
                favoritemodel__user_id=request.user.id
            )

            return render(
                request,
                "general/products_content.html",
                context={
                    "categories": categories,
                    "content": products,
                    "user_favorite_products": user_favorite_products,
                },
            )
        # elif js_request == "card":
        #     product_id = my_body.get("product_id")
        #     product = Product.objects.get(id=product_id)
        #     user_favorite_products = Product.objects.filter(
        #         favoritemodel__user_id=request.user.id
        #     )

        #     return render(
        #         request,
        #         "general/content.html",
        #         context={
        #             "product": product,
        #             "user_favorite_products": user_favorite_products,
        #         },
        #     )
        elif js_request == "cart":
            cart = CartModel.objects.get(user_id=request.user.id, is_active=True)
            if not cart:
                CartModel(
                    created_by=request.user,
                    updated_by=request.user,
                    user_id=request.user.id,
                ).save()

            cart_items = CartItemModel.objects.filter(cart_id=cart.pk)
            return render(
                request,
                "general/cart_items.html",
                context={"cart_items": cart_items},
            )

        product_id = my_body.get("product_id")
        if product_id:
            product_id_value = my_body.get("value")  # product_id is an int object

            cart, is_cart_created = CartModel.objects.get_or_create(
                created_by=request.user,
                updated_by=request.user,
                user_id=request.user,
            )

            cart_item, is_cart_item_created = CartItemModel.objects.get_or_create(
                created_by=request.user,
                updated_by=request.user,
                product_id=(current_product := Product.objects.get(id=product_id)),
                cart_id=cart,
                price=current_product.price,
            )

            user_favorite_products = Product.objects.filter(
                favoritemodel__user_id=request.user.id
            )

            if is_cart_item_created:
                if product_id_value < 0:
                    cart_item.delete()
                    # return HttpResponse(0)
                else:
                    cart_item.quantity = 1
                    cart_item.amount = cart_item.price * cart_item.quantity
                    current_product.sale_stock -= 1
                    cart_item.save()
                    current_product.save()
                    # return HttpResponse(1)

                print("*** cart item quantity in if:", cart_item.quantity)

                return render(
                    request,
                    "general/content.html",
                    context={
                        "product": current_product,
                        "cart_item_quantity": cart_item.quantity,
                        "user_favorite_products": user_favorite_products,
                    },
                )
            else:
                cart_item.quantity += product_id_value
                cart_item.amount = cart_item.price * cart_item.quantity
                current_product.sale_stock -= product_id_value
                # if user adds a product to their cart, sale_stock shall be reduced
                # if user removes a product from their cart, sale_stock shall be increased

                cart_item.save()
                current_product.save()

                if cart_item.quantity <= 0:
                    cart_item.delete()
                    # return HttpResponse(0)

                # return HttpResponse(cart_item.quantity)

                print("*** cart item quantity in else:", cart_item.quantity)
                return render(
                    request,
                    "general/content.html",
                    context={
                        "product": current_product,
                        "cart_item_quantity": cart_item.quantity,
                        "user_favorite_products": user_favorite_products,
                    },
                )

            # return render(
            #     request,
            #     "general/change_favorites.html",
            #     context={"user_favorite_products": user_favorite_products},
            # )
