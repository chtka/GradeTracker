from django.db import models

class Professor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    biography = models.TextField(default="")

    def __str__(self):
      return self.first_name + " " + self.last_name
