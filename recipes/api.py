from rest_framework.decorators import api_view
from .models import Recipe
from rest_framework import viewsets, permissions
from .serializers import RecipeSerializer


# @api_view(['GET', 'POST', 'DELETE'])
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    serializer_class = RecipeSerializer
    # http_method_names = ['get', 'post', 'put', 'delete']
