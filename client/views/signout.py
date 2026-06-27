from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


def sign_out_view(request):
    """Handle user logout"""
    logout(request)
    messages.success(request, "You Signed Out Successfully!")
    return redirect("general:home")
