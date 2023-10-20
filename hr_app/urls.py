
from django.contrib import admin
from django.urls import path, include

from .views import index, about_me

urlpatterns = [
   path('', index),
   path('about/<slug:what>', about_me),


]



