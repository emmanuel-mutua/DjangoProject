from django.db import models
from student.models import Student

class Teacher(models.Model):
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    nationality = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    years_of_experience = models.IntegerField()
    place_of_birth = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    salary = models.IntegerField()
    hire_date = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
