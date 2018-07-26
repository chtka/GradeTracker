from django.db import models

# Create your models here.
class Course(models.Model):
    department = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    verbose_name = models.CharField(max_length=254, default="")
    institution = models.CharField(max_length=254, default="University of California, San Diego")

    def __str__(self):
        return "%s %s: %s @ %s" % (self.department, self.number, self.verbose_name, self.institution)

    class Meta:
        unique_together = (('department', 'number'),)
