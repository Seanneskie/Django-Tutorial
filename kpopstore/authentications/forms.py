from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account, Role, Product

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2', 'role']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Account 
        fields = ['username', 'password']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'image']