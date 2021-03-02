from django.shortcuts import render
from .serializers import LeadSerializer
from .models import Lead
from rest_framework import generics


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer



