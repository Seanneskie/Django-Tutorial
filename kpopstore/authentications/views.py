# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import Role, Account

def index(request):
    context = {}
    return render(request, 'public/index.html', context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.save()
            login(request, user)
            if user.role.role == 'Customer':
                return redirect('customer_home')
            elif user.role.role == 'Supplier':
                return redirect('supplier_home')
    else:
        form = RegisterForm()
    return render(request, 'public/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role.role == 'Customer':
                    return redirect('customer_home')
                elif user.role.role == 'upplier':
                    return redirect('supplier_home')
    else:
        form = LoginForm()
    return render(request, 'public/login.html', {'form': form})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def customer_home_view(request):
    if request.user.role.role != 'Customer':
        return redirect('index')
    context = {}
    return render(request, 'customer/home.html', context)

@login_required(login_url='login')
def supplier_home_view(request):
    if request.user.role.role != 'Supplier':
        return redirect('index')
    context = {}
    return render(request, 'supplier/home.html', context)