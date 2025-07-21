from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import KPAForm
from .serializers import KPAFormSerializer

class KPAFormCreateView(generics.CreateAPIView):
    queryset = KPAForm.objects.all()
    serializer_class = KPAFormSerializer

class KPAFormDetailView(generics.RetrieveAPIView):
    queryset = KPAForm.objects.all()
    serializer_class = KPAFormSerializer
