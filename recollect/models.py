from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=250)
class Course(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    total_credits = models.IntegerField(default=0)
class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    credits = models.IntegerField(default=0)
    is_optional = models.BooleanField(default=False)