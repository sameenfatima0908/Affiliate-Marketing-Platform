from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from . forms import UserRegisterForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hi {username}, your account has been successfully created")
            return redirect('home')  # Redirect to the 'home' URL name
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

def pricing_view(request):
    return render(request, 'pricing.html', {})

def profile(request):
    return render(request, 'profile.html', {})

def logout(request):
    return render(request, 'logout.html', {})

def privacy(request):
    return render(request, 'privacy.html', {})
