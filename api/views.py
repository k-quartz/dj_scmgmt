from django.shortcuts import render
from django.http import HttpResponse
from api import serializers
from api import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

def index(request):
    return HttpResponse("Akash")

class ListEmployee(APIView):
    #permission_classes=(IsAuthenticated,)
    
    
    def get(self,request):
        employee=models.Employee.objects.all()
        serializer=serializers.EmployeeSerializer(employee,many=True)
        return Response(serializer.data)

    def post(self,request):
        print(request)
        serializer=serializers.EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=201)

