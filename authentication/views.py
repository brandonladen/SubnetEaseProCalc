from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import userprofileform

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #manualy authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            print("Successfully logged in")
            return redirect('home')
        else:
            print("Invalid username or password")
            messages.error(request, "Invalid username or password")
        
    return render(request, "login.html")


def update_profile(request):
    if request.method == 'POST':
        form = userprofileform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = userprofileform(instance=request.user)
    context = {
        'form': form
    }
    print(form)
    return render(request, 'core/base.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')