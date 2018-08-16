from django.contrib import admin
from django.urls import path
from . import views
app_name="mainapp"

urlpatterns = [
    path('home/', views.home),
    path('helplinenumbers/', views.helplinenumbers,name="helplinenumbers"),
    path('disastercamps/', views.disastercamps,name="disastercamps"),
]
