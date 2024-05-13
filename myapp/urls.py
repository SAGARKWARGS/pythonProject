
from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about, name='about-us'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('feature/', views.feature, name='feature'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('appointment/', views.appointment, name='appointment'),
    path('header/', views.header, name='header'),
]
