from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit/', views.edit_profile, name='edit'),
    path('change_password/', views.change_password, name='change_password')
]