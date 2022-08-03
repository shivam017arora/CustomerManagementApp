from nturl2path import url2pathname
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name='accounts'

urlpatterns = [
    path('', views.products, name='products'),
    path('login/', views.loginView, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutView, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_order/<str:pk>/', views.create_order, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('remove_order/<str:pk>/', views.remove_order, name='remove_order'),
]
