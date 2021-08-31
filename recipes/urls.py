from rest_framework import routers
from .views import RecipeViewSet

app_name = 'recipes'

router = routers.DefaultRouter()
router.register('api/recipes', RecipeViewSet, 'recipes')

urlpatterns = router.urls
