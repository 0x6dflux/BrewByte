from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from client.forms import UserProfileForm, ProfileDetailsForm
from client.models import Address, CustomerProfile

class ProfileEditView(LoginRequiredMixin, View):
    
    def get(self, request):
        profile, created = CustomerProfile.objects.get_or_create(user_id=request.user)
        user_form = UserProfileForm(instance=request.user)
        profile_form = ProfileDetailsForm(instance=profile)
        context = {
            "user_form": user_form,
            "profile_form": profile_form,
            "addresses": Address.objects.filter(user_id=request.user),
            "profile": profile,
        }
        return render(request, "client/profile.html", context)

    def post(self, request):
        profile, created = CustomerProfile.objects.get_or_create(user_id=request.user)
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_form = ProfileDetailsForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Changes saved successfully.")
            return redirect("general:home")
        
        context = {
            "user_form": user_form,
            "profile_form": profile_form,
            "addresses": Address.objects.filter(user_id=request.user),
            "profile": profile,
        }
        return render(request, "client/profile.html", context)
