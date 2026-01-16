from django.shortcuts import render

from rest_framework import viewsets
from .models import MarineAnimal, Category, Tag
from .serializers import MarineAnimalSerializer, CategorySerializer, TagSerializer

# Create your views here.

class MarineAnimalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarineAnimal.objects.all()
    serializer_class = MarineAnimalSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer