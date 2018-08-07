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

  @property
  def full_desc(self):
    return str(self.course) + ' ' + str(self.professor)

  def __str__(self):
    return str(self.course) + ' | ' + str(self.professor) + ' | ' + self.quarter + str(self.year)

  def update_grade(self):
    qs = self.category_set.all()
    grade = 0
    grade_alternate = 0
    for category in qs:
      grade += category.grade * category.weight
      grade_alternate += category.grade * category.weight_alternate
    self.grade = max(grade, grade_alternate)
    self.save()

# Create your models here.
