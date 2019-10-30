from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Students
from .serializers import studentSerializer


class Get_students_List(APIView):
    def get(self, request):
        students = Students.objects.all()
        serialized = studentSerializer(students, many=True)
        return Response(serialized.data)


def homepage(request):
    return render(request, 'index.html')
