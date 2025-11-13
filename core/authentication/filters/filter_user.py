import django_filters
from core.authentication.models import User

class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains") 
    type = django_filters.ChoiceFilter(field_name="type", choices=User.TypeChoices.choices)

    class Meta:
        model = User
        fields = ["name", "type"]