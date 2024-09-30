from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
import uuid

# Create your models here.

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        # Your custom logic for creating a regular user
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        # Your custom logic for creating a superuser
        user = self.create_user(username, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    

class Account(AbstractBaseUser, PermissionsMixin):
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)
    join_date = models.DateTimeField(default=timezone.now, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    last_login_date = models.DateTimeField(null=True, blank=True)

    groups = models.ManyToManyField(Role, related_name='user_accounts')
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='user_accounts'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
class Product(models.Model):

    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='product/', null=True, blank=True)

   

    def __str__(self):
        return self.name

