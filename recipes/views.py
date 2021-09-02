import json
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Recipe
from rest_framework import viewsets, status
from .serializers import RecipeSerializer
from .filters import RecipeFilter


class RecipeViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filter_class = RecipeFilter
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


@api_view(['POST'])
def calculate_time(request):
    recipes = Recipe.objects.filter(id__in=request.data)
    recipes_times = [r.time_to_prepare for r in recipes]
    time = sum(recipes_times)
    return Response(json.dumps(time), status=status.HTTP_200_OK)
