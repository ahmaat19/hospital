from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('signup/', views.Signup, name='Signup'),
    path('change-password/', views.ChangePassword, name='Change_password'),
    path('reset-password/', views.ResetPassword, name='Reset_password'),
]
