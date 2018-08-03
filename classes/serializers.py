from rest_framework import serializers

from classes.models import Class
from courses.models import Course
from professors.models import Professor

class ClassSerializer(serializers.ModelSerializer):

    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    professor = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all())

    class Meta:
        model = Class
        fields = ('id', 'course', 'professor', 'quarter', 'year', 'grade',)
    
    def create(self, validated_data):
        course = validated_data.pop('course')
        professor = validated_data.pop('professor')
        class_ = Class.objects.create(**validated_data, course_id=course, professor_id=professor)
        return class_
