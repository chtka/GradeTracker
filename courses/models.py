from django.db import models

# Create your models here.
class Course(models.Model):
    department = models.CharField(max_length=45)
    number = models.CharField(max_length=45)

    verbose_name = models.CharField(max_length=254, default="")
    institution = models.CharField(max_length=254, default="")
