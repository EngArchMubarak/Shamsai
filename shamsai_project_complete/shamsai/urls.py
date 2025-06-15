from django.contrib import admin
from django.urls import path
from shamsapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.welcome, name="welcome"),
]
