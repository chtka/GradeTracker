from django.db import models
from classes import Class
from heapq import nsmallest


# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=45)
  weight = models.FloatField(default=0)
  weight_alternate = models.FloatField(default=0)
  points_earned = models.FloatField(default=0)
  points_total = models.FloatField(default=0)

  # calculate every time we add an assignment
  grade = models.FloatField(default=100)

  num_drops_allowed = models.IntegerField(default=0)

  class_field = models.ForeignKey(Class, on_delete=models.CASCADE)

  def update_grade(self):
    qs = self.assignment_set.all()
    grades = [assignment.get_grade() for assignment in qs]
    total_assignments = len(qs) - self.num_drops_allowed
    if total_assignments== 0:
      self.grade = 1
    else:
      self.grade = (sum(grades) - sum(nsmallest(self.num_drops_allowed, grades))) / total_assignments
    self.save()
    
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    self.class_field.update_grade()