from django.contrib import admin
from django.urls import path
from location.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', index),
]
