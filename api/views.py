from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
# from schoolclass.models import SchoolClass
# from .serializers import SchoolClassSerializer
from course.models import Course
from .serializers import CourseSerializer
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer

# Create your views here.
class StudentListView(APIView):
    def get(self,request):
        students =Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)

# class SchoolClassListView(APIView):
#     def get(self,request):
#         schoolclasses=SchoolClass.objects.all()
#         serializer=SchoolClassSerializer(schoolclasses,many=True)
#         return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self,request):
        teachers =Teacher.objects.all()
        serializer=TeacherSerializer(teachers,many=True)
        return Response(serializer.data)
    
class CourseListView(APIView):
    def get(self,request):
        courses =Course.objects.all()
        serializer =CourseSerializer(courses,many=True)
        return Response(serializer.data)
    
class ClassPeriodListView(APIView):
    def get(self,request):
        classperiods=ClassPeriod.objects.all()
        serializer =ClassPeriodSerializer(classperiods,many=True)
        return Response(serializer.data)
