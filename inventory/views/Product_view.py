from django.db.models import Avg
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from activity.models import CommentModel
from general.models.business_settings import BusinessSetting
from inventory.models import Ingredient, Product


class ProductView(View):
    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        ingredients = Ingredient.objects.filter(product_id=id)
        comments = CommentModel.objects.filter(product_id=id)

        return render(
            request,
            "inventory/product.html",
            context={
                "ingredients": ingredients,
                "comments": comments,
                "overall_score": Product.objects.get(id=id).average_score,
            },
        )

    def post(self, request: HttpRequest, id: int) -> HttpResponse:
        score = request.POST.get("score")
        description = request.POST.get("description")

        CommentModel(
            created_by=(current_user := request.user),
            updated_by=current_user,
            user_id=current_user,
            responsible_user_id=BusinessSetting.objects.all()
            .first()
            .default_comment_responsible_user_id,
            product_id=Product.objects.get(id=id),
            description=description,
            score=score,
        ).save()

        comments_avg = CommentModel.objects.filter(product_id=id).aggregate(
            Avg("score")
        )
        product = Product.objects.get(id=id)
        product.average_score = comments_avg.get("score__avg")
        product.save()

        return redirect("inventory:product", id=id)
