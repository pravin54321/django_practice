from django.contrib import admin
from django.urls import path
from testApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('httest/',views.wish)
]