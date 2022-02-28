from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    
    path('create_Order/', views.createOrder, name='create_Order'),
    path('update_Order/<str:pk_id>/', views.updateOrder, name='update_Order'),
    path('delete_Order/<str:pk_test>/', views.deleteOrder, name='delete_Order'),
]

