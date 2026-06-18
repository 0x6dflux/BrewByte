from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from client.forms import ProfileForm


@login_required
def profile_edit_view(request: HttpRequest) -> HttpResponse:
    template_name = 'client/profile.html'
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'پروفایل با موفقیت به‌روزرسانی شد!')
            return redirect('home')  # تغییر از 'client:profile_edit' به 'home'
        else:
            messages.error(request, 'لطفاً خطاها را برطرف کنید.')
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, template_name, {'form': form})
