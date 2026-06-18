from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from client.forms import SignInForm
from datetime import date


class SignInView(View):
    template_name = 'client/signin.html'
    
    def get(self, request):
        form = SignInForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            
            user = authenticate(request, phone_number=phone_number, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'خوش اومدی {user.first_name}!')
                
                # بررسی تخفیف تولد
                # birth_date = user.birth_date
                # if birth_date:
                #     today = date.today()
                #     if birth_date.day == today.day and birth_date.month == today.month:
                #         messages.info(request, '🎉 تولدت مبارک! 20% تخفیف امروز!')
                
                return redirect('client:profile_edit')
            else:
                messages.error(request, 'شماره تلفن یا رمز عبور اشتباه است.')
        
        return render(request, self.template_name, {'form': form})
