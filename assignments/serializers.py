from rest_framework import serializers
from .models import Assignment

class AssignmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Assignment
    fields = ('id', 'name', 'category', 'points_total', 'points_earned')