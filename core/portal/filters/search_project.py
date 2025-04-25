import django_filters
from core.portal.models import Project
from django.db.models import TextField
from django.db.models.functions import Cast

class ProjectSearchFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    areas = django_filters.CharFilter(method='filter_by_areas')

    class Meta:
        model = Project
        fields = ['name', 'areas']

    def filter_by_areas(self, queryset, name, value):
        area_list = [area.strip() for area in value.split(',') if area.strip()]
        
        for area in area_list:
            queryset = queryset.annotate(
                areas_text=Cast('areas__areas', TextField())
            ).filter(areas_text__icontains=area)
        return queryset
