from rest_framework import serializers

from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):

  assignments = serializers.SerializerMethodField('get_assignments')

  class Meta:
    model = Category
    fields = ('id', 'assigments', 'name', 'weight', 'weight_alternate', 'num_drops_allowed', 'grade')
  
  def get_assignments(self, obj):
    return qs = self.assignment_set().values()