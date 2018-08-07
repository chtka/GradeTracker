from django.db import models
from categories.models import Category

class Assignment(models.Model):
  name = models.CharField(max_length=254)
  points_total = models.FloatField()
  points_earned = models.FloatField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    self.category.update_grade()
  
  @property
  def grade(self):
    return self.points_earned / self.points_total

  