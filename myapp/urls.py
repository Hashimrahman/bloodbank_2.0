from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display/', views.display, name='display'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
]
