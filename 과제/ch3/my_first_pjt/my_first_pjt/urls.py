from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/", views.articles, name="articles"),
    path("data_throw/", views.data_throw, name="data_throw"),
    path("hello/", views.hello),
]