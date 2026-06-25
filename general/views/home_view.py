from django.shortcuts import render, redirect
from django.views import View
from sale.models import CartModel, CartItemModel
from inventory.models import Product, Category
from activity.models import favorite_model



class HomeView(View):
    template_name = "general/home.html"
    def get(self,request):
        print(request.user.id)
        categories = Category.objects.all()
        products = Product.objects.all()
        if request.user.id:
            user_favorite_products = Product.objects.filter(favorite_model__user_id = request.user.id)
        else:
            user_favorite_products = False
        return render(request, self.template_name, context={"categories":categories, "products":products, "user_favorite_products":user_favorite_products})

    def post(self,request):
        return redirect(request.META.get('HTTP_REFERER'))




    


    