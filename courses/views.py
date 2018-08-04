from django_filters import rest_framework as filters

from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from courses.models import Course
from courses.serializers import CourseSerializer
from courses.permissions import IsAdminUserOrReadOnly

class CourseFilter(filters.FilterSet):

    verbose_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Course
        fields = ['department', 'number',]

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourseFilter
    


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminUserOrReadOnly,)