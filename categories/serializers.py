from rest_framework import serializers

from categories.models import Category
from assignments.models import Assignment

class CategorySerializer(serializers.ModelSerializer):

  assignments = serializers.SerializerMethodField()
  grade = serializers.ReadOnlyField()

  class Meta:
    model = Category
    fields = ('id', 'assignments', 'name', 'weight', 'weight_alternate', 'num_drops_allowed', 'grade', 'class_field')
  
  def get_assignments(self, obj):
    return Assignment.objects.filter(category__id=obj.id).values()