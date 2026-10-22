from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('grooming/', views.grooming, name='grooming'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]