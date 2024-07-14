from django.db import models

# Create your models here.
class ClassPeriod(models.Model):
    start_time =models.DateField()
    end_time =models.DateField()
    course =models.CharField(max_length=50)
    classroom =models.CharField(max_length=150)
    day_of_the_week =models.CharField(max_length=7)


    def __str__(self):
        return self.classroom




