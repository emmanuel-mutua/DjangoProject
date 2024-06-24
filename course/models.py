from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_trainer = models.CharField(max_length=100)
    course_objective = models.CharField(max_length=255)
    course_duration = models.DurationField()
    course_description = models.TextField()
    pass_mark = models.IntegerField()
    course_title = models.CharField(max_length=100)
    course_teacher = models.CharField(max_length=100)
    course_resources = models.CharField(max_length=255)
    teaching_assistant = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.course_name