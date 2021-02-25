
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('response/',include('response.urls')),
    path('administrator/',include('administrator.urls')),
]
