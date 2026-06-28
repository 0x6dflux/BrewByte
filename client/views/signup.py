from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib import messages

from client.forms import SignUpForm
from client.utils import set_user_code, create_customer_profile


class SignUpView(View):
    template_name = "client/signup.html"

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            set_user_code(user)
            user.save()

            login(request, user)
            messages.success(request, "You Signed Up Successfully!")

            create_customer_profile(user)

            # birth_date = user.birth_date
            # if birth_date:
            #     today = date.today()
            #     if birth_date.day == today.day and birth_date.month == today.month:
            #         messages.info(request, "Happy Birthday <3")

            return redirect("client:signin")

        messages.error(request, "Unsuccessful, Please Try Again!")
        return render(request, self.template_name, {"form": form})
