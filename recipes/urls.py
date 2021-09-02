from django.urls import path
from rest_framework import routers
from .views import RecipeViewSet, calculate_time

app_name = 'recipes'

router = routers.DefaultRouter()
router.register('api/recipes', RecipeViewSet, 'recipes')

urlpatterns = [
                  path('api/recipes/calculate/', calculate_time, name='calculate-time')
               ] + router.urls

