from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from articles import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index, name="index"),
    path("articles/", include("articles.urls")),
    path("users/", include("users.urls")),
    path("accounts/", include("accounts.urls")),
    

    path("data_throw/", views.data_throw, name= "data_throw"),
    path("data_catch/", views.data_catch, name= "data_catch"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)