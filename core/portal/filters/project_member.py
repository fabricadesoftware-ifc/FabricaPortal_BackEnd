import django_filters
from core.portal.models import Project

class ProjectFilter(django_filters.FilterSet):
    member_id = django_filters.NumberFilter(method='filter_by_member')

    def filter_by_member(self, queryset, name, value):
        return queryset.filter(members__id=value)

    class Meta:
        model = Project
        fields = ['member_id']
