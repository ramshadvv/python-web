from django.urls import path
from userapp import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
]