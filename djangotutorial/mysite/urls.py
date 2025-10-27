# mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # YALNIZ BİR DƏFƏ OLMALIDIR:
    path("polls/", include("polls.urls")), 
    path("admin/", admin.site.urls),
    # Əgər başqa yerdə təkrar qeydiyyat yoxdursa, problem həll olunacaq.
]