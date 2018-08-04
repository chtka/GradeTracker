from courses.models import Course
import django_filters

class CourseFilter(django_filters.FilterSet):
  class Meta:
    model = Course
    fields = ['department', 'number, verbose_name',]