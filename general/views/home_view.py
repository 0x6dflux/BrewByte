from django.shortcuts import redirect, render
from django.views import View

# from sale.models import CartModel, CartItemModel
from inventory.models import Category, Product


class HomeView(View):
    template_name = "general/home.html"

    def get(self, request):
        categories = Category.objects.all()
        products = Product.objects.all()
        print(products)
        return render(
            request,
            self.template_name,
            context={"categories": categories, "products": products, "forms": []},
        )
