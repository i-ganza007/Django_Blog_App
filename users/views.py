from bson import is_valid
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created , you can login now!')
            return redirect('login')

    else:
        form = UserRegistration()
    return render(request,'users/register.html',{'form':form})  

@login_required 
def profile(request):
    return render(request,'users/profile.html')
