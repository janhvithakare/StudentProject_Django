from django.urls import path
from . import views

urlpatterns = [
    path('sample2/', views.sample2, name='sample2'),
]
