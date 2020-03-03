from . import views
from django.urls import path

urlpatterns = [
    path('hello/', views.index, name= 'index'),
    path('', views.show, name= 'show'),
]