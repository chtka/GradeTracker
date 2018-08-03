from django.db import models

from django.contrib.auth.models import User

from courses.models import Course
from professors.models import Professor

ACADEMIC_QTR_CHOICES = (
  ('FA', 'Fall'),
  ('WI', 'Winter'),
  ('SP', 'Spring'),
  ('SS1', 'Summer Session 1'),
  ('SS2', 'Summer Session 2'),
)

class Class(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
  quarter = models.CharField(choices=ACADEMIC_QTR_CHOICES, max_length=10)
  year = models.IntegerField()
  grade = models.FloatField(default=100)


# Create your models here.
