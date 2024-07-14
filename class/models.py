from django.db import models
# from courses.models import Course
from student.models import Student

class SchoolClass(models.Model):
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE, default=1)
    class_name = models.CharField(max_length=100)
    class_code = models.CharField(max_length=50)
    room_allocation = models.CharField(max_length=100)
    no_of_tables = models.PositiveSmallIntegerField()
    no_of_students = models.PositiveSmallIntegerField()
    class_representative = models.CharField(max_length=100)
    class_goals = models.TextField()
    class_meeting = models.CharField(max_length=100)
    period_entity = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name
