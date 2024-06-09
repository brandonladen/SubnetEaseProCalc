from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import userprofileform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
         # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup_user')
        
         # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('signup_user')
        
         # Create the user object
        user = User.objects.create_user(username=username, 
                                        email=email,
                                        password=password)
        user.save()        
        messages.success(request, "Successfully signed up. You can now login.")
        return redirect('login')
            
    return render(request, "signup.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # manualy authenticate user
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')
