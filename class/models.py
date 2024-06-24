from django.db import models
from courses.models import Course

class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_code = models.CharField(max_length=50)
    room_allocation = models.CharField(max_length=100)
    no_of_tables = models.PositiveSmallIntegerField()
    no_of_students = models.PositiveSmallIntegerField()
    class_representative = models.CharField(max_length=100)
    class_goals = models.TextField()
    class_meeting = models.CharField(max_length=100)
    period_entity = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.class_name
