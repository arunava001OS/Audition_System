
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index,name="index"),
   path('get_question/',views.get_question,name="get-question"), 
]
