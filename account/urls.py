from os import name
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'account'
# If app_name is set, auth_view can't find corresponding url and raise reverse not found

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    path('<str:username>/profile/', views.view_profile, name='view_profile'), # View someone else's profile
]