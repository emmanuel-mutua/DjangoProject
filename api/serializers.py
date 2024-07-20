

from rest_framework import serializers
from student.models import Student
from classroom.models import ClassRoom
# from schoolclass.models import SchoolClass 
from teacher.models import Teacher
from course.models import Course
from classperiod.models import ClassPeriod


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model =ClassRoom
        fields ="__all__"

# class SchoolClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SchoolClass  
#         fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields ="__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model =Course
        fields ="__all__"

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model =ClassPeriod
        fields ="__all__"
