from rest_framework import serializers

from classes.models import Class
from courses.models import Course
from professors.models import Professor

class ClassSerializer(serializers.ModelSerializer):

    full_desc = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = ('id', 'course', 'professor', 'quarter', 'year', 'grade', 'full_desc',)
    
    def get_full_desc(self, obj):
        return str(obj.course) + ' with ' + str(obj.professor)

    def create(self, validated_data):
        course = validated_data.pop('course')
        professor = validated_data.pop('professor')
        class_ = Class.objects.create(**validated_data, course_id=course, professor_id=professor)
        return class_
