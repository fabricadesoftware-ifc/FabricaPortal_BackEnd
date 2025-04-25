import django_filters
from core.portal.models import Member

class MemberFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains") 
    type = django_filters.ChoiceFilter(field_name="type", choices=Member.TypeChoices.choices)

    class Meta:
        model = Member
        fields = ["name", "type"]
