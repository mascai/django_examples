from django.contrib import admin
from django.urls import path, include
from cars.views import *

app_name = 'car'

urlpatterns = [
    path('car/create/', CarCreateView.as_view(), name='CarCreate'),
    path('car/detail/<int:pk>/', CarDetailView.as_view(), name='CarDetail'),
    path('all/', CarsListView.as_view(), name='CarCreate'),
]
