from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from courses.models import Course
from courses.serializers import CourseSerializer
from courses.permissions import IsAdminUserOrReadOnly

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminUserOrReadOnly,)