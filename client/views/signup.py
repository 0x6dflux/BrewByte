from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib import messages
from client.forms import SignUpForm
from datetime import date


class SignUpView(View):
    template_name = 'client/signup.html'
    
    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            login(request, user)
            messages.success(request, 'ثبت‌نام با موفقیت انجام شد!')
            
            # birth_date = user.birth_date
            # if birth_date:
            #     today = date.today()
            #     if birth_date.day == today.day and birth_date.month == today.month:
            #         messages.info(request, '🎉 تولدت مبارک! 20% تخفیف دریافت کردی!')
            
            return redirect('client:profile_edit')
        
        messages.error(request, 'ثبت نام با خطا مواجه شد دوباره تلاش کنید')
        return render(request, self.template_name, {'form': form})
