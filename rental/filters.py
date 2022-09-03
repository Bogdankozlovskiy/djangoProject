import pendulum
from django_filters import FilterSet, BooleanFilter, DateTimeFilter
from rental.models import Borrowed


class BorrowedFilterSet(FilterSet):
    missing = BooleanFilter(field_name='returned', lookup_expr='isnull', label="missing")
    returned_befor = DateTimeFilter(field_name="returned", lookup_expr="lte")
    returned_after = DateTimeFilter(field_name="returned", lookup_expr="gte")
    overdue = BooleanFilter(field_name="returned", method='get_overdue', label="overdue")

    class Meta:
        model = Borrowed
        fields = ['what', 'to_who', 'missing', "returned_befor", "returned_after", "overdue"]

    def get_overdue(self, queryset, field_name, value):
        if value:
            return queryset.filter(
                returned__isnull=True,
                when__lte=pendulum.now().subtract(months=2)
            )
        return queryset
