from django.contrib import admin
from django.urls import path
from .views import UserViewSet
urlpatterns = [
    path('customer/', UserViewSet.as_view()),
    path('customer/<int:pk>',UserViewSet.as_view())
]