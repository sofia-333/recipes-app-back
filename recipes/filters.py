import django_filters
from .models import Recipe


class RecipeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='contains')
    time_to_prepare = django_filters.CharFilter(method='max_time')

    class Meta:
        model = Recipe
        fields = ['title']

    @staticmethod
    def max_time(queryset, name, value):
        queryset = queryset.filter(time_to_prepare__lt=value)
        return queryset
