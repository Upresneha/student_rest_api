from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from itsdangerous import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.models import stu,staff
from.serializers import staffserializer,stuserializer

class student_view(APIView):
    def get(self,request):
        student_1=stu.objects.all()
        serializer=stuserializer(student_1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
class staff_view(APIView):
    def get(self,request):
        staff_1=staff.objects.all()
        serializer=staffserializer(staff_1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
