from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('conferences/', views.conferences, name='conferences'),
    path('paperpresentations/', views.paper_presentations, name='paper-presentations'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
]
