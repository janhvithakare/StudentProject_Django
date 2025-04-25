from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sample1/', views.sample1, name='sample1'),
]
