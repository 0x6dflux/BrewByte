from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


def sign_out_view(request):
    """Handle user logout"""
    logout(request)
    messages.success(request, 'شما با موفقیت از سیستم خارج شدید.')
    return redirect('client:signin')
