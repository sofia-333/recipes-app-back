from django_filters.rest_framework import DjangoFilterBackend

from .models import Recipe
from rest_framework import viewsets, status
from .serializers import RecipeSerializer
from .filters import RecipeFilter


class RecipeViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filter_class = RecipeFilter
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
