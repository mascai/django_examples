from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailsSerializer, CarsListSerializer
from cars.models import Cars
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailsSerializer

class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Cars.objects.all()
    permission_classes = (IsAdminUser, )


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailsSerializer
    queryset = Cars.objects.all()
    authentication_classes = (TokenAuthentication,) 
    permission_classes = (IsOwnerOrReadOnly, )