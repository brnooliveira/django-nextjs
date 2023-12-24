from django_filters import rest_framework

from .models import Job


class JobFilter(rest_framework.FilterSet):
    keyword = rest_framework.CharFilter(
        field_name='title',
        lookup_expr='contains'
    )
    location = rest_framework.CharFilter(
        field_name='address',
        lookup_expr='contains'
    )
    min_salary = rest_framework.NumberFilter(
        field_name="salary" or 0,
        lookup_expr='gte'
    )
    max_salary = rest_framework.NumberFilter(
        field_name="salary" or 1000000,
        lookup_expr='lte'
    )

    class Meta:
        model = Job
        fields = [
            'education',
            'job_type',
            'experience',
            'min_salary',
            'max_salary',
            'keyword',
            'location'
        ]
