from django_filters import FilterSet
from .models import *



class CoursesFilter(FilterSet):
    class Meta:
        model = Courses
        fields = {
            'category': ['exact'],
            'price': ['gte', 'lte'],
            'level': ['exact'],
            'created_by': ['exact'],
        }


