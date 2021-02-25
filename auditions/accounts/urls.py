from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='landing'),
    path('register/', views.registerview, name='register'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
]
