from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns for your app
    path('', views.home, name='home'),
    path('success/', views.logout_success, name='success'),

    # Registration, login, and logout URLs

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
