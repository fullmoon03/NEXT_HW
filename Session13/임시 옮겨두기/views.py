from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Profile
# Create your views here.

def home(request):
    if profile = Profile.objects.filter(user = request.user)

def new(request):
    if request.method == 'POST':
        Profile.objects.create(
            user = request.user,
            age = request.POST['age'],
        )
        return redirect('accounts:new')
    return  render(request, 'accounts/home.html', {'profile': profile})






    return render(request, 'accounts/home.html')
