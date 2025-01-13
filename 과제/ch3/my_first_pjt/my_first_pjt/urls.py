from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index),
    path("users/", views.users),
    path("hello/", views.hello),
]