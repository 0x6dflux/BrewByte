from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib import messages

from client.forms import SignUpForm


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
            user.save()

            login(request, user)
            messages.success(request, "You Signed Up Successfully!")

            # birth_date = user.birth_date
            # if birth_date:
            #     today = date.today()
            #     if birth_date.day == today.day and birth_date.month == today.month:
            #         messages.info(request, "Happy Birthday <3")

            return redirect("client:signin")

        messages.error(request, "Unsuccessful, Please Try Again!")
        return render(request, self.template_name, {"form": form})

    # def save(self, *args, **kwargs):
    #     self.set_user_id()
    #     self.create_customer_profile()
    #     super().save(*args, **kwargs)

    # def set_user_id(self):
    #     if not self.user_code:
    #         last_user = User.objects.order_by("-id").first()
    #         if last_user:
    #             last_seq = int(last_user.user_code.split("-")[-1])
    #             new_seq = last_seq + 1
    #         else:
    #             new_seq = 1

    #         self.user_code = f"USR-{new_seq:04d}"

    # def create_customer_profile(self):
    #     from client.models import CustomerProfile

    #     try:
    #         customer_profile = CustomerProfile.objects.get(user_id=self)
    #     except CustomerProfile.DoesNotExist:
    #         last_profile = CustomerProfile.objects.order_by("-id").first()
    #         if last_profile:
    #             last_seq = int(last_profile.customer_id.split("-")[-1])
    #             new_seq = last_seq + 1
    #         else:
    #             new_seq = 1
    #         CustomerProfile.objects.create(
    #             user_id=self,
    #             customer_id=f"CPI-{new_seq:04d}",
    #             referral_code=f"CRC{self.phone_number[-4:]}",
    #             is_active=True,
    #         )
