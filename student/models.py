from django.db import models

# Create your models here.
from django.db import models
class Student(models.Model):
    Student_id =models.IntegerField(default=1)
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email =models.EmailField()
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()
    age=models.SmallIntegerField()
    nationality =models.CharField(max_length=50)
    gender =models.CharField(max_length=50)
    course =models.CharField(max_length=40)
    immediate_contact = models.CharField(max_length=20)
    enrollment_date =models

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
