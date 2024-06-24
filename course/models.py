from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_Length = 20)
    description = models.CharField()
    location = models.CharField()
    course_type = models.CharField(max_Length = 20)
    course_duration = models.IntegerField()
    course_level = models.CharField()
    course_fee = models.IntegerField()
    course_trainer = models.CharField()
    course_students = models.IntegerField()
    course_date = models.DateField()
    def __str__(self):
        return f"{self.name}{self.name}"
