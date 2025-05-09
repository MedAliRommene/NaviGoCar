from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('cars/', views.cars, name='cars'),
    path('car/<int:car_id>/', views.car_single, name='car_single'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
]