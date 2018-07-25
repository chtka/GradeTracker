from rest_framework import serializers

from courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'department', 'number', 'verbose_name', 'institution')