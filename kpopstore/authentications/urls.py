from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('customer/home', views.customer_home_view, name='customer_home'),
    path('supplier/home', views.supplier_home_view, name='supplier_home')
]

