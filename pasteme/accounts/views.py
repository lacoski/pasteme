from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm
# Create your views here.
def login_view(request):        
    form = UserLoginForm(request.POST or None)
    next = request.GET.get('next')
    print(form.errors)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        #print(username)
        #print(password)
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request, user.is_authenticated)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, 'accounts/login.html', {"form":form})



def registered_view(request):    
    return render(request, 'accounts/registered.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')