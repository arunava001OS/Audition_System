from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='dashboard'),
    path('response_detail/<int:id>',views.response_detail,name='response_detail'),

]
