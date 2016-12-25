from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# home
def home(request):
    return redirect(restaurant_home)

# Only the signed in users could logout
@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/home.html')