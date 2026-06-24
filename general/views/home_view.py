import json

from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse, HttpResponseNotAllowed
from sale.models import CartItemModel, CartModel
from inventory.models import Product, Category

# class Category:
#     def __init__(self,name):
#         self.name = name


# class Product:
#     def __init__(self,id,name,price,ingredients, sale_stock, category):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
#         self.sale_stock = sale_stock
#         self.category = category

# class CartItemModel:
#     def __init__(self,product_id,cart_id,price,quantity,amount):
#         self.product_id = product_id
#         self.cart_id = cart_id
#         self.price = price
#         self.quantity = quantity
#         self.amount = amount 

# class CartModel:
#     def __init__(self,user_id,total_amount):
#         self.user_id = user_id
#         self.total_amount = total_amount


class HomeView(View):
    template_name = "general/home.html"
    def get(self,request):
        categories = Category.objects.all()
        products = Product.objects.all()
        # categories = [Category("Drink"), Category("Food")]
        # products = [Product(1,"lemon soda",50, "water,lemon", 5, "Drink"),
        #             Product(2,"ginger soda",50, "water,ginger", 10, "Drink"),
        #             Product(3,"Burger",200, "200g meat, pickle, tomato, bun", 2, "Food"),
        #             Product(4,"Cheese Burger",250, "200g meat,goda cheese, pickle, tomato, bun", 2, "Food"),]
        return render(request, self.template_name, context={"categories":categories, "products":products} )
    
    # def post(self,request):
    #     user_cart = CartModel(1,0)
    #     products= request.POST.pop("csrfmiddlewaretoken")
    #     for id, quantity in products.items():
            
    #         cart_item = CartItemModel.objects.create(id , )

def add_to_cart(request):
    print(request.user)
    if request.method != 'POST':
        return HttpResponseNotAllowed('not allowed')
    
    res = json.loads(request.body)
    # print(res)
    product_id = res.get('product_id')
    quantity = res.get('quantity')

    try:
        cart = CartModel.objects.get(user_id=request.user.id)
    except:
        cart = CartModel.objects.create(user_id=request.user, total_amount=0)

    product = Product.objects.get(id=int(product_id))
    CartItemModel
    print(cart)

    # print(dir(request))

    return JsonResponse(data={'res': 'ok.'})