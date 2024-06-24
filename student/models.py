from django.db import models

# Create your models here.
from django.db import models
class Student(models.Model):
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email =models.EmailField()
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()
    age=models.SmallIntegerField()
    nationality =models.CharField()
    gender =models.CharField()
    id =models.AutoField()
    course =models.CharField()
    immediate_contact = models.CharField()
    enrollment_date =models

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
