from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from rest_framework import generics
from .serializers import HomeSerializer
# Create your views here.

class ListHomeView(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
