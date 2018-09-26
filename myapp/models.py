from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 30)
    roll = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
