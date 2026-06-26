from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from client.models import Address
from client.forms import AddressForm
#from django.http import JsonResponse #


@login_required
def address_add_view(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user_id = request.user.id  
            address.latitude = 0.0
            address.longitude = 0.0
            address.save()
            messages.success(request, "آدرس با موفقیت ذخیره شد.")
            return redirect('client:profile_edit')
        else:
            print(f"Form errors: {form.errors}") 
            return render(request, 'client/address_form.html', {'form': form})

    form = AddressForm()
    return render(request, 'client/address_form.html', {'form': form})


@login_required
def address_edit_view(request, id):
    address = get_object_or_404(Address, id=id, user_id=request.user.id)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.user_id = request.user.id  
            address.save()
            messages.success(request, "Address updated successfully.")
            return redirect('client:profile_edit')
        else:
            print(f"Edit Form Errors: {form.errors}")
            messages.error(request, "Error updating address. Please check the details.")
            return render(request, 'client/address_form.html', {'form': form})
    else:
        form = AddressForm(instance=address)
        
    return render(request, 'client/address_form.html', {'form': form})


@login_required
def address_delete_view(request, id):
    address = get_object_or_404(Address, id=id, user_id=request.user.id) 
    address.delete()
    messages.success(request, "Address has been deleted successfully.")
    return redirect('client:profile_edit')